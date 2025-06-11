from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>T2S Services – DevOps & SRE with AI</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; background-color: #f9f9f9; color: #333; }
        h1 { color: #0052cc; }
        ul { margin-top: 20px; }
        li { margin: 10px 0; }
        footer { margin-top: 50px; font-size: 0.9em; color: #777; }
    </style>
</head>
<body>
    <h1>Welcome to T2S Services</h1>
    <p>We specialize in transforming your infrastructure with modern DevOps, Site Reliability Engineering (SRE), and AI-powered solutions.</p>

    <h2>Our Services</h2>
    <ul>
        <li>Infrastructure Automation with Terraform, Ansible, and Pulumi</li>
        <li>CI/CD Pipelines using GitHub Actions, Jenkins, GitLab CI</li>
        <li>Kubernetes & Cloud-Native Deployment (EKS, AKS, GKE)</li>
        <li>Observability Engineering with Prometheus, Grafana, Datadog</li>
        <li>AI-powered Cloud Cost Optimization & Incident Prediction</li>
        <li>DevSecOps – Security integrated into DevOps workflows</li>
    </ul>

    <footer>
        By Emmanuel Naweji – Helping businesses modernize through automation and AI.<br>
        <a href="https://linkedin.com/in/ready2assist">Connect on LinkedIn</a>
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
