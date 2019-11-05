from __future__ import absolute_import

from itertools import zip_longest, accumulate
from re import compile, findall

from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def retrieve(file_path, section) -> dict:
    """
    Returns dict with configuration parameters.
    :param file_path: string
    :param section: string
    :return: dict
    """

    with open(file_path, 'r') as f:
        config = load(f, Loader)

        try:
            return config.get(section)
        except KeyError as e:
            print('Section: {} in the conf as a key.'.format(section), e)


def ackback(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}, Error: {1}".format(msg.value(), err.str()))
    else:
        print("Produced record to topic {0} partition [{1}] @ offset {2}"
              .format(msg.topic(), msg.partition(), msg.offset()))


def find_type(record: str) -> str:
    """
    Searches for the 3 character document type in the record
    :param: a read-line
    :return: three character token from the set (SEC,CMP,FIN)
    """
    token = compile(r'(SEC|CMP|FIN)')

    # return first match only
    matched_type = findall(token, record)[0]

    if matched_type in ['SEC', 'CMP', 'FIN']:
        return matched_type
    else:
        print('Invalid return value from find_type method.')
        raise ValueError