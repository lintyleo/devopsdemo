pipeline {
  agent any
  stages {
    stage('build') {
      steps {
		dir('CBoard') {
			// some block
			bat(script: 'mvn clean compile', label: 'build-compile')
		}
      }
    }
    stage('test') {
      steps {
	    dir('junitpro') {
			// some block
			bat(script: 'mvn clean test', label: 'test-xunit')
		}
      }
    }
  }
}