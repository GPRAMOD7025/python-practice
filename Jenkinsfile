pipeline {
    agent any
    triggers {
        pollSCM('H/2 * * * *')
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
