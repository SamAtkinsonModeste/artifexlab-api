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

---

---

## 📦 3. Install Project Dependencies

Once your virtual environment is activated, it’s time to install the packages your Django project needs to run — both locally and on Heroku.

Here’s what I used and why ⬇️

### ✅ Install core dependencies:

```bash
pip install django<4 gunicorn dj_database_url psycopg2 dj3-cloudinary-storage
```

- **django<4** — I pinned Django to stay below version 4 for stability and Heroku compatibility (targeting 3.2).

- **gunicorn** — Required by Heroku to serve Django apps in production.

- **dj_database_url** — Helps Django connect to the production PostgreSQL database using an environment variable.

- **psycopg2** — Lets Django talk to PostgreSQL.

- **django-cloudinary-storage** — Integrates Django with Cloudinary so user-uploaded images (like artwork and profile pics) are stored in the cloud.

---

#### ✅ Install REST framework & authentication tools:

```bash
pip install dj-rest-auth djangorestframework-simplejwt django-cors-headers

```

- **dj-rest-auth** — Handles login, logout, registration, and password reset flows.

- **djangorestframework-simplejwt** — Adds JWT (JSON Web Token) support for secure API access.

- **django-cors-headers** — Allows your frontend and backend to talk to each other from different domains (e.g. React + Django).

---

#### 📝 Save your dependencies

After installing everything, run:

```bash
pip freeze > requirements.txt

```

This saves a list of all installed packages and versions to a file called requirements.txt.

📌 This file is super important — it tells Heroku (and other developers) exactly what’s needed to run your app!

---

---

## 🏗️ Project Setup

### 1. Start the Django Project and First App

With your virtual environment active and dependencies installed, it’s time to get Django up and running 🎉

From your terminal in VSCode, run the following command to create your project:

```bash
django-admin startproject project_name_here .
```

👉 That period at the end is important!
It tells Django to place the project inside the current folder (your cloned repo), rather than creating a whole new subfolder. This keeps everything nice and tidy.

Next, create your first app — in my case, this was the profiles app:

```bash
python manage.py startapp profiles

```

You’ll repeat this step later for each app in your project (e.g. posts, tutorials, comments, etc).

Once that’s done, you’ll see the familiar Django project structure, and you’re ready to start adding your apps to INSTALLED_APPS and writing views. 💻✨

---
