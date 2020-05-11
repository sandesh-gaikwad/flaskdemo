node {
	def app
	stage('Docker Buile'){
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
  #sh "docker inspect -f {{.NetworkSettings.IPAddress}} ${container.id} > host.ip"
  #readFile('host.ip').trim()
  sh "docker inspect -f  ${container.id}"
}
