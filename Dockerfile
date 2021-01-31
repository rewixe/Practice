FROM openjdk
COPY /helloworld/target/helloworld.jar /tmp/helloworld.jar
EXPOSE 8085
ENTRYPOINT ["java","-jar","/tmp/helloworld.jar"]