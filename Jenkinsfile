node {
	def app
	checkout scm
	stage('Docker Build'){
		app = docker.build('python-flaskapp')
	}
	stage ('Test App'){
	docker.image('python-flaskapp').withRun { c-> 
		def ip = hostIp(c)
		docker.image('python-flaskapp').inside {
			sh "echo ${ip}"
			sh "python3 tests/testapp.py"
		}
	   }
	}
}

def hostIp(container) {
 	sh "docker inspect -f {{.NetworkSettings.IPAddress}} ${container.id} > host.ip"	
	readFile('host.ip').trim()
}
