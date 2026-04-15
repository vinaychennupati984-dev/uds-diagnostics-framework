pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    parameters {
        choice(name: 'SERVICE_MODE', choices: ['read_did', 'write_did', 'session'], description: 'Select the UDS service to run')
        string(name: 'DID', defaultValue: '0xF190', description: 'DID value')
        string(name: 'DATA', defaultValue: '0xAA 0xBB', description: 'Data bytes for write_did only')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run UDS Command') {
            steps {
                script {
                    if (params.SERVICE_MODE == 'read_did') {
                        bat "python main.py --service read_did --did ${params.DID}"
                    } else if (params.SERVICE_MODE == 'write_did') {
                        bat "python main.py --service write_did --did ${params.DID} --data ${params.DATA}"
                    } else if (params.SERVICE_MODE == 'session') {
                        bat "python main.py --service session --did ${params.DID}"
                    } else {
                        error("Unsupported SERVICE_MODE: ${params.SERVICE_MODE}")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
    }
}