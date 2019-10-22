pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat(script: '''cd CBoard
mvn clean compile''', label: 'build-compile')
      }
    }
    stage('test') {
      steps {
        bat(script: '''cd junipro
mvn clean test''', label: 'test-xunit')
      }
    }
  }
}