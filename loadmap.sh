#!/bin/sh
# load hdfs file into hbase table
# do this first in hbase shell
hbase shell <<!
disable 'wordcount'
drop 'wordcount'
create 'wordcount',{NAME=>'cf'}
quit
!
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=HBASE_ROW_KEY,cf:doc_id,cf:label,cf:word,cf:count wordcount  /twitter/out/part-00000

