# Obsidian Local AI

A local-first AI automation toolkit for Obsidian.

This project lets you:
- Summarize notes
- Auto-tag notes
- Organize markdown files

Everything runs locally using Ollama.
No OpenAI. No API credits. No internet required.

---

# FULL SETUP GUIDE (From Absolute Beginning)

This guide assumes:

You have:
- Windows / Mac / Linux
- No prior setup
- No models installed

Follow in order.

---

# 1️⃣ Install Python

Download Python:

https://www.python.org/downloads/

Important:
✔ Choose Python 3.10 or higher  
✔ Check "Add Python to PATH" during install  

After install, open terminal (CMD or PowerShell) and check:
'''bash 
python --version 
'''


You should see something like:
Python 3.11.x

If not, reinstall and make sure PATH is enabled.

---

# 2️⃣ Install Git (Required)

Download Git:

https://git-scm.com/downloads

After install:
'''bash
git --version 
'''

If version shows, it's installed.

---

# 3️⃣ Install Ollama (Local AI Engine)

Ollama runs AI models locally on your machine.

Download:

https://ollama.com/download

Install normally.

After installation, open terminal and check:
'''bash
ollama --version
 '''

Now start Ollama server:
'''bash
ollama serve 
'''

IMPORTANT:
- This runs the local AI server.
- It runs on http://localhost:11434
- Keep this running in background.

If port error appears, Ollama is already running.

---

# 4️⃣ Download a Model

You must download a model before using AI.

Recommended model:
'''bash
ollama pull deepseek-coder:6.7b 
'''

OR lighter model (better for 8GB RAM machines):
'''bash
ollama pull qwen:3b 
'''


Test model:
'''bash
ollama run deepseek-coder:6.7b 
'''


If it responds, it works.

Exit model:
'''bash
/bye
 '''


---

# 5️⃣ Clone This Project

Now clone this repository:
'''bash
 git clone https://github.com/YOUR_USERNAME/obsidian-local-ai.git

cd obsidian-local-ai 
'''


IMPORTANT:
You must run all Python commands inside this folder.
If you run from another folder, it will not work.
Example correct path: 
'''bash
 C:\Users\YourName\obsidian-local-ai> 
 '''

---

# 6️⃣ Install Python Dependencies

Inside project folder:
'''bash
 pip install -r requirements.txt
  '''

This installs:
- requests

---

# 8️⃣ Configuration

Open config.json:
{
"model": "deepseek-coder:6.7b",
"ollama_url": "http://localhost:11434/api/generate
"
}


You can change model name here if needed.

---

# 10️⃣ Using Aider (AI Coding Assistant)

Aider allows AI to edit your code automatically.

Install Aider:
'''bash
pip install aider-chat 
'''


To use Aider with Ollama:

Go inside your project folder:
cd obsidian-local-ai

Run :
'''bash
python -m aider --model ollama/deepseek-coder:6.7b 
'''


Important:
- You must run this in the folder you want AI to edit.
- Aider creates and edits files ONLY in the current folder.
- It also creates a git repository automatically if not present.

Example:

Inside folder:
'''bash
create a file called test.txt that says hello world 
'''


It will:
- Generate file
- Ask permission
- Commit changes to git

Aider edits files only in current directory.

---

# How Aider + Ollama Work Together

Aider:
- Reads your project files
- Sends prompt to Ollama
- Gets response
- Applies edits
- Creates git commit

Everything local.
No cloud.

---

# Important Rules

✔ Always run from correct folder  
✔ Always keep Ollama running  
✔ Model must be downloaded first  
✔ Files are created in current directory  

If something fails:
Check:
- Ollama is running
- Model name matches config
- You are in correct folder

---

# Example Full Workflow

Start Ollama:
'''bash
ollama serve 
'''


Open new terminal.

Go to project:
'''bash
cd obsidian-local-ai
 '''


Run summarize:
'''bash
 python -m main summarize note.md
  '''


Run Aider:
'''bash
 python -m aider --model ollama/deepseek-coder:6.7b 
 '''


---

# RAM Requirements

deepseek-coder:6.7b → ~8GB RAM  
qwen:3b → ~4GB RAM  

If slow:
Switch to smaller model.

---

# Why This Matters

- No API cost
- No privacy leak
- Fully local
- Open-source
- Extendable

---

# Future Improvements

- Full Obsidian plugin
- Background vault scanning
- Automatic daily summary
- Tag clustering
- GUI version

---

# License

MIT License

---

# Final Note

This is a local AI automation system for Obsidian users who want full control over their data and workflow.