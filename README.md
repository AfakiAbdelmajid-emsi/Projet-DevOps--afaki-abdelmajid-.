# 🚀 DevOps CI/CD Pipeline with Jenkins

## 📌 Project Overview

This project demonstrates the implementation of a **CI/CD (Continuous Integration / Continuous Deployment) pipeline** using **Jenkins**, integrated with **GitHub**, **Docker**, **Python**, **Pytest**, **ngrok**, and **Slack**.

The pipeline is fully automated:
- Any **push to GitHub** triggers Jenkins automatically
- Jenkins builds the project
- Runs **unit tests**
- **Deploys only if tests pass**
- Sends **Slack notifications** on success or failure

---

## 🧱 Technologies Used

### 🔹 Technologies required by the module
- **GitHub** – Source code management and webhook triggering
- **Jenkins** – CI/CD automation server
- **Docker** – Running Jenkins in an isolated container

### 🔹 Additional technologies
- **Python** – Sample application language
- **Pytest** – Unit testing framework
- **ngrok** – Exposes local Jenkins to GitHub webhooks
- **Slack** – Pipeline status notifications

---

## 📁 Project Structure

```
.
├── app.py              # Python application
├── test_app.py         # Unit tests
├── requirements.txt    # Python dependencies
├── Jenkinsfile         # Jenkins pipeline definition
├── pytest.ini         # Pytest configuration
└── README.md           # Project documentation
```

---

## ⚙️ Prerequisites

Make sure the following are installed:

- Docker
- Git
- ngrok
- A GitHub account
- A Slack workspace

---

## 🐳 Run Jenkins with Docker

Start Jenkins using Docker:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts-jdk17
```

Check Jenkins container:

```bash
docker ps
```

Access Jenkins UI:

```
http://localhost:8080
```

## 🔑 Jenkins Initial Setup

Get the initial admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Then:

1. Install recommended plugins
2. Create admin user
3. Ensure these plugins are installed:
   - Git
   - GitHub Integration
   - Pipeline

## 🔁 Create Jenkins Pipeline Job

1. **New Item** → **Pipeline**
2. Job name: `PipeLine-afaki-abdelmajid`
3. **Source Code Management** → **Git**
4. Repository URL:

```
https://github.com/AfakiAbdelmajid-emsi/Projet-DevOps--afaki-abdelmajid-..git
```

5. Add GitHub credentials (Personal Access Token)
6. **Pipeline definition**: Pipeline script from SCM
7. Branch: `main`
8. Save

## 🌐 Expose Jenkins Using ngrok

Start ngrok:

```bash
ngrok http 8080
```

You will get a public URL such as:

```
https://xxxx.ngrok-free.dev
```

## 🔗 Configure GitHub Webhook

In your GitHub repository:

1. **Settings** → **Webhooks** → **Add webhook**
2. Payload URL:

```
https://xxxx.ngrok-free.dev/github-webhook/
```

3. Content type:

```
application/json
```

4. Events:

```
Just the push event
```

5. Active: ✔

## 🧪 Pipeline Execution Flow

The pipeline defined in the Jenkinsfile includes:

1. **Checkout** – Pull code from GitHub
2. **Setup Python Environment**
   - Install Python
   - Create virtual environment
   - Install dependencies
3. **Run Tests**
   - Execute pytest
4. **Deploy**
   - Runs only if tests pass
5. **Post Actions**
   - Send Slack notification

## ❌ Test Failure Behavior

If a test fails:

- Jenkins marks the build as **FAILED**
- Deploy stage is **skipped**
- Slack receives ❌ **Pipeline FAILED**

This behavior demonstrates correct CI/CD quality control.

## ▶️ Trigger the Pipeline

Make a change and push it:

```bash
git add .
git commit -m "test pipeline"
git push
```

Jenkins will start automatically.

## 📊 Expected Results

- ✅ Automatic pipeline trigger on GitHub push
- ✅ Unit tests executed
- ✅ Deployment blocked on failure
- ✅ Slack notifications sent
- ✅ Full traceability of builds and commits

## 🎓 Educational Value

This project demonstrates:

- Real CI/CD automation
- Jenkins pipeline best practices
- Test-driven deployment
- DevOps workflow automation

## 👤 Author

**Abdelmajid Afaki**  
DevOps Project – 2025/2026
