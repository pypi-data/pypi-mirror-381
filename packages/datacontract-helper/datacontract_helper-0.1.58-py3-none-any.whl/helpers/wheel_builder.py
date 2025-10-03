import logging
import os
import shutil
import subprocess
import tempfile

import click
from datacontract.data_contract import DataContract

log = logging.getLogger(name="").getChild(suffix=__name__)


SEND_TO_KAFKA_TXT: str = """

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer
from confluent_kafka.serialization import MessageField, SerializationContext
from google.protobuf.message import Message

class KafkaProducer:
    def __init__(
        self,
        username: str,
        password: str,
        bootstrap_servers: str = broker,
        schema_registry_url: str = schema_registry,
        client_id: str = "datacontract-python-producer",
    ):
        self.producer = Producer(
            {
                "bootstrap.servers": bootstrap_servers,
                'security.protocol': 'SASL_PLAINTEXT',
                'sasl.mechanisms': 'PLAIN',
                'sasl.username': username,
                'sasl.password': password,
                "client.id": client_id,
            }
        )

        self.schema_registry_client = SchemaRegistryClient(
            conf={"url": schema_registry_url}
        )
        self.serializers_cache = {}

    def _get_serializer(self, proto_message_type):
        if proto_message_type not in self.serializers_cache:
            self.serializers_cache[proto_message_type] = ProtobufSerializer(
                msg_type=proto_message_type,
                schema_registry_client=self.schema_registry_client,
            )
        return self.serializers_cache[proto_message_type]

    def send_to_kafka(
        self,
        proto_message: Message,
        topic: str = topic,
        key=None):
        serializer = self._get_serializer(proto_message.__class__)

        value = serializer(
            message=proto_message,
            ctx=SerializationContext(topic=topic, field=MessageField.VALUE),
        )
        

        self.producer.produce(
            topic=topic,
            key=key,
            value=value,
        )

    def flush(self, timeout=5.0):
        self.producer.flush(timeout=timeout)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()



"""


class WheelBuilder:

    def build_wheel(
        self,
        # proto_file_name: str = "vertica_datacontract_pb2",
        filename: str,  # = "vertica_datacontract",
        version: str,  # = "0.1.8",
    ):
        proto_file_name: str = f"{filename}_pb2"
        module_folder: str = filename

        # VERSION: str = "0.1.8"

        # MODULE_NAME: str = "vertica-datacontract-tool"
        # MODULE_NAME: str = "vertica_datacontract_tool"

        # у нас должен быть файл proto.py:
        # PROTO_FILE_NAME: str = "vertica_datacontract_pb2"

        # MODULE_FOLDER: str = "vertica_datacontract"

        # pyproject_toml_content: str = """
        # [build-system]
        # requires = ["setuptools", "wheel"]
        # build-backend = "setuptools.build_meta"
        # """

        setup_file_content: str = f"""
from setuptools import setup, find_packages

setup(
    name="{module_folder}",
    version="{version}",# my_package.__version__,
    # author=my_package.__author__,
    packages=find_packages(),
    install_requires=[
        "protobuf>=3.20.0",
        "build>=1.3.0",
        "confluent-kafka[all]>=2.11.1",
        "pip>=25.2",
        ],

)
"""

        with tempfile.TemporaryDirectory() as tmpdirname:
            setup_file: str = os.path.join(tmpdirname, "setup.py")

            with open(file=setup_file, mode="w") as f:
                f.write(setup_file_content)

            module_folder_path: str = os.path.join(tmpdirname, module_folder)
            os.makedirs(name=module_folder_path)  # , exist_ok=True)

            init_file: str = os.path.join(module_folder_path, "__init__.py")

            data_contract: DataContract = self._get_data_contract(filename=filename)
            with open(file=f"{proto_file_name}.py", mode="r") as proto1:
                with open(file=init_file, mode="w") as f:
                    f.write(proto1.read())
                    f.write("\n\n")

                    f.write("\n".join(self._get_tags(data_contract=data_contract)))
                    f.write("\n\n")
                    f.write(
                        "\n".join(
                            f'{key} = "{value}"'
                            for key, value in self._get_urls(
                                data_contract=data_contract
                            ).items()
                        )
                    )
                    f.write("\n\n")
                    f.write(SEND_TO_KAFKA_TXT)


            subprocess.run(
                args=["python", "setup.py", "bdist_wheel"],
                check=True,
                cwd=tmpdirname,  # указать working directory
            )

            dist_folder: str = os.path.join(tmpdirname, "dist")
            wheels: list[str] = [
                os.path.join(dist_folder, filepath)
                for filepath in os.listdir(path=dist_folder)
            ]
            click.echo(message={"wheels": wheels})

            for wheel in wheels:
                subprocess.run(
                    args=["python", "-m", "pip", "install", wheel],
                    check=True,
                    cwd=tmpdirname,  # указать working directory
                )

            real_dir: str = os.getcwd()
            for wheel in wheels:
                click.echo(message=f"try copy2 {wheel}")
                shutil.copy2(src=wheel, dst=real_dir)

    def _get_data_contract(self, filename: str) -> DataContract:
        if not os.path.exists(path=f"{filename}.yaml"):
            raise FileNotFoundError(f"Data contract file not found: {filename}.yaml")

        data_contract: DataContract = DataContract(
            data_contract_file=f"{filename}.yaml"
        )
        data_contract.lint()
        return data_contract

    def _get_tags(self, data_contract: DataContract) -> list[str]:
        return data_contract.get_data_contract_specification().tags

    def _get_urls(self, data_contract: DataContract) -> dict:
        return {
            key: value.replace("kafka://", "") if key == "broker" else value
            for key, value in data_contract.get_data_contract_specification().links.items()
        }
        # data_contract.get_data_contract_specification().links["schema_registry"]
        # data_contract.get_data_contract_specification().links["broker"]
