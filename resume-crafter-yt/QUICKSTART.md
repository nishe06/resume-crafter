# Quick Start Guide - Resume Crafter

## How to Run the Application

### Step 1: Navigate to the Project Directory
```bash
cd "/Users/nishetha/Documents/resume crafter yt/resume-crafter-yt"
```

### Step 2: Activate the Virtual Environment
```bash
source ../venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

### Step 3: Install Dependencies (if not already installed)
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application
```bash
python app.py
```

### Step 5: Open in Browser
Once the server starts, you should see output like:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

Open your browser and go to:
```
http://localhost:5001
```
or
```
http://127.0.0.1:5001
```

## Troubleshooting

### Port Already in Use
If you see "Address already in use", either:
- Kill the process using port 5001: `lsof -ti:5001 | xargs kill -9`
- Or change the port in `app.py` (line 121) to a different port (e.g., 5002)

### Module Not Found Errors
Make sure your virtual environment is activated and dependencies are installed:
```bash
source ../venv/bin/activate
pip install -r requirements.txt
```

### OpenAI API Key
Make sure your OpenAI API key is set in `app.py` (line 32) or as an environment variable.

## Stopping the Server
Press `Ctrl + C` in the terminal to stop the server.

