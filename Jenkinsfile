pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('clean') {
            steps {
                cleanWs()
            }
        }
        stage('Build') {
            steps {
                echo 'Building ..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing ..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying ..'
                
            }
        }
    }
}
