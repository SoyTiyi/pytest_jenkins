pipeline {
	agent any
	stages {
		stage("test PythonEnv") {
			withPythonEnv('python3') {
				sh 'pip install pytest'
				sh 'pytest test.py'
			}
		}
	}
}
