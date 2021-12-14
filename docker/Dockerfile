FROM openjdk:8-jdk-alpine
COPY docker/image_content/practice.jar /tmp/practice.jar
COPY python/server2.py /tmp/server2.py
RUN apk add python3
RUN chmod +x /tmp/server2.py
ENTRYPOINT ["java","-jar","-Dserver.port=8083","/tmp/practice.jar"]
CMD ["nohup","python3","/tmp/server2.py","2>","/dev/null","&"]