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
                    push("django-app","latest","soniya06")
                }
            }
        }

        stage('Deploy to Kubernetes')
        {
            steps
            {
                sh '''

                    kubectl apply -f k8s/Deployment.yml
                    kubectl apply -f k8s/Service.yml
                    kubectl port-forward weather-svc 8000:8000 -n devops

                '''
            }
        }
    }
}
