pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    python manage.py test
                '''
            }
        }
        stage('Deploy') {
            steps {
                sshagent(['67ab364c-f4d6-4868-8c56-635f95ee3703']) {
                    sh '''
                        scp -r ./ azureuser@52.254.16.255:/home/azureuser/proyecto
                        ssh azureuser@52.254.16.255 <<EOF
                            cd /home/azureuser/proyecto
                            source env/bin/activate
                            python manage.py migrate
                            nohup gunicorn ProyectFinalDBP.wsgi:application --bind 0.0.0.0:8000 &
                        EOF
                    '''
                }
            }
        }
    }
}
