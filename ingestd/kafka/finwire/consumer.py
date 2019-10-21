import json
import os
import uuid

import structlog
from confluent_kafka_helpers.consumer import AvroLazyConsumer
from confluent_kafka_helpers.loader import AvroMessageLoader
from ingestd.kafka.finwire import utils
from itertools import zip_longest, accumulate


class ParsingConsumer(AvroLazyConsumer):

    def __init__(self, **kwargs) -> None:

        self.config = utils.retrieve(kwargs['--path_to_config'], kwargs['--section'])
        self._topic_name = kwargs['--topic']
        self._num_partitions = kwargs['--partitions']
        self._consumer_group_id = kwargs['--group']
        self._key = kwargs['--key']
        self._exit = kwargs['--exit']
        self.loader_config = kwargs['--loader_config']

        self.consumer = AvroLazyConsumer(self.config)
        self.consumer.subscribe(self._topic_name)

    def consume(self):
        with self.consumer as consumer:
            for message in consumer:
                if message.key() is not None:
                    deserialized_key = self.decode_message()