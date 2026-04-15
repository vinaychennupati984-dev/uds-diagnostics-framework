pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/vinaychennupati984-dev/uds-diagnostics-framework'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Main Script') {
            steps {
                sh 'python main.py'
            }
        }

        stage('Run PyTest') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}