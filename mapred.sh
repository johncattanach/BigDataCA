#!/bin/sh
# run hadoop map reduce
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file ./map-bag.py -mapper ./map-bag.py -file ./reduce-bag.py -reducer ./reduce-bag.py -input /twitter/twitter_MBTI.csv -output /twitter/out
