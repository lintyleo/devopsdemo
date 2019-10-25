pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        dir(path: 'mvndemo') {
          bat(script: 'mvn clean compile', label: 'build-compile')
        }

      }
    }
    stage('test') {
      parallel {
        stage('test-xunit') {
          steps {
            dir(path: 'junitpro') {
              bat(script: 'mvn clean test', label: 'test-xunit')
            }

            dir(path: 'mvndemo') {
              bat(script: 'mvn test', label: 'xunit')
            }

          }
        }
        stage('test-xunit2') {
          steps {
            dir(path: 'junitpro') {
              bat(script: 'mvn test', label: 'xunit2')
            }

          }
        }
      }
    }
    stage('automate') {
      parallel {
        stage('automate-api') {
          steps {
            dir(path: 'hatapi/runner') {
              bat(script: 'run_seniverse_life_suggest_test.bat', label: 'automate2')
            }

          }
        }
        stage('automate-web') {
          steps {
            dir(path: 'hatweb/runner') {
              bat(script: 'run_zentao_login_test.bat', label: 'web')
            }

          }
        }
      }
    }
    stage('deploy') {
      steps {
        echo 'deploy mvndemo'
      }
    }
    stage('post') {
      steps {
        echo 'post'
      }
    }
  }
}