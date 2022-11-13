pipeline {
  environment {
    registry = "oceus/eacode:initial"
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
    stage('Deploy image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Cleaning up') {
      steps{
        sh "sudo docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
