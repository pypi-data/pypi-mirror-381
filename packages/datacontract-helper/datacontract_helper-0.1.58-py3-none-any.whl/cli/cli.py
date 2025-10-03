import logging
import sys
from pathlib import Path

import click

from helpers import (ModuleBuilder, NexusPublisher, SchemaRegistryClient,
                     WheelBuilder)

# Add the current directory to the import path
current_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(object=current_dir))

# https://datacontract.com/examples/orders-latest/datacontract.yaml


NEXUS_URL: str = "https://nexus.k8s-analytics.ostrovok.in/repository/datacontract_pypi/"

log: logging.Logger = logging.getLogger(name=__name__)

log.setLevel(level=logging.DEBUG)


@click.group()
@click.pass_context
def cli(
    ctx,
):
    ctx.ensure_object(dict)


@cli.command()
@click.option("--filename", required=True)
def create_yaml_from_sql(filename: str):
    """
    команда для разработчиков незнакомых с datacontract,
    этой командой можно тестово создать самый просто datacontract.yml из вашего ddl.sql

    нужен ddl.sql

    uv run --env-file .env python -m src create-yaml-from-sql --filename vertica_datacontract

    uv run datacontract-helper create-yaml-from-sql --filename service_example
    """
    ModuleBuilder().create_yaml_from_sql(filename=filename)


@cli.command()
@click.option("--wheel-version", required=True)
@click.option("--filename", required=True)
def build_wheel(
    wheel_version: str,
    filename: str = "vertica_datacontract",
):
    """
    uv run python -m src build-wheel --wheel-version 0.1.1 --filename service_example

    uv run datacontract-helper build-wheel --wheel-version 0.1.1 --filename service_example

    """

    ModuleBuilder().create_proto_from_yaml(filename=filename)
    ModuleBuilder().generate_python_code_from_proto(filename=filename)
    WheelBuilder().build_wheel(
        filename=filename,
        version=wheel_version,
    )


@cli.command()
@click.option("--filename", required=True)
@click.option("--wheel-version", required=True)
@click.option("--username", required=True, type=str)
@click.option("--password", required=True, type=str)
def publish_package_manual(
    wheel_version: str,
    filename: str,
    username: str,
    password: str,
):
    """


    uv run python -m src publish-package-manual --filename service_example --username n.shokurov --password test_pass

    uv run datacontract-helper publish-package-manual --filename service_example --username n.shokurov --password test_pass


    """

    filepath: str = f"{filename}-{wheel_version}-py3-none-any.whl"
    NexusPublisher().publish_package(
        nexus_pass=password,
        nexus_repo=NEXUS_URL,
        nexus_user=username,
        wheel_file=filepath,
    )


@cli.command()
# @click.option("--filepath", required=True, type=str)
@click.option("--filename", required=True)
@click.option("--wheel-version", required=True)
# @click.option("--nexusurl", required=True, type=str)
@click.option("--username", required=True, type=str)
@click.option("--password", required=True, type=str)
def publish_package(
    # filepath: str,
    wheel_version: str,
    filename: str,
    # nexusurl: str,
    username: str,
    password: str,
):
    """
    Основная команда в cicd,
    при коммите в репозиторий с контрактом
    https://gitlab.ostrovok.ru/dataplatform-infra1/datacontract-example/-/tree/dev_b?ref_type=heads
    происходит запуск этой команды

    срабатывает при наличии datacontract.yaml

    .yaml -> .proto -> _pb2.py -> .whl -> nexus


    uv run python -m src publish-package --filename service_example --username n.shokurov --password test_pass

    uv run datacontract-helper publish-package --filename service_example --username n.shokurov --password test_pass --wheel-version 0.1.1


    """
    ModuleBuilder().create_proto_from_yaml(filename=filename)
    ModuleBuilder().generate_python_code_from_proto(filename=filename)
    WheelBuilder().build_wheel(
        filename=filename,
        version=wheel_version,
    )

    filepath: str = f"{filename}-{wheel_version}-py3-none-any.whl"
    NexusPublisher().publish_package(
        nexus_pass=password,
        nexus_repo=NEXUS_URL,
        nexus_user=username,
        wheel_file=filepath,
    )


@cli.command()
@click.option("--filename", required=True)
@click.option("--subject-name", required=True)
# @click.option("--version")
# @click.option("--compatibility-type", required=False)
def validate_schema_registry(
    filename: str,
    subject_name: str,
    # version: str | None = None,
    # compatibility_type: str | None = None,
):
    """

    uv run python -m src validate-schema-registry --filename "vertica_datacontract" --subject-name vertica_datacontract

    uv run datacontract-helper validate-schema-registry --filename "et_admin_datacontract" --subject-name et_admin_datacontract
    """
    SchemaRegistryClient().validate_schema_registry(
        subject_name=subject_name,
        # version=version,
        filename=filename,
        # compatibility_type=compatibility_type,
    )


@cli.command()
@click.option("--filename", required=True)
@click.option("--subject-name", required=True)
def publish_schema_registry(
    filename: str,
    subject_name: str,
):
    """
    uv run python -m src publish-schema-registry --filename "service_example" --subject-name "etl_scripts.logs-value"

    uv run datacontract-helper publish-schema-registry --filename et_admin_datacontract --subject-name et_admin_datacontract

    """
    SchemaRegistryClient().publish_schema_registry(
        filename=filename, subject_name=subject_name
    )


@cli.command()
@click.option("--filename", required=True)
@click.option("--subject-name", required=True)
def delete_schema_registry(
    filename: str,
    subject_name: str,
):
    """
    uv run python -m src delete-schema-registry --filename "service_example" --subject-name service_example

    uv run datacontract-helper delete-schema-registry --filename et_admin_datacontract --subject-name et_admin_datacontract

    """
    SchemaRegistryClient().delete_schema_registry(
        filename=filename, subject_name=subject_name
    )

