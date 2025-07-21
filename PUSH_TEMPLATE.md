# 🚀 GitHub Push Commands Template

## After you create your Personal Access Token, use these commands:

### Replace these values:
- YOUR_USERNAME = Your GitHub username
- YOUR_REPO_NAME = Your repository name  
- YOUR_TOKEN = Your personal access token

```bash
# Navigate to your project
cd "c:\Users\Sardar Ahmed\PycharmProjects\ubl_jd_chatbot"

# Add your GitHub repository as remote
git remote add origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push your code to GitHub
git push -u origin main
```

## Example (with fake data):
If your username is "sardaahmed" and repo is "ubl-career-portal":
```bash
git remote add origin https://ghp_xxxxxxxxxxxxxxxxxxxx@github.com/sardaahmed/ubl-career-portal.git
git push -u origin main
```

## Verification Commands:
```bash
# Check if remote was added correctly
git remote -v

# Check current status
git status

# View your commits
git log --oneline
```

---
**Security Note**: Replace YOUR_TOKEN with your actual token. Keep your token private!
