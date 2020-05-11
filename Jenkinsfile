node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Build'){
		app = docker.build('python/flaskapp')
	}
	
	docker.image('python/flaskapp').inside { 			
		sh "python3 tests/testapp.py"
	}
}

