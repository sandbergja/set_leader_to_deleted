# set_leader_to_deleted
Sets LDR to deleted based on holdings data in the 852 tag (provided by Evergreen ILS)

This script was created to provide OCLC with a file of our current records and deleted records, with the deleted ones containing a "d" in character 5 of the ldr.  OCLC Batchload projects set and remove holdings based on character 5 of the leader field (i.e. whether or not a record has been deleted), but our library wanted to base deletion on our holdings, due to the shared bib records within our consortium.
