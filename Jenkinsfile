node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Build'){
		app = docker.build('python/flaskapp')
	}
	
	stage('Test') {
		docker.image('python/flaskapp').withRun('-p 5000:5000') { c->
			sh "curl http://localhost:5000/api/v1.0/task"
		}
	
	}
		
}

