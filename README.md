
# AI-Powered IaC Security Pipeline & T2S Services App

This project simulates a **real-world DevSecOps solution for Transformed 2 Succeed (T2S)**. It integrates secure infrastructure automation, container hardening, secret detection, and an AI-powered audit engine—all packaged with a containerized web application (`t2s-services`) to showcase the services offered by T2S in **DevOps, SRE, and AI engineering**.

---

## Case Scenario

**Client:** T2S (Transformed 2 Succeed)  
**Problem:** Disconnected security practices across the SDLC led to vulnerabilities in IaC, containers, and source code. T2S also needed a central way to present its service offerings.  
**Goal:**  
1. Build an automated CI/CD security pipeline using industry-standard tools.  
2. Leverage AI to summarize findings and offer remediation guidance.  
3. Deploy a clean, containerized Flask app to showcase DevOps/SRE/AI services.

---

## Features

- Scans **Terraform** for misconfigurations using **Checkov**
- Analyzes **Docker** containers for vulnerabilities via **Trivy**
- Detects **hardcoded secrets** using **Gitleaks**
- Executes AI-based audits using **OpenAI** with PDF and chart generation
- Deploys a **Flask web app** (`t2s-services`) showcasing T2S offerings
- Fully automated via **GitHub Actions**

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── security.yml         # CI/CD pipeline
│
├── .github/scripts/
│   └── ai_analyzer.py           # Generates AI PDF report & vulnerability chart
│
├── terraform/
│   └── *.tf                     # Example IaC config to scan
│
├── t2s-services/                # Flask service showcase app
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── checkov-report.json          # Checkov scan output
├── trivy-report.json            # Trivy scan output
├── gitleaks-report.sarif        # Gitleaks scan output
├── devsecops_scan_results.png   # AI-generated scan severity chart
├── ai-security-analysis.pdf     # AI-generated executive report
└── requirements.txt             # Python dependencies for local use
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Here2ServeU/iac-security-pipeline.git
cd iac-security-pipeline
```

### 2. (Optional) Create Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Required Python Packages

```bash
pip install -r requirements.txt
```

### 4. Set Your OpenAI API Key

Create a `.env` file in the root directory:

```dotenv
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Running the Pipeline

On each **GitHub commit or pull request**, the pipeline will:
- Run Checkov on your Terraform code
- Scan Dockerfile using Trivy
- Detect exposed secrets via Gitleaks
- Execute `ai_analyzer.py` to:
  - Generate a **PDF summary report**
  - Produce a **bar chart** of vulnerability counts per tool

Outputs:
- `devsecops_scan_results.png`
- `ai-security-analysis.pdf`

---

## Running the T2S Services App

This Flask app summarizes DevOps & SRE services offered by T2S.

### 1. Build the Docker Image

```bash
cd t2s-services
docker build -t t2s-services .
```

### 2. Run the App Locally

```bash
docker run -d -p 8000:8000 t2s-services
```

Visit [http://localhost:8000](http://localhost:8000) to view your services app.

---

## Scanning the T2S Dockerfile and Generating AI Reports

1. Ensure you have `Trivy` installed:

```bash
brew install aquasecurity/trivy
```

2. Scan the Dockerfile:

```bash
trivy config --format json --output trivy-report.json t2s-services/Dockerfile
```

3. Run the AI Analyzer script to generate a **visual chart** and **PDF** report:

```bash
python .github/scripts/ai_analyzer.py
```

You will receive:
- `devsecops_scan_results.png` for team presentations
- `ai-security-analysis.pdf` for manager/executive briefings

---

## Real-World Benefits

This integrated solution enables T2S to:

- **Enforce DevSecOps best practices** from commit to deployment
- **Identify and fix security risks early** (IaC misconfigs, vulnerable images, secrets)
- **Produce AI-generated executive reports** for leadership and audits
- **Demonstrate services clearly** using a professional Flask-based web app
- **Train DevOps/SRE teams** with a full example of GitHub-integrated security automation

---

## Tools Used

- **Checkov** – Terraform static analysis
- **Trivy** – Container CVE detection
- **Gitleaks** – Secrets scanning
- **OpenAI** – AI-generated audit summaries and recommendations
- **GitHub Actions** – CI/CD automation
- **Flask** – Web app for showcasing services
- **Docker** – Containerization for deployment and scanning

---

## Cleanup

```bash
deactivate
rm -rf venv
rm *.json *.sarif *.png *.pdf
docker stop $(docker ps -q)
docker system prune -f
```

---

## Author

**Built by Emmanuel Naweji, 2025**

**Cloud | DevOps | SRE | FinOps | AI Engineer**  

Helping businesses modernize infrastructure and guiding engineers into top 1% career paths through real-world projects and automation-first thinking.

![AWS Certified](https://img.shields.io/badge/AWS-Certified-blue?logo=amazonaws)
![Azure Solutions Architect](https://img.shields.io/badge/Azure-Solutions%20Architect-0078D4?logo=microsoftazure)
![CKA](https://img.shields.io/badge/Kubernetes-CKA-blue?logo=kubernetes)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-blue?logo=githubactions)
![GitLab CI](https://img.shields.io/badge/CI/CD-GitLab%20CI-FC6D26?logo=gitlab)
![Jenkins](https://img.shields.io/badge/CI/CD-Jenkins-D24939?logo=jenkins)
![Ansible](https://img.shields.io/badge/Automation-Ansible-red?logo=ansible)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange?logo=argo)
![VMware](https://img.shields.io/badge/Virtualization-VMware-607078?logo=vmware)
![Linux](https://img.shields.io/badge/OS-Linux-black?logo=linux)
![FinOps](https://img.shields.io/badge/FinOps-Cost%20Optimization-green?logo=money)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-ff9900?logo=openai)

---

## Connect with Me

- [LinkedIn](https://www.linkedin.com/in/ready2assist)
- [GitHub](https://github.com/Here2ServeU)
- [Free Strategy Call](https://bit.ly/letus-meet)

