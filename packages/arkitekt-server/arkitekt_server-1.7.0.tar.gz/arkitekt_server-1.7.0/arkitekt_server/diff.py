import difflib
import secrets
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
import typer
from .config import (
    ArkitektServerConfig,
    BaseService,
    LocalDBConfig,
    Membership,
    RemoteDBConfig,
    GlobalAdminConfig,
    SpecificAdminConfig,
    LocalRedisConfig,
    LocalBucketConfig,
    LocalAuthConfig,
    RemoteRedisConfig,
    User,
    generate_alpha_numeric_string,
)
import yaml


def iterate_service(config: ArkitektServerConfig) -> list[BaseService]:
    """Iterate over the services in the configuration."""
    all_services = [
        config.rekuest,
        config.kabinet,
        config.mikro,
        config.fluss,
        config.elektro,
        config.lok,
        config.alpaka,
        config.kraph,
    ]

    services = []
    for service in all_services:
        if isinstance(service, BaseService):
            if service.enabled:
                services.append(service)
        else:
            raise TypeError(
                f"Expected BaseServiceConfig, got {type(service).__name__} instead."
            )

    return services


def create_basic_config_values(
    config: ArkitektServerConfig, service: BaseService
) -> Dict[str, Any]:
    """
    Create basic configuration values for a service.

    This function generates the common configuration structure that most
    Arkitekt services need, including database connections, Redis settings,
    authentication, and S3 storage configuration.

    Args:
        config: The main Arkitekt server configuration
        service: The specific service configuration to generate values for

    Returns:
        A dictionary containing the service configuration values

    Raises:
        TypeError: If the service has an unsupported database or Redis configuration type
    """
    db: dict[str, str | int] = {}
    if isinstance(service.db_config, LocalDBConfig):
        db = {
            "db_name": service.db_config.db,
            "engine": "django.db.backends.postgresql",
            "host": "db",
            "password": config.db.postgres_password,
            "port": 5432,
            "username": config.db.postgres_user,
        }
    elif isinstance(service.db_config, RemoteDBConfig):
        db = {
            "db_name": service.db_config.db,
            "engine": "django.db.backends.postgresql",
            "host": service.db_config.host,
            "password": service.db_config.password,
            "port": service.db_config.port,
            "username": service.db_config.user,
        }
    else:
        raise TypeError(
            f"Expected LocalDBConfig or RemoteDBConfig, got {type(service.db_config).__name__} instead."
        )

    django_admin: dict[str, str] | None = None
    if isinstance(service.admin_config, GlobalAdminConfig):
        django_admin = {
            "email": config.global_admin_email,
            "password": config.global_admin_password,
            "username": config.global_admin,
        }
    elif isinstance(service.admin_config, SpecificAdminConfig):
        django_admin = {
            "email": service.admin_config.email,
            "password": service.admin_config.password,
            "username": service.admin_config.username,
        }
    else:
        raise TypeError(
            f"Expected GlobalAdminConfig or SpecificAdminConfig, got {type(service.admin_config).__name__} instead."
        )

    redis: dict[str, str | int] | None = None
    if isinstance(service.redis_config, LocalRedisConfig):
        redis = {
            "host": config.local_redis.host,
            "port": config.local_redis.internal_port,
        }
    elif isinstance(service.redis_config, RemoteRedisConfig):
        redis = {
            "host": service.redis_config.host,
            "port": service.redis_config.port,
        }
    else:
        raise TypeError(
            f"Expected LocalRedisConfig or RemoteRedisConfig, got {type(service.redis_config).__name__} instead."
        )

    script_name = service.host
    config_values: dict[str, Any] = {
        "csrf_trusted_origins": [],
        "db": db,
        "django": {
            "admin": django_admin,
            "debug": service.debug,
            "hosts": service.allowed_hosts,
            "secret_key": service.secret_key,
        },
        "lok": {
            "issuer": config.lok.issuer,
            "key_type": config.lok.auth_key_pair.key_type,
            "public_key": config.lok.auth_key_pair.public_key,
        },
        "force_script_name": script_name,
        "redis": redis,
        "s3": {
            "access_key": config.minio.access_key,
            "secret_key": config.minio.secret_key,
            "buckets": {
                key: config.bucket_name for key, config in service.get_buckets().items()
            },
            "host": config.minio.host,
            "port": config.minio.internal_port,
            "protocol": "http",
        },
    }
    return config_values


def clone_repo(github_repo: str, target_dir: str, base_dir: Path):
    """Clone a GitHub repository into a target directory."""

    if (Path(base_dir) / Path(target_dir)).exists():
        # Check if the directory is the github repo of this service
        if (Path(base_dir) / Path(target_dir) / ".git").exists():
            # check if origin is remote
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                check=True,
                capture_output=True,
                cwd=Path(base_dir) / Path(target_dir),
            )
            if result.returncode == 0:
                if result.stdout:
                    if not result.stdout.strip().decode("utf-8") == github_repo:
                        raise ValueError(
                            f"Already cloned repository at path {Path(base_dir) / Path(target_dir)} of already present repository does not match expected {github_repo}. Got: {result.stdout.strip()}. Please remove directory manually before proceeding"
                        )
                    else:
                        print(
                            f"Directory {target_dir} is already a git repository with matching remote origin, skipping clone...."
                        )
                else:
                    raise ValueError(
                        f"Directory {target_dir} is already a git repository without remote origin. Please check this before proceeding."
                    )

            else:
                raise ValueError(
                    f"Directory {target_dir} is a git repository without remote origin. Please check this before proceeding."
                )
    else:
        subprocess.run(
            ["git", "clone", github_repo, target_dir], check=True, cwd=base_dir
        )


def create_config(
    service_name: str, config_values: Dict[str, Any], base_path: Path
) -> None:
    """Create a service configuration dictionary."""
    service_dir = base_path / "configs"
    service_dir.mkdir(parents=True, exist_ok=True)

    (service_dir / f"{service_name}.yaml").write_text(
        yaml.dump(config_values, default_flow_style=False)
    )


def build_default_service(
    path: Path, config: ArkitektServerConfig, service: BaseService
) -> dict[str, Any]:
    """
    Build a default Docker Compose service definition.

    Creates a standard service configuration for Docker Compose with common
    settings like image, command, dependencies, and volume mounts.

    Args:
        config: The main Arkitekt server configuration
        service: The service to create a Docker Compose definition for

    Returns:
        A dictionary representing a Docker Compose service definition
    """

    docker_service = {
        "image": service.image,
        "command": service.build_run_command(),
        "depends_on": ["redis", "db", "minio"],
        "stop_grace_period": "2s",
        "volumes": [f"./configs/{service.host}.yaml:/workspace/config.yaml"],
        "deploy": {
            "restart_policy": {
                "condition": "on-failure",
                "delay": "10s",
                "max_attempts": 10,
                "window": "300s",
            }
        },
    }

    if service.mount_github:
        cloned_repo = f"./repos/{service.host}"
        clone_repo(
            github_repo=service.github_repo, target_dir=cloned_repo, base_dir=path
        )

        docker_service["volumes"].append(
            f"./repos/{service.host}:/workspace/repos/{service.host}"
        )

        del docker_service["image"]
        docker_service["build"] = cloned_repo

    return docker_service


def create_fluss_config(config: ArkitektServerConfig, base_path: Path) -> None:
    """
    Create configuration file for the Fluss workflow service.

    Args:
        config: The main Arkitekt server configuration
        base_path: Directory where the configuration file should be written
    """
    fluss_config = create_basic_config_values(config, config.fluss)
    create_config("fluss", fluss_config, base_path)


def create_lok_config(config: ArkitektServerConfig, base_path: Path) -> None:
    """
    Create configuration file for the Lok authentication service.

    Args:
        config: The main Arkitekt server configuration
        base_path: Directory where the configuration file should be written
    """

    lok_config = create_basic_config_values(config, config.lok)

    create_config("lok", lok_config, base_path)


def parse_local_db_requests(config: ArkitektServerConfig) -> list[LocalDBConfig]:
    """
    Parse and collect all local database configuration requests.

    Iterates through all enabled services and extracts those that require
    local database connections. This is used to determine what databases
    need to be created in the PostgreSQL container.

    Args:
        config: The main Arkitekt server configuration

    Returns:
        A list of LocalDBConfig objects for all services requiring local databases
    """
    db_names: list[LocalDBConfig] = []
    for service in iterate_service(config):
        if isinstance(service.db_config, LocalDBConfig):
            db_names.append(service.db_config)
    return db_names


def parse_local_auth_requests(config: ArkitektServerConfig) -> list[LocalDBConfig]:
    """
    Parse and collect all local authentication configuration requests.

    Note: This function currently has the same implementation as parse_local_db_requests,
    which appears to be a bug. It should be collecting LocalAuthConfig objects instead.

    Args:
        config: The main Arkitekt server configuration

    Returns:
        A list of LocalAuthConfig objects (currently returns LocalDBConfig due to bug)
    """
    db_names: list[LocalDBConfig] = []
    for service in iterate_service(config):
        if isinstance(service.db_config, LocalDBConfig):
            db_names.append(service.db_config)
    return db_names


def parse_local_redis_request(config: ArkitektServerConfig) -> list[LocalRedisConfig]:
    """
    Parse and collect all local Redis configuration requests.

    Iterates through all enabled services and extracts those that require
    local Redis connections. This is used to determine if a Redis container
    needs to be started in the deployment.

    Args:
        config: The main Arkitekt server configuration

    Returns:
        A list of LocalRedisConfig objects for all services requiring local Redis
    """
    redis_dbs: list[LocalRedisConfig] = []
    for service in iterate_service(config):
        if isinstance(service.redis_config, LocalRedisConfig):
            redis_dbs.append(service.redis_config)
    return redis_dbs


def parse_local_bucket_configs(config: ArkitektServerConfig) -> list[LocalBucketConfig]:
    """
    Parse and collect all local bucket configuration requests.

    Iterates through all enabled services and extracts bucket configurations
    that use local MinIO storage. This is used to determine what S3 buckets
    need to be created in the MinIO container.

    Args:
        config: The main Arkitekt server configuration

    Returns:
        A list of LocalBucketConfig objects for all local buckets needed
    """
    bucket_names: list[LocalBucketConfig] = []
    for service in iterate_service(config):
        buckets = service.get_buckets()
        if isinstance(buckets, dict):
            for bucket_name, bucket_config in buckets.items():
                if isinstance(bucket_config, LocalBucketConfig):
                    bucket_names.append(bucket_config)
    return bucket_names


def create_caddyfilepath(service: BaseService) -> str:
    """
    Create a Caddyfile path matcher and handler for a single service.

    This is a helper function that generates the Caddy configuration block
    for routing requests to a specific service based on URL path matching.

    Args:
        service: The service to create routing configuration for

    Returns:
        A string containing the Caddy configuration block for this service
    """
    caddyfile = f"\t@{service.host} path /{service.host}*\n"
    caddyfile += "\thandle @" + service.host + " { \n"
    caddyfile += f"\t\treverse_proxy {service.host}:{service.internal_port}\n"
    caddyfile += "\t}\n\n"
    return caddyfile


def create_caddy_file(config: ArkitektServerConfig) -> str:
    """
    Create a Caddyfile for reverse proxy configuration.

    Generates a Caddy reverse proxy configuration that routes requests to the
    appropriate services based on URL paths. This includes:
    - Service routing (e.g., /rekuest/* -> rekuest service)
    - Bucket routing for MinIO access
    - Special routes like /.well-known for OAuth/OIDC
    - MinIO admin interface routing

    Args:
        config: The main Arkitekt server configuration

    Returns:
        A string containing the complete Caddyfile configuration

    Raises:
        TypeError: If a service doesn't implement the BaseService protocol
    """

    caddyfile = "http:// {\n"

    for service in iterate_service(config):
        if not isinstance(service, BaseService):
            raise TypeError(
                f"Expected BaseServiceConfig, got {type(service).__name__} instead."
            )
        caddyfile += f"\t@{service.host} path /{service.host}*\n"
        caddyfile += "\thandle @" + service.host + " { \n"
        caddyfile += f"\t\treverse_proxy {service.host}:{service.internal_port}\n"
        caddyfile += "\t}\n\n"

    for bucket in parse_local_bucket_configs(config):
        caddyfile += f"\t@{bucket.bucket_name} path /{bucket.bucket_name}*\n"
        caddyfile += "\thandle @" + bucket.bucket_name + " { \n"
        caddyfile += (
            f"\t\treverse_proxy {config.minio.host}:{config.minio.internal_port}\n"
        )
        caddyfile += "\t}\n\n"

    caddyfile += "\t@.well-known path /.well-known/*\n"
    caddyfile += "\thandle @.well-known {\n"
    caddyfile += "\t\trewrite * /lok{uri}\n"
    caddyfile += f"\t\treverse_proxy {config.lok.host}:{config.lok.internal_port}\n"
    caddyfile += "\t}\n\n"

    caddyfile += "\t@minio path /minio/*\n"
    caddyfile += "\thandle @minio {\n"
    caddyfile += f"\t\treverse_proxy {config.minio.host}:{config.minio.internal_port}\n"
    caddyfile += "\t}\n\n"

    caddyfile += "}\n"
    return caddyfile


class AliasConfig(BaseModel):
    """
    Configuration for service aliases in the Arkitekt ecosystem.

    Aliases define how services are exposed and accessed through different
    protocols and layers (e.g., HTTP, WebSocket, public/private access).

    Attributes:
        challenge: The challenge type for authentication/access
        kind: The protocol or connection type (e.g., 'http', 'ws')
        layer: The access layer (e.g., 'public', 'private')
        path: The URL path where the service is accessible
    """

    challenge: str
    kind: str
    layer: str
    path: str | None = None


class InstanceConfig(BaseModel):
    """
    Configuration for a service instance in the Arkitekt ecosystem.

    Instances represent deployed services that can be discovered and
    connected to by other services or client applications.

    Attributes:
        service: The service type identifier (e.g., 'live.arkitekt.rekuest')
        identifier: Unique identifier for this instance
        alias: List of aliases defining how to access this instance
    """

    service: str
    identifier: str
    aliases: list[AliasConfig] = []


class RedeemTokenConfig(BaseModel):
    """
    Configuration for redeem tokens used in service authentication.

    Redeem tokens allow services or users to exchange temporary tokens
    for persistent authentication credentials.

    Attributes:
        token: The redeemable token string
        user: The user associated with this token
    """

    token: str
    user: str
    organization: str


def service_to_instance_config(
    service: BaseService, service_name: str
) -> InstanceConfig:
    """
    Convert a service configuration to an instance configuration.

    This creates the instance metadata that gets registered with the Lok
    authentication service, allowing other services and clients to discover
    and connect to this service instance.

    Args:
        service: The service configuration to convert
        service_name: The canonical service name (e.g., 'live.arkitekt.rekuest')

    Returns:
        An InstanceConfig object representing this service instance
    """
    return InstanceConfig(
        service=service_name,
        identifier=service.host,
        aliases=[
            AliasConfig(
                challenge="ht", kind="relative", layer="public", path=service.host
            )
        ],
    )


def write_virtual_config_files(tmpdir: Path, config: ArkitektServerConfig):
    """
    Generate all configuration files needed for deployment.

    This is the main function that orchestrates the creation of all necessary
    configuration files for a complete Arkitekt deployment, including:

    - Docker Compose service definitions
    - Individual service configuration files (YAML)
    - Caddyfile for reverse proxy
    - MinIO initialization configuration
    - Lok authentication service setup with users, groups, and instances

    The function analyzes the configuration to determine which services are
    enabled and what infrastructure components (databases, Redis, storage)
    are needed, then generates appropriate configurations for each.

    Args:
        tmpdir: Temporary directory where configuration files will be written
        config: The main Arkitekt server configuration to generate files from
    """

    services = {}

    instances: list[InstanceConfig] = []  # Service instances for Lok registration
    redeem_tokens: list[
        RedeemTokenConfig
    ] = []  # Authentication tokens for service access

    for org in config.organizations:
        # Add a bot user for each organization
        config.users.append(
            User(
                username=org.bot_name,
                password=generate_alpha_numeric_string(12),
                email=None,
                active_organization=org.identifier,
                memberships=[
                    Membership(
                        organization=org.identifier,
                        roles=["bot"],
                    )
                ],
            )
        )

    # Configure PostgreSQL database if any services need local databases
    local_dbs = parse_local_db_requests(config)
    if len(local_dbs) > 1:
        services["db"] = {
            "image": config.db.image,
            "environment": {
                "POSTGRES_MULTIPLE_DATABASES": ",".join(
                    [request.db for request in local_dbs]
                ),
                "POSTGRES_PASSWORD": config.db.postgres_password,
                "POSTGRES_USER": config.db.postgres_user,
            },
            "volumes": [
                f"{config.db.mount or config.db.volume_name}:/var/lib/postgresql/data"
            ],
        }

    # Configure Redis service if any services need local Redis
    local_redis_requests = parse_local_redis_request(config)
    if len(local_redis_requests) > 1:
        services[config.local_redis.host] = {
            "image": config.local_redis.image,
        }

    # Configure MinIO object storage if any services need local buckets
    local_bucket_requests = parse_local_bucket_configs(config)
    if len(local_bucket_requests) > 1:
        services[config.minio.host] = {
            "image": config.minio.image,
            "command": "server /data",
            "environment": {
                "MINIO_ROOT_USER": config.minio.root_user,
                "MINIO_ROOT_PASSWORD": config.minio.root_password,
            },
            "stop_grace_period": "2s",
            "volumes": [f"{config.minio.mount or config.minio.volume_name}:/data"],
        }

        # Configuration for MinIO initialization (creates buckets and users)
        init_config: dict[str, Any] = {
            "buckets": [{"name": req.bucket_name} for req in local_bucket_requests],
            "users": [
                {
                    "access_key": config.minio.access_key,
                    "secret_key": config.minio.secret_key,
                    "policies": ["readwrite"],
                    "name": "Default User",
                }
            ],
        }
        instances.append(
            service_to_instance_config(config.fluss, "live.arkitekt.fluss")
        )

        create_config(config.minio.init_container_host, init_config, tmpdir)
        # MinIO initialization container that sets up buckets and users on startup
        services[config.minio.init_container_host] = {
            "image": config.minio.init_container_image,
            "volumes": [
                f"./configs/{config.minio.init_container_host}.yaml:/workspace/config.yaml"
            ],
            "stop_grace_period": "2s",
            "environment": {
                "MINIO_ROOT_USER": config.minio.root_user,
                "MINIO_ROOT_PASSWORD": config.minio.root_password,
                "MINIO_HOST": f"http://{config.minio.host}:{config.minio.internal_port}",
            },
            "depends_on": {config.minio.host: {"condition": "service_started"}},
        }

    # Configure deployer service for container orchestration
    if config.deployer.enabled:
        for org in config.organizations:
            token = secrets.token_hex(16)

            services[config.deployer.host + org.name] = {
                "image": config.deployer.image,
                "volumes": ["/var/run/docker.sock:/var/run/docker.sock"],
                "command": (
                    f"arkitekt-next run prod --redeem-token={token} "
                    f"--url http://{config.gateway.host}:{config.gateway.internal_port}"
                ),
                "stop_grace_period": "2s",
                "deploy": {
                    "restart_policy": {
                        "condition": "on-failure",
                        "delay": "10s",
                        "max_attempts": 10,
                        "window": "300s",
                    }
                },
                "environment": {
                    "ARKITEKT_GATEWAY": f"http://{config.gateway.host}:{config.gateway.internal_port}",
                    "ARKITEKT_NETWORK": config.internal_network,
                    "INSTANCE_ID": "default",
                    "DEPLOYER_ORGANIZATION": org.name,
                },
            }

            redeem_tokens.append(
                RedeemTokenConfig(
                    token=token, user=org.bot_name, organization=org.identifier
                )
            )

    # Configure individual Arkitekt services
    if config.fluss.enabled:
        services[config.fluss.host] = build_default_service(
            tmpdir, config, config.fluss
        )

        gconfig = create_basic_config_values(config, config.fluss)
        create_config(config.fluss.host, gconfig, tmpdir)
        instances.append(
            service_to_instance_config(config.fluss, "live.arkitekt.fluss")
        )

    if config.kabinet.enabled:
        services[config.kabinet.host] = build_default_service(
            tmpdir, config, config.kabinet
        )

        gconfig = create_basic_config_values(config, config.kabinet)

        repo_map = []
        for org in config.organizations:
            repo_map.append(
                {
                    "organization": org.identifier,
                    "repos": [repo for repo in config.kabinet.ensured_repositories],
                }
            )

        gconfig["repo_map"] = repo_map

        create_config(config.kabinet.host, gconfig, tmpdir)
        instances.append(
            service_to_instance_config(config.kabinet, "live.arkitekt.kabinet")
        )

    if config.elektro.enabled:
        services[config.elektro.host] = build_default_service(
            tmpdir, config, config.elektro
        )

        gconfig = create_basic_config_values(config, config.elektro)
        create_config(config.elektro.host, gconfig, tmpdir)
        instances.append(
            service_to_instance_config(config.elektro, "live.arkitekt.elektro")
        )

    if config.kraph.enabled:
        services[config.kraph.host] = build_default_service(
            tmpdir, config, config.kraph
        )

        gconfig = create_basic_config_values(config, config.kraph)

        create_config(config.kraph.host, gconfig, tmpdir)
        instances.append(
            service_to_instance_config(config.kraph, "live.arkitekt.kraph")
        )

    if config.alpaka.enabled:
        services[config.alpaka.host] = build_default_service(
            tmpdir, config, config.alpaka
        )

        lok_config = create_basic_config_values(config, config.alpaka)
        create_config(config.alpaka.host, lok_config, tmpdir)
        instances.append(
            service_to_instance_config(config.alpaka, "live.arkitekt.alpaka")
        )

    if config.mikro.enabled:
        services[config.mikro.host] = build_default_service(
            tmpdir, config, config.mikro
        )

        lok_config = create_basic_config_values(config, config.mikro)
        create_config(config.mikro.host, lok_config, tmpdir)
        instances.append(
            service_to_instance_config(config.mikro, "live.arkitekt.mikro")
        )

    if config.rekuest.enabled:
        services[config.rekuest.host] = build_default_service(
            tmpdir, config, config.rekuest
        )

        lok_config = create_basic_config_values(config, config.rekuest)
        create_config(config.rekuest.host, lok_config, tmpdir)
        instances.append(
            service_to_instance_config(config.rekuest, "live.arkitekt.rekuest")
        )

    exposed_ports = []

    if config.gateway.exposed_http_port:
        exposed_ports.append(f"{config.gateway.exposed_http_port}:80")

    if config.gateway.exposed_https_port:
        exposed_ports.append(f"{config.gateway.exposed_https_port}:443")

    # Configure Caddy reverse proxy/gateway
    services[config.gateway.host] = {
        "image": config.gateway.image,
        "ports": exposed_ports,
        "networks": [config.internal_network, "default"],
        "volumes": ["./configs/Caddyfile:/etc/caddy/Caddyfile"],
    }

    # Generate and write the Caddyfile configuration
    caddyfile = create_caddy_file(config)
    mkkdirs = tmpdir / "configs"
    mkkdirs.mkdir(parents=True, exist_ok=True)
    (tmpdir / "configs" / "Caddyfile").write_text(caddyfile)

    default_lok_service = build_default_service(tmpdir, config, config.lok)
    default_lok_service["environment"] = {
        "AUTHLIB_INSECURE_TRANSPORT": "true",
    }
    # Create Lok service configuration
    services[config.lok.host] = default_lok_service

    instances.append(service_to_instance_config(config.lok, "live.arkitekt.lok"))

    instances.append(
        InstanceConfig(
            service="live.arkitekt.s3",
            identifier=config.minio.host,
            aliases=[
                AliasConfig(
                    challenge="minio/health/live", kind="relative", layer="public"
                )
            ],
        )
    )

    lok_config = create_basic_config_values(config, config.lok)

    lok_config["deployment"] = {"name": "test"}
    lok_config["email"] = {
        "host": config.email.host if config.email else "NOT_SET",
        "port": config.email.port if config.email else 587,
        "user": config.email.username if config.email else "NOT_SET",
        "password": config.email.password if config.email else "NOT_SET",
        "email": config.email.email if config.email else "NOT_SET",
    }
    lok_config["layers"] = [{"kind": "public", "identifier": "public"}]
    lok_config["private_key"] = config.lok.auth_key_pair.private_key
    lok_config["public_key"] = config.lok.auth_key_pair.public_key
    lok_config["redeem_tokens"] = [instance.model_dump() for instance in redeem_tokens]

    lok_config["scopes"] = {
        "kabinet_add_repo": "Add repositories to the database",
        "kabinet_deploy": "Deploy containers",
        "mikro_read": "Read image from the database",
        "mikro_write": "Write image to the database",
        "openid": "The open id connect scope",
        "read": "A generic read access",
        "read_image": "Read image from the database",
        "rekuest_agent": "Act as an agent",
        "rekuest_call": "Call other apps with rekuest",
        "write": "A generic write access",
    }
    lok_config["token_expire_seconds"] = 800000
    lok_config["organizations"] = [org.model_dump() for org in config.organizations]
    lok_config["users"] = [user.model_dump() for user in config.users]
    lok_config["roles"] = [role.model_dump() for role in config.roles]
    lok_config["instances"] = [instance.model_dump() for instance in instances]

    create_config(config.lok.host, lok_config, tmpdir)

    volumes: list[str] = []
    if not config.db.mount:
        volumes.append(f"{config.db.volume_name}")
    if not config.minio.mount:
        volumes.append(f"{config.minio.volume_name}")

    docker_compose_content: Dict[str, Any] = {
        "services": services,
        "networks": {
            config.internal_network: {
                "driver": "bridge",
                "name": config.internal_network,
            }
        },
        "volumes": {vol: {} for vol in volumes},
    }

    (tmpdir / "docker-compose.yaml").write_text(
        yaml.dump(docker_compose_content, default_flow_style=False)
    )


def collect_all_files(base: Path) -> dict[Path, Path]:
    """
    Recursively collect all files in a directory tree.
    This function scans the specified directory and returns a dictionary
    mapping relative file paths to their absolute Path objects. It is useful
    for comparing directory structures or preparing for deployment.

    Args:
        base: The base directory to scan

    Returns:
        A dictionary mapping relative paths to absolute Path objects
    """
    files: dict[Path, Path] = {}
    for path in base.rglob("*"):
        if path.is_file():
            relative_path = path.relative_to(base)
            files[relative_path] = path
    return files


def compare_filesystems(
    virtual_dir: Path, real_dir: Path, *, allow_deletes: bool = True
):
    """
    Compare virtual and real directory structures and display differences.

    This function performs a comprehensive comparison between the generated
    (virtual) configuration files and the existing (real) deployment files.
    It identifies files that would be:
    - Created (exist in virtual but not real)
    - Deleted (exist in real but not virtual, if allow_deletes=True)
    - Modified (exist in both but with different content)

    For modified files, it displays a unified diff showing the exact changes.

    Args:
        virtual_dir: Directory containing the generated configuration files
        real_dir: Directory containing the existing deployment files
        allow_deletes: Whether to report files that would be deleted
    """
    virtual_files = collect_all_files(virtual_dir)
    real_files = collect_all_files(real_dir)

    all_paths = sorted(set(virtual_files) | set(real_files))

    for path in all_paths:
        v_file = virtual_files.get(path)
        r_file = real_files.get(path)

        if v_file and not r_file:
            print(f"[+] Would create: {path}")
        elif not v_file and r_file:
            if allow_deletes:
                print(f"[-] Would delete: {path}")
        elif v_file and r_file:
            v_lines = v_file.read_text().splitlines(keepends=True)
            r_lines = r_file.read_text().splitlines(keepends=True)

            if v_lines != r_lines:
                diff = list(
                    difflib.unified_diff(
                        r_lines,
                        v_lines,
                        fromfile=f"{path} (current)",
                        tofile=f"{path} (new)",
                        lineterm="",
                    )
                )
                print(f"[~] Would modify: {path}")
                print("".join(diff))


def run_dry_run_diff(
    config: ArkitektServerConfig,
    real_dir: Path,
    allow_deletes: bool = False,
    yes: bool = False,
):
    """
    Execute a dry-run comparison and optionally apply changes.

    This is the main entry point for the configuration diff workflow. It:
    1. Creates a temporary directory with the generated configuration
    2. Compares it to the existing deployment directory
    3. Shows the user what changes would be made
    4. Prompts for confirmation before applying changes
    5. Copies the new configuration files if confirmed

    This provides a safe way to preview and apply configuration changes
    without accidentally overwriting important files.

    Args:
        config: The Arkitekt server configuration to deploy
        real_dir: The target directory for the deployment files
        allow_deletes: Whether to allow deletion of existing files

    Raises:
        typer.Abort: If the user declines to apply the changes
    """

    with tempfile.TemporaryDirectory() as tmp:
        virtual_dir = Path(tmp)
        print(f"🛠  Generating virtual config in: {virtual_dir}")
        write_virtual_config_files(virtual_dir, config)

        print(f"\n🔍 Comparing to real directory: {real_dir}\n")
        compare_filesystems(virtual_dir, real_dir, allow_deletes=allow_deletes)

        if not yes:
            typer.confirm(
                "Do you want to apply these changes?",
                abort=True,
            )

        # copy the virtual files to the real directory
        for path in virtual_dir.rglob("*"):
            if path.is_file():
                relative_path = path.relative_to(virtual_dir)
                target_path = real_dir / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "r") as src_file:
                    with open(target_path, "w") as dst_file:
                        dst_file.write(src_file.read())
