pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Ahora, los pasos de construcción se realizan en la máquina virtual
                sshagent(['67ab364c-f4d6-4868-8c56-635f95ee3703']) {
                    sh '''
                        # Conectamos a la máquina virtual y realizamos la construcción
                        ssh azureuser@52.254.16.255 <<EOF
                            cd /home/azureuser/proyecto/ProyectFinalDBP
                            
                            # Comprobamos si el entorno virtual no existe y lo creamos
                            if [ ! -d "env" ]; then
                                python3 -m venv env
                            fi

                            # Activamos el entorno virtual y luego instalamos las dependencias
                            source env/bin/activate
                            pip install -r /home/azureuser/proyecto/ProyectFinalDBP/requirements.txt
                        EOF
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // También se ejecutan los tests en la máquina virtual
                sshagent(['67ab364c-f4d6-4868-8c56-635f95ee3703']) {
                    sh '''
                        ssh azureuser@52.254.16.255 <<EOF
                            cd /home/azureuser/proyecto/ProyectFinalDBP
                            
                            # Activamos el entorno virtual
                            source env/bin/activate
                            
                            # Ejecutamos las pruebas
                            python /home/azureuser/proyecto/ProyectFinalDBP/manage.py test
                        EOF
                    '''
                }
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
                            # Activar el entorno virtual
                            source /home/azureuser/proyecto/env/bin/activate
                            
                            # Instalar las dependencias (si no se instalaron previamente)
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
