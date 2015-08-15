#!/bin/python

from pymarc import MARCReader
import sys

if sys.argv[1]:
   file_name = sys.argv[1]
else:
   file_name = 'export.biblio.UTF-8.USMARC'

with open(file_name, 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        delete_this_one = True
        for f in record.get_fields('852'):
           print f
           if ('LBCC' in str(f)) and ('DEFAULT' in str(f)):
               delete_this_one = False
        if delete_this_one:
           record.leader = record.leader[:5] + 'd' + record.leader[6:]
    print record.leader
