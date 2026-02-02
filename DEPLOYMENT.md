# GitHub Deployment Guide

Follow these steps to push your Unit Converter application to GitHub and deploy it on Render.

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Repository name: `unit-converter`
4. Description: "A simple unit converter web application built with Flask"
5. Choose "Public" or "Private" as you prefer
6. DO NOT initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

## Step 2: Initialize Git and Push to GitHub

Open Command Prompt or PowerShell and run these commands:

```bash
# Navigate to your project
cd C:\Users\djsce.student\Desktop\a035\unit-converter

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Unit Converter Flask app"

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/unit-converter.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Deploy on Render

### If you don't have a Render account:
1. Visit [render.com](https://render.com)
2. Click "Sign up" and choose "Continue with GitHub"
3. Authorize Render to access your GitHub account

### Deploy the app:
1. Log in to your Render dashboard
2. Click "New +" button and select "Web Service"
3. Select your `unit-converter` repository
4. Fill in the configuration:
   - **Name**: unit-converter
   - **Region**: Choose nearest to you
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (for testing)
5. Click "Create Web Service"
6. Wait for deployment (2-5 minutes)
7. Your app will be live at the provided URL

## Step 4: Update Render when you make changes

After making changes and pushing to GitHub:
1. Render will automatically detect the push
2. It will rebuild and redeploy automatically
3. No additional steps needed!

## Adding Gunicorn to Production

The production server uses Gunicorn. It's automatically installed on Render, but to test locally:

```bash
pip install gunicorn
gunicorn app:app
```

## Useful Git Commands

```bash
# Check status
git status

# Add specific files
git add app.py

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push changes to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log
```

## Troubleshooting

### "Git not found"
- Install Git from [git-scm.com](https://git-scm.com/download/win)
- Restart PowerShell/Command Prompt

### "Remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/unit-converter.git
```

### Render deployment fails
- Check build logs in Render dashboard
- Ensure all files are pushed to GitHub
- Verify `requirements.txt` and `Procfile` are correct

## Next Steps

1. Add new features (more conversion types, history, etc.)
2. Improve UI/UX
3. Add unit tests
4. Create GitHub Issues for improvements
5. Share with others!

---

Happy deploying! 🚀
