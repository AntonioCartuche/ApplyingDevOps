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
                    bandit -r . --exclude env --exit-zero
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

        /*
        stage('Dynamic Analysis - Nikto') {
            steps {
                echo 'Running dynamic security tests with Nikto...'
                bat '''
                    nikto -h http://localhost:8000
                '''
            }
        }
        */

        stage('Dynamic Tests with Playwright') {
            steps {
                echo 'Running dynamic tests with Playwright...'
                bat '''
                    npx playwright test
                '''
            }
        }


        stage('Deploy Locally') {
            steps {
                echo 'Activating virtual environment and deploying the application...'
                bat '''
                    call "C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\env\\Scripts\\activate.bat"
                    cd "C:\\Users\\Usuario\\Desktop\\8vo ciclo\\Software Security2\\UNIDAD 2\\entorno\\ProyectFinalDBP"
                    dir
                    python manage.py migrate
                    python manage.py runserver 
                '''
            }
        }

        



        /*

        stage('Dynamic Analysis - OWASP ZAP') {
            steps {
                echo 'Running dynamic security tests with OWASP ZAP...'
                bat '''
                    "C:\\Users\\Usuario\\Desktop\\zap\\ZAP_2_15_0_windows.exe" -quickurl http://localhost:8000 -quickout zap_report.txt
                '''
            }
        }

        */





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
