node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Build'){
		app = docker.build('python/flaskapp')
	}
	
	docker.image('python/flaskapp').inside { 			
		sh "curl http://127.0.0.1:5000/api/v1.0/task"
	}
}

