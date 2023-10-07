pipeline {
    agent {
        // node { label 'windowsAgent' }
        dockerfile true
    }
    stages {
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
