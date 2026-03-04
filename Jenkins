pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Jainandan-728/Calculator.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
    }
}
