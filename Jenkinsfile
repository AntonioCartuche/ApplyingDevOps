pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    if [ ! -d "env" ]; then
                        python3 -m venv env
                    fi
                    source env/bin/activate
                    pip install -r /home/azureuser/proyecto/ProyectFinalDBP/requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    source env/bin/activate
                    python /home/azureuser/proyecto/ProyectFinalDBP/manage.py test
                '''
            }
        }
        stage('Deploy') {
            steps {
                sshagent(['67ab364c-f4d6-4868-8c56-635f95ee3703']) {
                    sh '''
                        # Copiar archivos a la máquina virtual
                        scp -r ./ azureuser@52.254.16.255:/home/azureuser/proyecto
                        # Ejecutar comandos en la VM a través de SSH
                        ssh azureuser@52.254.16.255 <<EOF
                            cd /home/azureuser/proyecto/ProyectFinalDBP
                            # Activar el entorno virtual (ruta corregida)
                            source /home/azureuser/proyecto/env/bin/activate
                            # Instalar las dependencias
                            pip install -r /home/azureuser/proyecto/ProyectFinalDBP/requirements.txt
                            # Ejecutar migraciones
                            python /home/azureuser/proyecto/ProyectFinalDBP/manage.py migrate
                            # Iniciar gunicorn
                            nohup gunicorn ProyectFinalDBP.wsgi:application --bind 0.0.0.0:8000 &
                        EOF
                    '''
                }
            }   
        }
    }
}
