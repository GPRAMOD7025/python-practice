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

    stage('Unit Tests & Coverage') {
        steps {
            bat 'python -m pip install coverage'
            bat 'python -m coverage run --source=hello -m unittest discover -s tests -v'
            bat 'python -m coverage report -m'
        }
    }

        stage('Run Python') {
            steps {
                bat 'python hello.py'
            }
        }
    }
}
