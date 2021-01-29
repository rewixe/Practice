FROM opensuse/leap
#FROM alpine
#WORKDIR /root/helloworld
COPY helloworld/HelloWorld.java /root/helloworld
COPY scripts/keepAlive.bash /tmp/keepAlive.bash

RUN zypper install -y java-1_8_0-openjdk \
    jdk-8u66-linux-x64 && \
    zypper clean -a

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

RUN javac HelloWorld.java

ENTRYPOINT java HelloWorld