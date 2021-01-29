#FROM opensuse/leap
FROM alpine
WORKDIR /root/helloworld
COPY helloworld/HelloWorld.java /root/helloworld

RUN apk add openjdk8

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

RUN javac HelloWorld.java

ENTRYPOINT java HelloWorld