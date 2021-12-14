FROM openjdk:8-jdk-alpine
COPY docker/image_content/practice.jar /tmp/practice.jar
COPY python/server2.py /tmp/server2.py
COPY bash/scripts/entrypoint.sh /tmp/entrypoint.sh
COPY bash/scripts/keepAlive.sh /tmp/keepAlive.sh
RUN apk add python3
RUN chmod +x /tmp/server2.py
RUN chmod +x /tmp/entrypoint.sh
RUN chmod +x /tmp/keepAlive.sh
#ENTRYPOINT ["/tmp/keepAlive.sh"]
ENTRYPOINT ["/tmp/entrypoint.sh"]
#ENTRYPOINT ["java","-jar","-Dserver.port=8083","/tmp/practice.jar"]
#CMD ["nohup","python3","/tmp/server2.py","2>","/dev/null","&"]