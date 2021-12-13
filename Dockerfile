FROM openjdk:8-jdk-alpine
COPY ../../../target/practice.jar /tmp/practice.jar
ENTRYPOINT ["java","-jar","-Dserver.port=8083","/tmp/practice.jar"]