# AI-Powered IaC Security Pipeline for T2S

This project simulates a real-world DevSecOps case for Transformed 2 Succeed (T2S), combining infrastructure, containers, secret detection, and AI-powered recommendations into one automated GitHub CI/CD workflow.

---

## Case Scenario

**Client:** T2S (Transformed 2 Succeed)  
**Problem:** Security checks were inconsistently enforced across infrastructure and app deployments—resulting in risks such as misconfigured resources, insecure containers, and secret leakage.  
**Goal:** Automate security scans and use AI to summarize findings and provide remediation strategies after every GitHub commit or pull request.

---

## Features

- Scans **Terraform** code for misconfigurations with **Checkov**
- Analyzes **Docker containers** for vulnerabilities with **Trivy**
- Detects **hardcoded secrets** with **Gitleaks**
- Uses **OpenAI** to generate a readable audit report and visual summary
- Automatically runs after every commit or PR via **GitHub Actions**

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/Here2ServeU/iac-security-pipeline.git
cd iac-security-pipeline
```

2. (Optional) Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install Python requirements:

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key to a `.env` file:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5. Push changes or open a pull request. GitHub Actions will:
   - Run Checkov on your Terraform configs
   - Scan the Dockerfile with Trivy
   - Detect secrets using Gitleaks
   - Auto-generate:
     - `ai-security-analysis.md` – a human-readable summary with GPT recommendations
     - `devsecops_scan_results.png` – a visual chart of scan severity counts

---

## GitHub Actions Workflow

The workflow is defined in:

```
.github/workflows/security.yml
```

What it does:
- Runs all scanners
- Installs dependencies (Checkov, Trivy, Gitleaks, OpenAI client)
- Executes `.github/scripts/ai_analyzer.py` to analyze results and produce summary files

---

## Project Structure

```
.github/
└── workflows/
    └── security.yml              # CI pipeline
.github/scripts/
└── ai_analyzer.py               # AI recommendations & chart generator
terraform/
├── main.tf, variables.tf        # Sample IaC to scan
docker/
└── Dockerfile                   # Sample container config
checkov-report.json              # Output from Checkov
trivy-report.json                # Output from Trivy
gitleaks-report.sarif            # Output from Gitleaks
ai-security-analysis.md          # AI-generated recommendations
devsecops_scan_results.png       # Vulnerability visual chart
requirements.txt                 # Python dependencies
```

---

## Sample Use Case Impact

This pipeline enables T2S to:
- Enforce security gates early in the CI/CD cycle
- Catch S3 misconfigs, insecure ports, or untagged resources (Checkov)
- Find outdated vulnerable libraries (Trivy)
- Block secrets like AWS keys and tokens (Gitleaks)
- Deliver a summarized, visual report via GPT to leadership and DevOps teams

---

## Tools Used

- `Checkov` – IaC scanning
- `Trivy` – Container scanning
- `Gitleaks` – Secret detection
- `OpenAI` – Remediation advice + executive summary
- `GitHub Actions` – CI/CD pipeline automation

---

## Cleanup

```bash
deactivate
rm -rf venv
rm *.json *.sarif *.png *.md
```

---

## Author

By Emmanuel Naweji, 2025  
**Cloud | DevOps | SRE | DevSecOps | FinOps | AI Engineer**  
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

- [LinkedIn](https://www.linkedin.com/in/ready2assist/)
- [GitHub](https://github.com/Here2ServeU)
- [Medium](https://medium.com/@here2serveyou)

---

## Book a Free Consultation

Let’s talk about securing your CI/CD pipeline with AI-driven automation.  
👉🏾 [Schedule a free 1:1 consultation](https://bit.ly/letus-meet)
