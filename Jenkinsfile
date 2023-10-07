pipeline {
    agent none
    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }
    stages {
        stage('clean') {
             agent {
                    dockerfile true
            }
            steps {
                cleanWs()
            }
        }
        stage('Build') {
            agent {
                dockerfile true
            }
            steps {
                checkout scm
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
    post {
        // Clean after build
        always {
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true,
                    patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                               [pattern: '.propsfile', type: 'EXCLUDE']])
        }
    }
}
