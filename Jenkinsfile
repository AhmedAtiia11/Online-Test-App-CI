pipeline {
    agent any
    environment {
        DOCKER_HUB_USER_NAME="ahmedatiia11"
        REACT_IMAGE_NAME = "${DOCKER_HUB_USER_NAME}/react-nginx-img"
        DJANGO_IMAGE_NAME = "${DOCKER_HUB_USER_NAME}/django_app"
    }

    stages {
      //Cloning CI Repo to git the last version of the code
      stage('Clone repository') {  
        steps {
        checkout scm
    }
      }
      // Build  React Dockerfile and Rename it with the Dockerhub-reg Account name and Add the commmit number as tag name 
      stage('Test and Build React Image') {
         steps {       
         script {  
                    env.GIT_COMMIT_REV = sh (script: 'git log -n 1 --pretty=format:"%h"', returnStdout: true)
                    sh '''
                          cd ./frontend
                          docker build -t ${REACT_IMAGE_NAME}:${GIT_COMMIT_REV} .
                       '''   
                  }
              }                           
     }
      // Build  Django Dockerfile and Rename it with the Dockerhub-reg Account name and Add the commmit number as tag name 
      stage('Test and Build Django Image') {
         steps {       
         script {  
                    env.GIT_COMMIT_REV = sh (script: 'git log -n 1 --pretty=format:"%h"', returnStdout: true)
                    sh '''
                          cd ./backend
                          docker build -t ${DJANGO_IMAGE_NAME}:${GIT_COMMIT_REV} .
                       '''   
                  }
              }                           
     }

     // push Docker Images to the registry with the modified name 
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', "docker-cred" ) {
            sh 'docker push ${REACT_IMAGE_NAME}:${GIT_COMMIT_REV}'
            sh 'docker push ${DJANGO_IMAGE_NAME}:${GIT_COMMIT_REV}'
          }
        }
      }
    }

        
    // Trigger  the CD job at Jenkins
        stage('Trigger CD job ') {
                steps {
                echo "triggering CD"
                build job: 'Connection-Test-App-CD', parameters: [string(name: 'GIT_COMMIT_REV', value: env.GIT_COMMIT_REV)]
        }
        }      
  }

}
