pipeline {
    agent any
    environment {
    PATH = "C:/Program Files/Git/bin:$PATH"
    }

    stages {
        stage ('Verify stage') {
            steps {
                withMaven(maven : 'maven3') {
                    powershell 'mvn verify -f C:/Users/tavin/Documents/Sideproject/Practice'
                }
            }
        }

        stage ('Testing stage') {

            steps {
                withMaven(maven : 'maven3') {
                    powershell 'mvn test -f C:/Users/tavin/Documents/Sideproject/Practice'
                }
            }
        }

        stage ('Validate stage') {

            steps {
                withMaven(maven : 'maven3') {
                    powershell 'mvn validate -f C:/Users/tavin/Documents/Sideproject/Practice'
                }
            }
        }
    }
}