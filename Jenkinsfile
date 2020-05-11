node {
	def app
	checkout scm
	stage('Docker Build'){
		app = docker.build('python-flaskapp')
	}
	docker.image('python-flaskapp').withRun { c-> 
		def ip = hostIp(c)
		docker.image('python-flaskapp').inside {
			sh "echo ${ip}"
		}
	}
}

def hostIp(container) {
  
  sh "docker inspect -f  ${container.id}"
}
