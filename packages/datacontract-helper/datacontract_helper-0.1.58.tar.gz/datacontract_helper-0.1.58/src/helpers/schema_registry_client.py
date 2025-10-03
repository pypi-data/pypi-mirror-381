import json
import logging

import click
import requests
from datacontract.data_contract import DataContract

import os


log = logging.getLogger(name="").getChild(suffix=__name__)

SCHEMA_TYPE: str = "PROTOBUF"
SCHEMA_REGISTRY_CONTENT_TYPE: str = "application/vnd.schemaregistry.v1+json"


class SchemaRegistryClient:
    def publish_schema_registry(
        self,
        filename: str,
        subject_name: str,
    ):

        data_contract: DataContract = self._get_data_contract(filename=filename)

        schema_registry: str = self._get_schema_registry(data_contract=data_contract)

        # Запрос на регистрацию схемы
        response: requests.Response = requests.post(
            url=f"{schema_registry}/subjects/{subject_name}/versions",
            headers={"Content-Type": SCHEMA_REGISTRY_CONTENT_TYPE},
            json=self._make_schema_request_data(data_contract=data_contract),
            timeout=200,
        )
        click.echo(message=response.url)
        click.echo(message=response.text)
        click.echo(message=response.status_code)

    def delete_schema_registry(
        self,
        filename: str,
        subject_name: str,
        permanent: bool = False,
    ) -> bool:
        """
        Удаляет схему из Schema Registry по названию
        
        Args:
            filename: Путь к файлу с data contract
            subject_name: Название схемы для удаления
            permanent: Если True - полное удаление, если False - мягкое удаление
        
        Returns:
            bool: True если удаление успешно, False в противном случае
        """

        data_contract: DataContract = self._get_data_contract(filename=filename)
        schema_registry: str = self._get_schema_registry(data_contract=data_contract)

        # Формируем URL в зависимости от типа удаления
        if permanent:
            url = f"{schema_registry}/subjects/{subject_name}?permanent=true"
        else:
            url = f"{schema_registry}/subjects/{subject_name}"

        # Запрос на удаление схемы
        response: requests.Response = requests.delete(
            url=url,
            timeout=200,
        )
        
        click.echo(message=response.url)
        click.echo(message=response.text)
        click.echo(message=response.status_code)

    def validate_schema_registry(
        self,
        subject_name: str,
        filename: str,
        # version: str = "latest",
        # compatibility_type: str = "FULL",
    ):
        # CompatibilityType = Literal["NONE", "FULL", "FORWARD", "BACKWARD", "FULL_TRANSITIVE"]

        data_contract: DataContract = self._get_data_contract(filename=filename)

        schema_registry: str = self._get_schema_registry(data_contract=data_contract)
        #   broker: ht

        print(self._make_schema_request_data(data_contract=data_contract))
        response: requests.Response = requests.post(
            url=f"{schema_registry}/compatibility/subjects/{subject_name}/versions/latest",
            headers={"Content-Type": SCHEMA_REGISTRY_CONTENT_TYPE},
            json=self._make_schema_request_data(data_contract=data_contract),
            timeout=20,
        )
        # click.echo(message=response.url)
        click.echo(message=response.text)

    def _get_data_contract(self, filename: str) -> DataContract:
        if not os.path.exists(path=f"{filename}.yaml"):
            raise FileNotFoundError(f"Data contract file not found: {filename}.yaml")

        data_contract: DataContract = DataContract(
            data_contract_file=f"{filename}.yaml"
        )
        data_contract.lint()
        return data_contract

    def _get_schema_registry(self, data_contract: DataContract) -> str:
        return data_contract.get_data_contract_specification().links["schema_registry"]


    def _make_schema_request_data(self, data_contract: DataContract) -> dict:
        """Создает данные для запроса к Schema Registry."""
        return {
            "schemaType": SCHEMA_TYPE,
            "schema": data_contract.export(export_format="protobuf")["protobuf"],
        }