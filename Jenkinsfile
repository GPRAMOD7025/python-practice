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
    stages {
        stage('Run Python') {
            steps {
                bat 'python --version'
                bat 'python hello.py'
            }
        }
    }
}
