pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myusername/todo-api:latest'
        REGISTRY = 'docker.io'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Prathapprofessional/pythonproject.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Push') {
            steps {
                bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin %REGISTRY%'
                bat 'docker push %DOCKER_IMAGE%'
            }
        }

        stage('Deploy') {
            steps {
                bat 'kubectl set image deployment/todo-api-deployment todo-api=%DOCKER_IMAGE%'
            }
        }
    }
}
