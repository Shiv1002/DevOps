pipeline {
    agent any

    environment {
        GIT_REPO = "https://github.com/Shiv1002/DevOps.git"
        DOCKER_IMAGE = "node:latest"
        CONTAINER_NAME = "my-container"
        PUBLISH_DIR = "/var/www/html"
    }

    stages {
        stage('Clone Git repository') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }

        stage('Build and deploy HTML files') {
            agent {
                docker { image "${DOCKER_IMAGE}" }
            }
            steps {
                sh "cp ${WORKSPACE}/package.json ."
                sh "npm install" // Add this line
                sh "npm run build"
                sh "docker run -d --name ${CONTAINER_NAME} -p 80:80 -v ${PWD}/${PUBLISH_DIR}:${PUBLISH_DIR} ${DOCKER_IMAGE}"
            }
        }

        stage('Publish site') {
            steps {
                sh "curl --fail http://localhost/index.html"
                sh "curl -X PURGE http://localhost/index.html"
            }
        }
    }

}
