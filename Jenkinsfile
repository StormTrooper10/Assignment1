pipeline {
    environment {
        registry = "gulomer10/assignment1"
        registryCredential = 'dockerHubCredentials'
        dockerImage = ''
    }

    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/StormTrooper10/Assignment1.git'
            }
        }

        stage('Install dependencies') {
            steps {
                // Install dependencies using pip
                bat 'C:\\Users\\gulom\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Run tests using pytest
                bat 'C:\\Users\\gulom\\AppData\\Local\\Programs\\Python\\Python312\\python.exe test.py'

            }
        }


        stage('Building our image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        success {
            emailext (
                to: 'i200591@nu.edu.pk',
                subject: 'Jenkins Job Successful',
                body: 'The Jenkins job has been successfully executed.'
            )
        }
        failure {
            emailext (
                to: 'i200591@nu.edu.pk',
                subject: 'Jenkins Job Failed',
                body: 'The Jenkins job has failed. Please investigate.'
            )
        }
    }
}
