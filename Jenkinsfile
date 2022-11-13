pipeline {
  environment {
    registry = 'oceus/eacode:initial'
    registryCredential = 'dockerhub_id'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git(url: 'https://github.com/Oceus/eacode.git', branch: 'main')
      }
    }
    stage('Building image') {
      steps{
        sh 'sudo docker build -t oceus/eacode:initial .'
      }
    }
    stage('Docker login') {
      steps{
        sh 'sudo docker login -u oceus -p H?XWy#R_LJ:q6;d'
      } 
    }
    stage('Deploy image') {
      steps{
        sh 'sudo docker push oceus/eacode:$BUILD_NUMBER'
      }
    }
    stage('Cleaning up') {
      steps{
        sh 'sudo docker rmi $registry:$BUILD_NUMBER'
      }
    }
  }
}
