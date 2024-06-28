pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bakosabir99/simple-web-app.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t bakosabir99/simple-web-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run bakosabir99/simple-web-app pytest'
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        bat 'docker push bakosabir99/simple-web-app'
                    }
                }
            }
        }
    }
}
