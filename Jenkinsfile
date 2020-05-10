node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Buile'){
		app = docker.build('python/flaskapp')
	}
	
	stage('Test') {
		app.inside {
			echo "Test Passed"
			sh "python3 tests/testapp.py"
		}
	}
		
}
