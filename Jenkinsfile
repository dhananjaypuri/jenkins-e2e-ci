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
            environment {
                IMG_NAME = "jenkins-python-ec2"
                NEW_IMG_NAME = "${IMG_NAME}:${BUILD_ID}"
                NEW_REPO_NAME = "argocd-k8-manifest"
            }
            steps{
                withCredentials([usernamePassword(credentialsId: 'git_cred', passwordVariable: 'GIT_PASSWD', usernameVariable: 'USER_NAME')]) {
                    sh '''
                    git config --global user.email "dhananjay.puri@gmail.com"
                    git config --global user.name "dhananjaypuri"
                    echo "${NEW_IMG_NAME}"
                    sed -i "s/jenkins-python-ec2.*/${NEW_IMG_NAME}/g" manifests/deploy.yml
                    cat manifests/deploy.yml
                    git add manifests/deploy.yml
                    git commit -m "Updating K8 manifest file with build : ${BUILD_ID}"
                    git push https://${GIT_PASSWD}@github.com/${USER_NAME}/${NEW_REPO_NAME}.git HEAD:master
                    '''
                }
                echo "This is last stage"
            }
        }
    }
}
