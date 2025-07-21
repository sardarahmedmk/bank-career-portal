# 🔐 Safe GitHub Authentication Guide

## Method 1: GitHub Desktop (Recommended)
1. Download: https://desktop.github.com/
2. Sign in with your GitHub account
3. Add existing repository from your project folder
4. Publish to GitHub with one click!

## Method 2: Personal Access Token (Command Line)

### Step 1: Create Personal Access Token
1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name: "UBL Career Portal"
4. Scopes: Check "repo" (gives full repository access)
5. Click "Generate token"
6. **COPY THE TOKEN** (you'll only see it once!)

### Step 2: Use Token for Authentication
```bash
# First create the repository on GitHub.com manually
# Then use these commands:

cd "c:\Users\Sardar Ahmed\PycharmProjects\ubl_jd_chatbot"

# Add remote (replace YOUR_USERNAME and YOUR_TOKEN)
git remote add origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/ubl-bank-career-portal.git

# Push to GitHub
git push -u origin main
```

## Method 3: SSH Key (Most Secure)

### Step 1: Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter for default location
# Set a passphrase (optional)
```

### Step 2: Add SSH Key to GitHub
```bash
# Copy your public key
cat ~/.ssh/id_ed25519.pub
# Go to GitHub → Settings → SSH Keys → Add new
# Paste the key content
```

### Step 3: Use SSH URL
```bash
git remote add origin git@github.com:YOUR_USERNAME/ubl-bank-career-portal.git
git push -u origin main
```

## Quick Manual Steps
1. Create repository on GitHub.com
2. Use GitHub Desktop to publish
3. Done! 🎉

---
**Security Note**: Never share your tokens or passwords. Use GitHub Desktop for the easiest experience!
