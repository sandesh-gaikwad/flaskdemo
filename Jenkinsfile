node {
	def app
	stage('Clone Repo'){
		checkout scm
	}
	
	stage('Docker Build'){
		app = docker.build('python/flaskapp')
	}
	def hostIp(container) {
  		sh "docker inspect -f {{.Node.Ip}} ${container.id} > hostIp"
  		readFile('hostIp').trim()
	}
	stage('Test') {
		docker.image('python/flaskapp').withRun('-p 5000:5000') { c->
			sh "curl http://${hostIP(c)}:5000/api/v1.0/task"
		}
	
	}
		
}
