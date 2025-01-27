pipeline {
    agent any
    environment {
        VIRTUAL_ENV = '"C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env"'
        DJANGO_SETTINGS_MODULE = 'ProyectFinalDBP.settings'
        DJANGO_PORT = '8000'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo No requirements.txt found, skipping dependency installation
                    )
                '''
            }
        }
        stage('Dependency Analysis') {
            steps {
                echo 'Checking for vulnerabilities in dependencies...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    pip install safety
                    safety check -r requirements.txt
                '''
            }
        }
        stage('Static Code Analysis') {
            steps {
                echo 'Analyzing code for security vulnerabilities...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    pip install bandit

                    try {
                        'bandit -r . --exclude env'
                    } catch (Exception e) {
                        echo 'Bandit encontró problemas, pero continuamos con el pipeline.'
                    }
                   
                    
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
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
                    call %VIRTUAL_ENV%\\Scripts\\activate.bat
                    if exist manage.py (
                        python manage.py migrate
                        python manage.py runserver 0.0.0.0:%DJANGO_PORT%
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
            echo 'Pipeline executed successfully! Access your application at http://localhost:8080/:%DJANGO_PORT%'
        }
        failure {
            echo 'Pipeline failed, check the logs for more details.'
        }
    }
}
