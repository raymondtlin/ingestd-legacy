from itertools import zip_longest, accumulate
from re import findall
from confluent_kafka import Message
from schema_registry import Schema

def create_parser(fieldwidths):

    # https://stackoverflow.com/a/4915359
    """
    Constructs a tuple of fieldwidths to parse fixedwidth records
    :param fieldwidths: 
    :return: 
    """
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldwidths))
    pads = tuple(fw < 0 for fw in fieldwidths)
    flds = tuple(zip_longest(pads, (0,) + cuts, cuts))[:-1]
    parse = lambda line: tuple(line[i: j] for pad, i, j in flds if not pad)
    
    parse.size = sum(abs(fw) for fw in fieldwidths)
    parse.fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)

    return parse


field_widths = {"SEC": (15, 3, 15, 6, 4, 70, 6, 13, 8, 8, 12),
                "FIN": (15, 3, 4, 1, 8, 8, 17, 17, 12, 12, 12, 17, 17, 17, 13, 23),
                "CMP": (15, 3, 60, 10, 4, 2, 4, 8, 80, 80, 12, 25, 20, 24, 46, 150)}

# create separate parser objects by doc_type
cmp, sec, fin = map(lambda x: create_parser(fieldwidths=field_widths.get(x)), ['CMP', 'SEC', 'FIN'])

#sec = pts, rectype, symbol, issuetype, status, name, exid, shout, firsttradedate, firsttradeexchg, dividend, conameorcik
#cmp = pts, rectype, name, cik, status, industryId, spRating, FoundingDate, addr1,addr2, postalcode,city,stateprovince,country,ceo,desc


