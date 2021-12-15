Basic setup:
UI: go to http://localhost:8083/rest/docker/hello (spring boot), http://localhost:8086/ (python)
Docker: docker build --no-cache -t spring-docker -f .\docker\Dockerfile . (main Dockerfile)
docker run -p 8085:8085 1da2b732347be6f6aa56631792981dd13305166031cfef5206f327d345a1e31e
Jenkins: install Jenkins, install maven plugins, add maven tool within Jenkins, create pipeline
K8s: install via docker desktop

Test project

Next steps:
3x Spring Boot tutorials
3x Java 8 tutorial/specifics/Add in complex java stuff
Add in more pipeline -> build spring package->copy into /x-> push to git->rebuild docker->start pods etc.
DevOps project videos
Dependencies/modules
Build snapshot -> copy into image -> Build image -> run image -> test?
Spinnaker setup
Helm setup
Simple interactive front end (button=>hello)
Postgres setup
Javascript front end
Create other Jenkins items
Add another microservice
Add simple js framework helloworld script, RUN in dockerfile
Create another branch, merge
Add simple python ML script
Allow UI to work on mobile
Create app
CSAR build?
AWS?
Use SLES image for pods

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
Java hello world
Docker setup with Java
Docker container keep running
Convert to SLES base image
Spring boot REST API setup
Add dockerfile to correct dir
Use Practice jar instead of helloworld (<build>)
Add git add-ons to Intellij
Spring testing setup (one test)
withMaven fix
fix Jenkins intellij plugin
Integrate Jenkins with Git SCM
Jenkins setup
Kubernetes pod setup
Create k8s folder
Create k8s spring-docker deployment
Python setup
Spinnaker (not compatible)
Refactor structure
Python cleanup
File cleanup
Startup/entrypoint script
