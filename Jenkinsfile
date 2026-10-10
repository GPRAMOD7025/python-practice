pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Ruff Check') {
            steps {
                bat 'python -m pip install ruff'
                bat 'python -m ruff check .'
            }
        }

        stage('Unit Tests') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python hello.py'
            }
        }
    }
}
