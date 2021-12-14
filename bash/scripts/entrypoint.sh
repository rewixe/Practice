#!/bin/sh
java -jar -Dserver.port=8083 /tmp/practice.jar > /dev/null &
nohup python3 /tmp/server2.py > /dev/null &

while true
do
  sleep 20
done