from __future__ import absolute_import

from itertools import zip_longest, accumulate
from re import compile, findall

from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def retrieve(file_path: str, section: str) -> dict:
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
            print('Section: {} in the configuration as a key.'.format(section), e)


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


def stream_flatfile(fpath: str):
    """
    Creates a filesystem handle on a local file.  Generates a list of fields.
    :param fpath: string
    :return:
    """
    with open(fpath, 'r') as handle:
        yield handle.read()


def generate_payload(fpath: str, field_widths: dict):
    """
    Opens a fs handle to specified path.  Reads each line in the flatfile.
    Determines type of record.
    Parses fixed width values according to record type.
    :param fpath: string
    :param field_widths: dict
    :return: yields record token, and parsed record
    """
    try:
        for line in stream_flatfile(fpath):
            p = create_parser(field_widths.get(find_type(line)))(line)
            yield (find_type(line), p)
    except BaseException as e:
        print("Exception in generate_payload execution: {0}".format(e), e.args)

def create_parser(fieldWidths: tuple):
    # https://stackoverflow.com/a/4915359
    """
    Constructs a tuple of fieldwidths to parse fixed-width records
    :param: fieldwidths: tuple of field-lengths + pad-lengths to split line by
    :return: parsed line as List[string]
    """
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldWidths))
    pads = tuple(fw < 0 for fw in fieldWidths)
    flds = tuple(zip_longest(pads, (0,) + cuts, cuts))[:-1]

    return lambda line: tuple(line[i: j] for pad, i, j in flds if not pad)