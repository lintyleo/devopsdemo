pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat(script: 'cd CBoard', label: 'build-dir')
        bat(script: 'mvn clean compile', label: 'build-mvn')
      }
    }
    stage('test') {
      steps {
        bat(script: 'cd junitpro', label: 'test-dir')
        bat(script: 'mvn clean test', label: 'mvn-xunit')
      }
    }
  }
}