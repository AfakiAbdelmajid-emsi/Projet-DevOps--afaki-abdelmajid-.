pipeline {
    agent any

    stages {

        stage('Install Python & dependencies') {
            steps {
                sh '''
                python3 --version || true
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                python3 -m pytest
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
