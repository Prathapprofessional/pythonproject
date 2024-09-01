pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'prathapprof/todo-api:latest'
        REGISTRY = 'docker.io' // Replace with your private registry URL if applicable
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Prathapprofessional/pythonproject.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run your tests
                    sh 'pytest'
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    // Login to Docker Registry (if private)
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin $REGISTRY'

                    // Push Docker image
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy to Kubernetes
                    sh 'kubectl set image deployment/todo-api-deployment todo-api=$DOCKER_IMAGE'
                }
            }
        }
    }
}
