pipeline {
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
        stage('Build Docker image') {
            steps {
                // Build Docker image
                script {
                    docker.build('assignment1:latest')
                }
            }
        }
        stage('Push Docker image to Docker Hub') {
            steps {
                // Push Docker image to Docker Hub
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerHubCredentials') {
                        docker.image('assignment1:latest').push()
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
