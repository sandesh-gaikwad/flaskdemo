pipeline {
    agent any
    stages {
        stage('GitScm') {
            steps {}
                git credentialsId: 'github', url: 'https://github.com/sandesh-gaikwad/flaskdemo.git'
            }
        }
        stage('Builds') {
            steps {
                sh "pip3 install -r requirement.txt"
                sh "python3 app.py"
            }
        }
        stage('Test') {
            steps {
                sh "python testapp.py"
            }
        }
    }
