pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Main Script') {
            steps {
                sh 'echo Running main.py'
                sh 'python main.py'
            }
        }

        stage('Run PyTest') {
            steps {
                sh 'echo Running pytest'
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