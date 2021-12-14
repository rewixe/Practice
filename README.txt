Basic setup:
UI: go to http://localhost:8085/rest/docker/hello
Docker: docker build . (main Dockerfile)
docker run -p 8085:8085 1da2b732347be6f6aa56631792981dd13305166031cfef5206f327d345a1e31e
exec into container to start jar, java -jar x.jar
Jenkins: 

Test project

Next steps:
Build snapshot -> copy into image -> Build image -> run image -> test?
Spinnaker setup
CSAR build?
Helm setup
Simple interactive front end (button=>hello)
Postgres setup
Javascript front end
Create other Jenkins items
Use SLES image for pods
Add another microservice
Add simple js framework helloworld script, RUN in dockerfile
Create another branch, merge
Add simple python ML script
Allow UI to work on mobile
Create app
Java 8 specifics

Tech added:
Git
Intellij
Java
Docker
Spring
Jar
Testing
Jenkins
Kubernetes
Python

To be added:
Startup/entrypoint script
Python cleanup
File cleanup
Add in complex java stuff
Add in more pipeline -> build spring package->copy into /x-> push to git->rebuild docker->start pods etc.
DevOps project videos
Proper README explaining setup
Dependencies/modules
Helm
Postgres
Microservices
ML
Mobile
Javascript (React/Node/Angular/etc)
Git branching
CSAR
Pyunits

DONE
x	Java hello world										
x	Docker setup with Java
x	Docker container keep running
x	Convert to SLES base image
x	Spring boot REST API setup
x	Add dockerfile to correct dir
x	Use Practice jar instead of helloworld (<build>)
x	Add git add-ons to Intellij
x	Spring testing setup (one test)
x	withMaven fix
x	fix Jenkins intellij plugin
x	Integrate Jenkins with Git SCM
x	Jenkins setup
x	Kubernetes pod setup
x	Create k8s folder
x	Create k8s spring-docker deployment
x	Python setup
x	Spinnaker (not compatible)
Refactor structure