pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('bako_id')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bakosabir99/simple-web-app.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t bakosabr99/simple-web-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run bakosabr99/simple-web-app pytest'
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        bat 'docker push bakosabr99/simple-web-app'
                    }
                }
            }
        }
    }
}
