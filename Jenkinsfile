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

                sh '''
                    ls -ltr
                    docker build -t ${IMG_NAME}:${BUILD_ID} .
                    docker image ls
                '''
            }
            
        }

        stage('Image Push Stage'){

            environment {
                DOCKER_CREDENTIALS = credentials('docker_cred')
                DOCKER_USER_NAME = "dhananjaypuri"
                IMG_NAME = "dhananjaypuri/jenkins-python-ec2"
            }

            steps
            {
                echo "This is image push stage"
                sh 'echo "${DOCKER_CREDENTIALS}" | docker login -u ${DOCKER_USER_NAME} --password-stdin'
                sh 'docker image push ${IMG_NAME}:${BUILD_ID}'
                sh '''
                    echo "Cleaning Up Images"
                    docker image rmi -f $(docker images | grep jenkins-python-ec2 | awk '{print $3}')
                '''
            }
            
        }

        stage('Checkout argocd-k8-manifest'){
            
            steps{
                echo "Getting code from GIT"
                git 'https://github.com/dhananjaypuri/argocd-k8-manifest.git'
                sh 'ls'
            }
        }

        stage('Push Code to K8 manifest repo'){
            
            steps{
                echo "This is last stage"
            }
        }
    }
}
