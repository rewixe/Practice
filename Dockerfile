FROM openjdk:8
COPY src/main/docker/image_content/keepAlive.bash /tmp/keepAlive.bash
COPY helloworld/target/helloworld.jar /tmp/helloworld.jar
COPY target/practice.jar /tmp/practice.jar
COPY helloworld/src/main/resources/application.properties /tmp/application.properties
COPY src/main/python/server.py /var/tmp/server.py
#RUN apt-get install python3.6
#RUN python /var/tmp/server.py
EXPOSE 8085 8086
#ENTRYPOINT ['tail', '-f', '/dev/null']
#ENTRYPOINT ["java","-jar","/tmp/practice.jar","--spring.config.location=file:/tmp/application.properties"]

#RUN zypper install -y java-1_8_0-openjdk-devel

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

#RUN javac /root/helloworld/HelloWorld.java

ENTRYPOINT ["/bin/bash","/tmp/keepAlive.bash"]