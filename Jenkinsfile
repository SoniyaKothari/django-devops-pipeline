@Library("libs") _

pipeline 
{
    agent any

    stages 
    {
        stage('Git Success') 
        {
            steps 
            {
                sh 'echo "Hurray!"'
            }
        }

        stage('Docker build') 
        {
            steps 
            {
                script
                {
                    build("django-app","latest","soniya06")
                }
            }
        }

        stage('DockerHub login') 
        {
            steps 
            {
                sh 'echo "Logged-in"'
            }
        }

        stage('DockerHub push') 
        {
            steps 
            {
                script
                {
                    pushDockerImage("django-app","latest","soniya06")
                }
            }
        }

        stage('Deploy to Kubernetes')
        {
            steps
            {
               script
               {
                    deployToK8s()
               }
            }
        }
    }
}
