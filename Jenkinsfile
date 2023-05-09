pipeline {
    agent any
    stages {
        stage('Code Checkout'){

            steps{
                echo "This is code checkout stage"
                git branch: 'master', url: 'https://github.com/dhananjaypuri/jenkins-e2e-ci.git' 
                sh 'ls'
            }
            
        }

        stage('Image Build Stage'){

            steps{
                echo "This is image build stage"
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
