pipeline{
    agent by
    stages{
        stage('checkout code'){
            steps{
                checkout scm
            }
        
        }
        stage('Run python project'){
            steps{
                bat 'python app.py'
            }
        }
    }
    post{
        success{
            echo "build successfully"
        }
        failure{
            echo "build failed"
        }
    }
}