import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI
from fpdf import FPDF

# Load environment variables from .env
load_dotenv()

# Simulated scan results
scan_summary = {
    "Checkov": {"Critical": 3, "High": 4, "Medium": 3, "Low": 2},
    "Trivy": {"Critical": 5, "High": 10, "Medium": 7, "Low": 4},
    "Gitleaks": {"Critical": 1, "High": 1, "Medium": 1, "Low": 0},
    "AI Best Practices": {"Critical": 2, "High": 1, "Medium": 1, "Low": 1}
}

# Detailed recommendations per tool and severity
recommendations = {
    "Checkov": {
        "Critical": "Audit IAM roles and block unrestricted access.",
        "High": "Enable encryption and enforce compliance checks.",
        "Medium": "Tag cloud resources and apply default security groups.",
        "Low": "Standardize all resource declarations in Terraform."
    },
    "Trivy": {
        "Critical": "Use minimal base images and patch critical CVEs.",
        "High": "Schedule regular rebuilds with updated dependencies.",
        "Medium": "Reduce unnecessary packages in Dockerfiles.",
        "Low": "Evaluate third-party package sources."
    },
    "Gitleaks": {
        "Critical": "Remove secrets from repo history and rotate keys.",
        "High": "Use env variables or secrets managers instead of hardcoding.",
        "Medium": "Educate developers on secret hygiene best practices.",
        "Low": "Run secrets scan before each commit."
    },
    "AI Best Practices": {
        "Critical": "Enforce build breaks for Critical issues and add auto-linting.",
        "High": "Notify team leads on Slack when High issues are detected.",
        "Medium": "Suggest fixes using GPT-based inline code comments.",
        "Low": "Review low-severity suggestions during weekly retros."
    }
}

# Build the recommendations table for CSV
rows = []
for tool, severity_data in scan_summary.items():
    for severity, count in severity_data.items():
        if count > 0:
            rows.append({
                "Tool": tool,
                "Severity": severity,
                "Count": count,
                "Recommendation": recommendations[tool][severity]
            })

# Save to CSV
csv_path = "devsecops_recommendations.csv"
df = pd.DataFrame(rows)
df.to_csv(csv_path, index=False)

# Generate scan result chart
categories = list(scan_summary.keys())
critical = [scan_summary[t]["Critical"] for t in categories]
high = [scan_summary[t]["High"] for t in categories]
medium = [scan_summary[t]["Medium"] for t in categories]
low = [scan_summary[t]["Low"] for t in categories]

bar_width = 0.2
x = range(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - 1.5 * bar_width for i in x], critical, width=bar_width, label='Critical', color='darkred')
ax.bar([i - 0.5 * bar_width for i in x], high, width=bar_width, label='High', color='orange')
ax.bar([i + 0.5 * bar_width for i in x], medium, width=bar_width, label='Medium', color='gold')
ax.bar([i + 1.5 * bar_width for i in x], low, width=bar_width, label='Low', color='green')

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("Issue Count")
ax.set_title("DevSecOps Scan Results Overview")
ax.legend()

plt.tight_layout()
chart_path = "devsecops_scan_results.png"
plt.savefig(chart_path)

# Output
print(f" Chart saved as: {chart_path}")
print(f" Recommendations CSV saved as: {csv_path}")
