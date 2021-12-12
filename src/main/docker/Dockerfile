FROM opensuse/leap
COPY image_content/keepAlive.bash /tmp/keepAlive.bash

RUN zypper install -y java-1_8_0-openjdk-devel

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

RUN javac /root/helloworld/HelloWorld.java

ENTRYPOINT ["/bin/bash","/tmp/keepAlive.bash"]