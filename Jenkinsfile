pipeline {
	agent any
	stages {
		stage('clone repository') {
			script {
				git credentialsId: 'jenkins-user-github', url: 'https://github.com/SoyTiyi/pytest_jenkins.git', branch: 'master'
			}
		}
		stage("test PythonEnv") {
			withPythonEnv('python3') {
				sh 'pip install pytest'
				sh 'pytest mytest.py'
			}
		}
	}
}
