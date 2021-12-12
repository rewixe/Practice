pipeline {
    agent any
    environment {
    PATH = "C:/Program Files/Git/bin:$PATH"
    }

    stages {
        stage ('Verify stage') {
            steps {
                withMaven(maven : 'maven_3_8_4') {
                    powershell 'mvn verify -f C:/Users/PC/Documents/Sideproject/Practice'
                }
            }
        }

        stage ('Testing stage') {

            steps {
                withMaven(maven : 'maven_3_5_4') {
                    powershell 'mvn test -f C:/Users/PC/Documents/Sideproject/Practice'
                }
            }
        }

        stage ('Validate stage') {

            steps {
                withMaven(maven : 'maven_3_5_4') {
                    powershell 'mvn validate -f C:/Users/PC/Documents/Sideproject/Practice'
                }
            }
        }
    }
}