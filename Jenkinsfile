pipeline {
    agent any
    stages {
        stage('Check style') {
            steps {
                sh(
                    script: """
                        docker run --rm -v $WORKSPACE/python_example_api/app.py:/apps/app.py alpine/flake8 app.py
                    """
                )
            }
        }
        stage('Run unit test'){
            steps {
                sh(
                    script: """
                        docker build -f Dockerfile.unit_test -t unit_test .
                        docker run --rm --name unit_test unit_test
                    """
                )
            }
        }
        stage('Build image'){
            steps {
                sh(
                    script: """
                        docker build -f Dockerfile -t examplecsd/example:latest .
                    """
                )
            }
        }
        stage('Push image to dockerhub'){
            steps {
                sh(
                    script: """
                        docker login -u "examplecsd" -p "123456789" docker.io
                        docker push examplecsd/example:latest
                    """
                )
            }
        }
        stage('Start application from image'){
            steps {
                sh(
                    script: """
                        docker pull examplecsd/example:latest
                        docker run -d --name python_example_latest -p "5000:5000/tcp" examplecsd/example:latest
                    """
                )
            }
        }
    }
}
