pipeline {
    agent any

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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-id', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat """
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                        docker push bakosabir99/simple-web-app
                    """
                }
            }
        }
    }
}
