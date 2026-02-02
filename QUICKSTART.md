# Quick Start Guide

Get your Unit Converter running in minutes!

## Option 1: Run Locally (Recommended for Testing)

### Windows Users

1. **Install Python** (if not already installed)
   - Download from [python.org](https://python.org)
   - Check "Add Python to PATH" during installation

2. **Open Command Prompt or PowerShell**
   - Navigate to project: `cd C:\Users\djsce.student\Desktop\a035\unit-converter`

3. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open browser**
   - Go to: `http://localhost:5000`
   - Done! 🎉

### macOS/Linux Users

1. **Open Terminal**
   - Navigate to project: `cd path/to/unit-converter`

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open browser**
   - Go to: `http://localhost:5000`

## Option 2: Deploy on Render (Production)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## Testing the App

### Try these conversions:

1. **Length**: 100 meters to feet
2. **Weight**: 5 kilograms to pounds
3. **Volume**: 1 gallon to liters
4. **Temperature**: 32 Fahrenheit to Celsius

## Project Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with conversion logic |
| `requirements.txt` | Python packages needed |
| `Procfile` | Configuration for Render deployment |
| `templates/index.html` | Web interface |
| `static/css/style.css` | Styling and layout |
| `README.md` | Full documentation |
| `DEPLOYMENT.md` | GitHub & Render deployment guide |

## Common Issues

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Address already in use"
- Port 5000 is busy. Edit `app.py` line 123:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Virtual environment not activating
- **Windows**: `venv\Scripts\activate.bat`
- **macOS/Linux**: `source venv/bin/activate`

## Next Steps

1. ✅ Run locally and test
2. 📝 Create GitHub account (if needed)
3. 🚀 Deploy to Render
4. 🎨 Customize the app
5. 🔄 Push updates to GitHub

## Need Help?

- Check [README.md](README.md) for full documentation
- See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- Check Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

**Tip**: Press `Ctrl+C` to stop the app when running locally.

Happy coding! 💻
