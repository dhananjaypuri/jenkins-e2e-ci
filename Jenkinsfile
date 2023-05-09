pipeline {
    agent any
    stages {
        stage('Code Checkout'){

            steps{
                echo "This is code checkout stage"
                git 'https://github.com/dhananjaypuri/jenkins-e2e-ci.git'
                sh 'ls'
            }
            
        }

        stage('Image Build Stage'){

            environment {
                IMG_NAME = "dhananjaypuri/jenkins-python-ec2"
            }

            steps{
                echo "This is image build stage"
                sh 'echo ${IMG_NAME}'
            }
            
        }

        stage('Image Push Stage'){

            steps{
                echo "This is image push stage"
            }
            
        }

        stage('Push Code to K8 manifest repo'){
            
            steps{
                echo "This is last stage"
            }
        }
    }
}
