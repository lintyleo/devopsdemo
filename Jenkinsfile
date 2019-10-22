pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        dir(path: 'CBoard') {
          bat(script: 'mvn clean compile', label: 'build-compile')
        }

      }
    }
    stage('test') {
      steps {
        dir(path: 'junitpro') {
          bat(script: 'mvn clean test', label: 'test-xunit')
        }

      }
    }
    stage('update') {
      steps {
        jiraComment(issueKey: 'SCRUM-3', body: 'kkk')
      }
    }
  }
}