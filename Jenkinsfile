pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                python --version
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
