# DevOps CI/CD Pipeline with Jenkins

Réalisé par : afaki abdelmajid

📌 Project Overview

This project demonstrates the implementation of a CI/CD (Continuous Integration / Continuous Deployment) pipeline using Jenkins, integrated with GitHub, Docker, Python, and Slack.

The pipeline is fully automated:

Any push to GitHub triggers Jenkins

Jenkins builds the project

Runs unit tests

Deploys only if tests pass

Sends Slack notifications on success or failure

🧱 Technologies Used
🔹 Mandatory (Module Requirements)

GitHub – Source code management & webhook trigger

Jenkins – CI/CD automation server

Docker – Run Jenkins in an isolated environment

🔹 Additional Technologies

Python – Sample application

Pytest – Unit testing framework

ngrok – Expose local Jenkins to GitHub webhooks

Slack – Pipeline status notifications

📁 Project Structure
.
├── app.py                 # Python application
├── test_app.py            # Unit tests (pytest)
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # Jenkins pipeline definition
├── pytest.ini             # Pytest configuration
└── README.md              # Project documentation

⚙️ Prerequisites

Make sure you have installed:

Docker

Git

ngrok (free version is enough)

A GitHub account

A Slack workspace (for notifications)

🐳 Step 1 – Run Jenkins with Docker

Run Jenkins in a Docker container:

docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts-jdk17


Check that Jenkins is running:

docker ps


Then open Jenkins in your browser:

http://localhost:8080

🔑 Step 2 – Initial Jenkins Setup

Get the initial admin password:

docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword


Install recommended plugins

Create an admin user

Install plugins if not already installed:

Git

GitHub Integration

Pipeline

🔁 Step 3 – Create Jenkins Pipeline Job

New Item → Pipeline

Name: PipeLine-afaki-abdelmajid

Source code management → Git

Repository URL:

https://github.com/AfakiAbdelmajid-emsi/Projet-DevOps--afaki-abdelmajid-..git


Credentials: GitHub Personal Access Token

Pipeline definition: Pipeline script from SCM

Branch: main

Save

🌐 Step 4 – Expose Jenkins with ngrok

Start ngrok:

ngrok http 8080


You will get a public URL like:

https://xxxx.ngrok-free.dev

🔗 Step 5 – Configure GitHub Webhook

In your GitHub repository:

Settings → Webhooks → Add webhook

Payload URL:

https://xxxx.ngrok-free.dev/github-webhook/


Content type:

application/json


Events:

Just the push event


Active: ✅

🧪 Step 6 – How the Pipeline Works
Jenkinsfile stages:

Checkout – Pull code from GitHub

Setup Python Environment

Install Python

Create virtual environment

Install dependencies

Run Tests

Execute pytest

Deploy

Executed only if tests pass

Post Actions

Send Slack notification (SUCCESS or FAILURE)

❌ Example: Test Failure Behavior

If a test fails:

Jenkins marks the build as FAILED

Deploy stage is skipped

Slack receives ❌ Pipeline FAILED

This behavior is intentional and demonstrates quality gating.

📣 Slack Notifications

Slack notifications are sent automatically:

✅ Pipeline SUCCESS

❌ Pipeline FAILED

Slack Webhook URL is stored as a Jenkins credential for security.

▶️ How to Trigger the Pipeline

Make any change in the project, for example:

git add .
git commit -m "test pipeline"
git push


➡️ Jenkins will start automatically
➡️ No manual action required

📊 Expected Results

Jenkins build triggered by GitHub push

Unit tests executed automatically

Deployment blocked if tests fail

Slack notifications received

Full traceability of commits and builds

🎓 Educational Value

This project demonstrates:

Real CI/CD pipeline

Jenkins security behavior

Importance of unit tests

DevOps best practices

Automation without manual intervention

📌 Notes

ngrok URL changes after restart → update GitHub webhook if needed

CSRF protection is handled by Jenkins webhook endpoint

This setup is suitable for academic and demo purposes

👤 Author

Abdelmajid Afaki
DevOps Project – 2025/2026
