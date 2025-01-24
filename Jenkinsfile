pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    source env/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    source env/bin/activate
                    python manage.py test
                '''
            }
        }
        stage('Deploy') {
            steps {
                sshagent(['67ab364c-f4d6-4868-8c56-635f95ee3703']) {
                    sh '''
                        scp -r ./ azureuser@52.254.16.255:/home/azureuser/proyecto/ProyectFinalDBP/
                        ssh azureuser@52.254.16.255 <<EOF
                            cd /home/azureuser/proyecto/ProyectFinalDBP
                            source env/bin/activate
                            python manage.py migrate
                            sudo systemctl restart gunicorn
                        EOF
                    '''
                }
            }
        }
    }
}
