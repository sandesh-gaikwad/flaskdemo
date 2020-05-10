node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Buile'){
		app = docker.build('python/flaskapp')
	}
}
