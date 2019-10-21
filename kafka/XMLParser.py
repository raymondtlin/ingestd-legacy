
import os

from xml.etree import cElementTree as ETree
from pathlib import Path


tree = ETree()
# get an iterable
context = iterparse(source, events=("start", "end"))

is_first = True

for event, elem in context:
    # get the root element
    if is_first:
        root = elm
        is_first = False
    if event == "end" and elem.tag == "record":
        ... process record elements ...
        root.clear()