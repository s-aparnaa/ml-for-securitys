# 🧾 Secure Vibe Payment Widget

This project demonstrates how to build and secure a simple frontend payment widget using Secure Vibe Coding practices. It includes secure code generation, pre-commit scanning, GitHub Actions integration, and AI-assisted coding. Below is a full walkthrough of all setup steps.

---

## 📦 Environment Setup

### 🔹 1. Create and Activate Conda Environment
```bash
conda create -n secure-vibe python=3.10 -y
conda activate secure-vibe
```

### 🔹 2. Install Required Tools
```bash
pip install ggshield semgrep pre-commit
```

---

## 🔐 GitGuardian Setup

### 🔹 3. Create a Personal Token
- Go to [dashboard.gitguardian.com](https://dashboard.gitguardian.com)
- Log in and create an API token under **API > Personal Access Tokens**

### 🔹 4. Authenticate `ggshield`
```bash
ggshield auth login
```

Paste your token when prompted.

---

## 🧰 Git + Pre-commit Setup

### 🔹 5. Install Git on Windows
Download from [https://git-scm.com/download/win](https://git-scm.com/download/win)  
During installation, choose:  
✅ "Git from the command line and also from 3rd-party software"

### 🔹 6. Initialize Git Repository
```bash
git init
```

### 🔹 7. Set up Pre-commit Hook
Ensure `.pre-commit-config.yaml` is present, then:
```bash
pre-commit install
```

> This enables automatic scanning for secrets using GitGuardian before every commit.

---

## 🛡️ Pre-commit Test

Make a dummy change:
```bash
echo "# test" >> test.md
git add test.md
git commit -m "test: trigger pre-commit"
```

Expected output:
```
[INFO] Running ggshield...
[INFO] No secrets found.
```

---

## ☁️ GitHub Integration

### 🔹 8. Setup GitHub Actions for Secret Scanning
Move the following file to the root of your repo:
```
.github/workflows/secrets-scan.yml
```

Example contents:
```yaml
name: GitGuardian Secret Scan

on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install ggshield
        run: pip install ggshield
      - name: Run ggshield scan
        run: ggshield secret scan repo .
```

---

## 🏷️ Badge for README

Add this to your `README.md` (adjust `USERNAME` and `REPO`):

```markdown
![Secret Scan](https://github.com/USERNAME/REPO/actions/workflows/secrets-scan.yml/badge.svg)
```

---

## ✅ Optional Add-ons

- 🔍 `semgrep scan --config auto .` — for JS/CSS/HTML security patterns
- 🌐 GitHub Pages — to host the `index.html` widget
- 💼 LinkedIn post — to showcase your AI + security workflow

---

## 🎉 You Did It!

You're now using **Secure Vibe Coding** with:
- Conda environment
- AI-generated frontend
- `ggshield` secret scans (local + CI)
- GitHub Actions automation
- DevSecOps best practices


---

## 🤖 Prompt-Driven Development

The initial version of the `index.html`, `styles.css`, and `app.js` files was created using AI-assisted development through ChatGPT. Specific prompts were used to:

- Generate secure and aesthetic frontend code
- Implement client-side validation (Luhn algorithm)
- Apply Vibe Coding themes (dark mode, responsive UI)
- Embed security review and comments into the code

Prompts used have been documented in the development notebook and can be added as part of future transparency or AI audit logs.

This project demonstrates how generative AI can be safely combined with traditional DevSecOps practices to create beautiful, secure, and auditable codebases.

