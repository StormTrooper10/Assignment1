pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package' // Example Maven build command
            }
        }
        stage('Containerize') {
            steps {
                script {
                    docker.build('yourdockerhubusername/yourapp:latest')
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerHubCredentials') {
                        docker.image('yourdockerhubusername/yourapp:latest').push()
                    }
                }
            }
        }
    }
    
    post {
        success {
            emailext (
                to: 'admin@example.com',
                subject: 'Jenkins Job Successful',
                body: 'The Jenkins job has been successfully executed.'
            )
        }
    }
}
