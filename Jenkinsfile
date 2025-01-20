pipeline {
    agent any
    environment {
        // Ruta del entorno virtual
        VIRTUAL_ENV = 'C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env'  // Asegúrate de que la ruta sea correcta
        DJANGO_SETTINGS_MODULE = 'ProyectFinalDBP.settings'  // Nombre de tu proyecto Django
    }
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat '''
                    call C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env\\Scripts\\activate.bat
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo No requirements.txt found, skipping dependency installation
                    )
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    call "C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env\\Scripts\\activate.bat"
                    python --version  
                    if exist manage.py (
                        python manage.py test 
                    ) else (
                        echo No manage.py found, skipping tests
                    )
                '''
            }
        }
        stage('Deploy Locally') {
            steps {
                echo 'Deploying locally...'
                bat '''
                    call "C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env\\Scripts\\activate.bat"
                    if exist manage.py (
                        python manage.py migrate  
                        python manage.py runserver 0.0.0.0:8000  
                    ) else (
                        echo No manage.py found, skipping deployment
                    )
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution complete!'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed, check the logs for more details.'
        }
    }
}
