pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Calculator') {
            steps {
                sh '''
                . venv/bin/activate
                python calculator.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m pytest
                '''
            }
        }
    }
}
