pipeline {
	agent any
	stages {
		stage("test PythonEnv") {
			steps{
				sh 'pip install pytest'
				sh 'pytest test.py'
			}
		}
	}
}
