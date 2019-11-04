from pathlib import Path
from confluent_kafka import avro
from ingestd.kafka.finwire import utils
from os import getcwd


class FinWire:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def consume(self):
        AvroConsumer(**self.kwargs).consume()

    def produce(self):
        RawProducer(**self.kwargs).produce()



root_dir = Path(getcwd())
schema_dir = root_dir / "schema_registry" / "schemas"

field_widths = {"SEC": (15, 3, 15, 6, 4, 70, 6, 13, 8, 8, 12),
                "FIN": (15, 3, 4, 1, 8, 8, 17, 17, 12, 12, 12, 17, 17, 17, 26, 150),
                "CMP": (15, 3, 60, 10, 4, 2, 4, 8, 80, 80, 12, 25, 20, 24, 46, 150)}

