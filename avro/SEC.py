import argparse
from uuid import uuid4

from confluent_kafka import avro

# cik = central index key
# accession-number = unique identifier assigned automatically to an acccepted EDGAR submission
#   generally in the format (CIK-YR-ROWID), rowid is the number of sequential filings year to date by CIK entity


record_schema = avro.loads("""{\
        "namespace": "ingestd",\
        "name": "request",\
        "type": "record",\
        "fields": [\
            {"name":"ip", "type":"string"},\
            {"name":"date", "type":"int"},\
            {"name":"time", "type":"long"},\
            {"name":"zone", "type":"string"},\
            {"name":"cik", "type":"string"},\
            {"name":"accession", "type":"string"},\
            {"name":"extension", "type":"string"},\
            {"name":"code", "type":"int"},\
            {"name":"size", "type":"long"},\
            {"name":"idx", "type":"int"},\
            {"name":"norefer", "type":"int"},\
            {"name":"noagent","type":"int"},\
            {"name":"find","type":"int"},\
            {"name":"crawler","type":"int"},\
            {"name":"browser","type":"string"}\
        ]\
    }\
""")

csv_schema = avro.loads("""{"namespace":"ingestd",\
        "name":"csv",\
        "type":"record",\
        "fields": [\
            {"name":"header","type":"string"},\
            {"name":"record","type":"string"}\
        ]\
    }\
""")

class Request(object):
    """
        Container for deserialized request Avro record
    """

    __slots__ = ["ip","date","time","zone","cik","accession","extension","code",
                 "size","idx","norefer","noagent","find","crawler","browser"]

    def __init__(self, ip, date, time, zone, cik, accession, extension, code,
                 size, idx, norefer, noagent, find, crawler, browser):
        self.ip = ip or None
        self.date = date or None
        self.time = time or None
        self.zone = zone or None
        self.cik = cik or None
        self.accession  = accession or None
        self.extension = extension or None
        self.code = code or None
        self.size = size or None
        self.idx = idx or None
        self.norefer = norefer or None
        self.noagent = noagent or None
        self.find = find or None
        self.crawler = crawler or None
        self.browser = browser or None
        self.id = uuid4()

    def to_dict(self):
        """
            Since Avro python library does not support code gen, we must provide a dict of our class for serialization
        """

        return {
            "ip": self.ip,
            "date": self.date,
            "time": self.time,
            "zone": self.zone,
            "cik": self.cik,
            "accession": self.accession,
            "extension": self.extension,
            "code": self.code,
            "size": self.size,
            "idx": self.idx,
            "norefer": self.norefer,
            "noagent": self.noagent,
            "find": self.find,
            "crawler": self.crawler,
            "browser": self.browser,
        }