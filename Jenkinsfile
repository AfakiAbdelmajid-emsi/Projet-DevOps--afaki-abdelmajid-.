pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Setup Python & venv') {
            steps {
                sh '''
                set -e
                apt-get update
                apt-get install -y python3 python3-venv python3-pip

                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
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
