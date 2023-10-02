pipeline {
    agent {
        docker { image 'node' }
        node { label 'windowsAgent' }
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
