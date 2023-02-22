#!/bin/bash    
hadoop fs -rm -f -r /input
hadoop fs -rm -f -r /output
hadoop fs -mkdir /input
hadoop fs -copyFromLocal ./M.txt /input/M.txt
hadoop fs -copyFromLocal ./N.txt /input/N.txt
hadoop fs -copyFromLocal ./X.txt /input/X.txt

hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./mapper.py \
-mapper "./mapper.py 2 3 3 2 2 2" \
-file ./reducer.py \
-reducer ./reducer.py \
-input /input \
-output /output