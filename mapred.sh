#!/bin/sh
hadoop fs -rm /twitter/out/*
hadoop fs -rmdir /twitter/out
# run hadoop map reduce
#hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file ./map-bag.py -mapper ./map-bag.py -file ./reduce-bag.py -reducer ./reduce-bag.py -input /twitter/twitter_MBTI.csv -output /twitter/out
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -files map-bag.py,reduce-bag.py -mapper map-bag2.py -reducer reduce-bag3.py   -input /twitter/twitter_MBTI.csv -output /twitter/out
