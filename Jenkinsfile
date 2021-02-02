pipeline {
    agent any

    stages {
        stage ('Compile stage') {

            steps {
                withMaven(maven : 'maven_3_5_4') {
                    sh 'mvn verify'
                }
            }
        }

        stage ('Testing stage') {

            steps {
                withMaven(maven : 'maven_3_5_4') {
                    sh 'mvn test'
                }
            }
        }

        stage ('Deploy stage') {

                    steps {
                        withMaven(maven : 'maven_3_5_4') {
                            sh 'mvn clean'
                        }
                    }
                }
    }
}