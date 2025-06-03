# 🚀 Deployment

This file documents how the **ArtifexLab API** was deployed, covering all tools, environment variables, and setup steps. The goal is to allow others to replicate (or troubleshoot!) the deployment process.

---

## 🔧 Core Technologies & Tools Used

- 🐙 **Git & GitHub** – Version control and remote repository hosting
  _Used from the very beginning to track progress and safely back up the project._

- 🐍 **Python 3.11** – The programming language used to build the backend

- 🌐 **Django 3.2** – Web framework powering the backend logic
  _Temporarily upgraded to Django 5.2.1 during dev, but pinned to 3.2 for deployment stability._

- 🛠️ **Django REST Framework** – Used to build RESTful API endpoints

- ☁️ **Cloudinary** – For media storage (e.g. user-uploaded profile pics and artwork)

- 🔥 **Gunicorn** – WSGI server that runs the app in production

- 🔐 **dj-rest-auth** – Handles authentication, registration, and JWT token management

- 🔄 **CORS Headers** – Allows frontend and backend to safely communicate across domains

- 🐘 **PostgreSQL** – Production database (hosted using Code Institute’s setup, not ElephantSQL)

- 🚀 **Heroku** – Hosting platform used for live deployment

---

## 🗂️ Creating the Repository

### Tools Used

- 🐙 **GitHub** — To create and host the project repository
- 🧑‍💻 **Visual Studio Code (VS Code)** — Used for writing code and managing the project
- 🧬 **Git** — Built into VS Code for version control and pushing commits

### Steps Taken

#### ✅ Create the GitHub Repository

1. Head to [GitHub](https://github.com) and click the ➕ icon in the top-right corner.
2. Select **New repository**.
3. Fill in the details:
   - **Repository name:** `artifexlab-api`
   - Add a short description
   - Set visibility to **Public**
   - Tick the box to **Add a README file**
   - Choose **VisualStudioCode** from the `.gitignore` dropdown to exclude workspace files
4. Click **Create repository** — you're ready to start coding! 🎉

---

## 🧲 Cloning the Repo into VS Code

Here’s how I got the project set up locally using the built-in Git tools in VS Code:

1. Open **Visual Studio Code**.
2. On the Welcome screen, click **Clone Git Repository**.
3. Paste in the GitHub clone URL (e.g. `https://github.com/your-username/artifexlab-api.git`).
4. Choose where on your local machine you want to save the project.
5. VS Code will clone the repo and ask if you want to open it in the current window or a new one.
6. Once opened, confirm Git is working by checking the **Source Control** panel (👁️‍🗨️ icon on the left sidebar).
7. You're now set up to start coding, committing, and pushing to GitHub! 🙌

📚 **Reference:**
[How to clone a GitHub repository into Visual Studio Code – Microsoft Docs](https://learn.microsoft.com/en-us/visualstudio/version-control/git-clone-repository?view=vs-2022&utm_source=chatgpt.com)

---

## 🧪 2. Create and Activate a Virtual Environment

Before installing any packages, it’s a good idea to set up a **virtual environment**. This keeps your project’s dependencies neatly contained — so you’re not installing things globally or messing with other Python projects on your system.

Here’s how I did it inside **VS Code**:

### ✅ Steps

1. Open the **Terminal** in VS Code
   You can do this with the shortcut ` Ctrl + `` (backtick) `, or from the menu:
   **Terminal → New Terminal**

2. Create the virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:

- **On Windows:**

```bash
.venv\Scripts\activate
```

- **On Mac/Linux:**

```bash
source .venv/bin/activate
```

4. You’ll know it worked when you see (.venv) at the beginning of your terminal line.

### 🔐 Why You Need an env.py File

Once your virtual environment is activated, you’ll often need to store sensitive info like API keys, Cloudinary credentials, or secret tokens. For this, we create a file called env.py.

##### What goes in it?

Example:

```python
import os

os.environ["CLOUDINARY_URL"] = "your-cloudinary-url-here"
os.environ["SECRET_KEY"] = "your-django-secret-key"
```

This way, your keys stay safe and out of version control.

### Don’t forget!

👉 Add env.py to your .gitignore file so it never gets pushed to
This keeps your private data private 🔐
