pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                python -m pytest
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.py, requirements.txt, pytest.ini', fingerprint: true
            }
        }
    }
}
