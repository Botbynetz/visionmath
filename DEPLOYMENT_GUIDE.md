# 🚀 DEPLOYMENT GUIDE - GitHub & PythonAnywhere

## STEP 1: Create GitHub Repository

### 1.1 Create Repository on GitHub
1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `mathvision`
   - **Description**: `Professional Mathematics Learning Platform`
   - **Visibility**: Public (so it's accessible)
   - Leave everything else as default
3. Click **Create repository**
4. Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/mathvision.git`)

### 1.2 Push Code to GitHub
Run these commands in PowerShell:

```powershell
cd "d:\tania's project"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/mathvision.git

# Rename branch to main
git branch -M main

# Push code to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username**

Example:
```powershell
git remote add origin https://github.com/tania123/mathvision.git
git branch -M main
git push -u origin main
```

---

## STEP 2: Setup PythonAnywhere

### 2.1 Create Account
1. Go to https://www.pythonanywhere.com
2. Click **Sign up**
3. Choose **Beginner Plan** (Free, 100MB)
4. Fill in email and password
5. Verify email

### 2.2 Add SSH Key (for easy git clone)
1. Login to PythonAnywhere
2. Go to **Account** → **SSH keys**
3. Click **Add a new SSH key**
4. Copy the public key

Optional: Add to GitHub for automatic authentication

### 2.3 Open Bash Console
1. Go to **Consoles** → **Start a new console** → **Bash**
2. Run these commands:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/mathvision.git

# Navigate to project
cd mathvision/web

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 mathvision

# Install dependencies
pip install -r requirements.txt

# Test the app
python run.py
```

---

## STEP 3: Configure Web App on PythonAnywhere

### 3.1 Create New Web App
1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Python 3.10**
4. Select **Flask**
5. Choose path: `/home/YOUR_USERNAME/mathvision/web`

### 3.2 Configure WSGI File
1. Go to **Web** → **mathvision** (your app)
2. Click **Edit WSGI configuration file**
3. Replace content with:

```python
import sys
path = '/home/YOUR_USERNAME/mathvision/web'
if path not in sys.path:
    sys.path.append(path)

from run import app
application = app
```

4. Click **Save**

### 3.3 Configure Virtualenv
1. In the same Web tab, find **Virtualenv section**
2. Enter: `/home/YOUR_USERNAME/.virtualenvs/mathvision`
3. Click the link to create if it doesn't exist

### 3.4 Set Source Code Directory
1. In **Code section**:
   - **Source code**: `/home/YOUR_USERNAME/mathvision`
   - **Working directory**: `/home/YOUR_USERNAME/mathvision/web`

### 3.5 Add Environment Variables
Scroll down and find **Web app settings → Environment variables**:
- Key: `FLASK_ENV`
- Value: `production`

---

## STEP 4: Reload & Test

1. Scroll to top of Web tab
2. Click **Reload** (green button)
3. Wait 10-20 seconds for reload
4. Your app is now live at: `https://YOUR_USERNAME.pythonanywhere.com`

Example: `https://tania.pythonanywhere.com`

---

## ✅ VERIFICATION CHECKLIST

- [ ] GitHub repository created and pushed
- [ ] PythonAnywhere account created
- [ ] Repository cloned on PythonAnywhere
- [ ] Dependencies installed in virtualenv
- [ ] WSGI file configured
- [ ] Environment variables set
- [ ] Web app reloaded
- [ ] Website accessible at `https://YOUR_USERNAME.pythonanywhere.com`

---

## 📊 Your Live Website URLs

**Local (WiFi)**: `http://192.168.1.9:5000`
**Cloud (Public)**: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🆘 Troubleshooting

### Error: ModuleNotFoundError
- **Solution**: Ensure virtualenv path is correct in Web app settings

### Error: Flask not found
- **Solution**: Reinstall requirements in virtualenv:
  ```bash
  pip install -r requirements.txt
  ```

### Error: 502 Bad Gateway
- **Solution**: Click **Reload** again, wait 30 seconds

### Can't see changes after push
- **Solution**: Pull latest code and reload:
  ```bash
  cd ~/mathvision
  git pull origin main
  # Then reload in PythonAnywhere
  ```

---

## 📱 Access from Anywhere

Once deployed on PythonAnywhere, your app is accessible from:
- ✅ Any device with internet
- ✅ Any country
- ✅ Mobile phones
- ✅ Tablets
- ✅ Desktop computers

Just visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🔄 Future Updates

To update your live website:

1. Make changes locally
2. Push to GitHub:
   ```powershell
   git add .
   git commit -m "Update description"
   git push origin main
   ```

3. On PythonAnywhere bash:
   ```bash
   cd ~/mathvision
   git pull origin main
   ```

4. Reload web app in PythonAnywhere dashboard

---

**Your MathVision Platform is now live! 🎉**
