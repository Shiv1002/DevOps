pipeline {
    agent any
    
    environment {
        NODE_IMAGE = "node:latest"
        NGINX_IMAGE = "nginx:latest"
        GIT_REPO = "https://github.com/Shiv1002/DevOps.git"
        HTML_FOLDER = "htmlFolder"
    }
    
    stages {
        stage("Build") {
            steps {
                // Checkout HTML files from Git repository
                git branch: 'main', url: env.GIT_REPO
                
                // Build Node container with HTML files
                sh "docker build -t node-html ."
            }
        }
        
        stage("Deploy") {
            steps {
                // Run Node container with HTML files
                sh "docker run -d --name node-html-container node-html"
                
                // Run Nginx container and mount HTML files from Node container
                sh "docker run -d --name nginx-container -p 80:80 --link node-html-container:node-html -v ${pwd()}/${env.HTML_FOLDER}:/usr/share/nginx/html ${env.NGINX_IMAGE}"

            }
        }
        
        stage("Test") {
            steps {
                // Test the HTML files by accessing the Nginx server
                sh "curl http://localhost"
            }
        }
    }
    
    post {
        always {
            // Clean up containers and images
            sh "docker rm -f node-html-container nginx-container"
            sh "docker rmi -f node-html ${env.NGINX_IMAGE}"
        }
    }
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Shiv1002/DevOps.git']], gitTool: 'gitInstall'])

}
