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

## 🧪 Create and Activate a Virtual Environment

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

👉 Add env.py to your `.gitignore` file so it never gets pushed to GitHub
This keeps your private data private 🔐

---

---

## 📦 3. Install Project Dependencies

Once your virtual environment is activated, it’s time to install the packages your Django project needs to run — both locally and on Heroku.

Here’s what I used and why ⬇️

### ✅ Install core dependencies:

```bash
pip install django<4 gunicorn dj_database_url psycopg2 django-cloudinary-storage
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

## 🏗️ Project Setup

### 1. Start the Django Project and First App

With your virtual environment active and dependencies installed, it’s time to get Django up and running 🎉

From your terminal in VSCode, run the following command to create your project:

```bash
django-admin startproject artlab_api .
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

### 2. Apply Migrations & Run the Server

**Once the project and your first app are created, it’s time to let Django set up the database 🧱**

**In the terminal, run:**

```bash
python manage.py migrate
```

This applies the initial built-in migrations (like users, admin, sessions, etc.) so Django can create the default database structure.

Then fire up the development server:

```bash
python manage.py runserver

```

You should see the familiar message that Django is running on http://127.0.0.1:8000/.
Click the link or paste it in your browser to see the welcome screen — your project is officially alive! 🎉

### 🔐 Authentication Setup

To handle user accounts, login, and secure access to the API, I used:

- **dj-rest-auth** - for registration, login, logout, and password reset

- **simplejwt** - for JSON Web Token (JWT) support

- **allauth (auto-installed with dj-rest-auth)** - to handle account logic like email validation

#### 🔧 JWT Cookie Settings

I used cookie-based JWT tokens to keep things secure and frontend-friendly.

In settings.py, I added:

```python
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

```

These settings allow the frontend to securely store tokens in browser cookies instead of localStorage.

#### 👤 Current User Serializer

To give the frontend access to the current user’s profile ID and profile image, I created a custom serializer called CurrentUserSerializer.

Then I overrode the default like this:

```python
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'artlab_api.serializers.CurrentUserSerializer'
}
```

📝 Replace your_project with the actual folder name where your custom serializer lives.

This makes sure the logged-in user data returned from the API includes both their profile ID (needed for linking content) and profile image (handy for UI display).

---

### 🛤️ Add a Root Route to the API

To make the API feel more welcoming (especially for first-time visitors), I added a simple root route that returns a friendly message.

##### ✅ Steps:

1. In your project folder, create a new file if it doesn’t exist already:
   your_project/views.py

2. Inside views.py, add:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({"message": "Welcome to my Django REST Framework API!"})

```

3. Then open your urls.py and:

- Import the view at the top:

```python
from .views import root_route

```

- Add the path to your urlpatterns list:

```python
path('', root_route),

```

Now when someone visits your Heroku backend root URL, they’ll see your welcome message instead of a blank page ✨

---

## 📚 Pagination & JSON Renderer Setup

To improve the API experience, I added pagination (so large datasets are broken into pages), and set the JSON renderer for production.

Open settings.py and scroll to where your REST_FRAMEWORK settings are defined. Then update it like this:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

```

✅ What this does:

Adds default pagination (10 results per page)

Ensures consistent datetime formatting like 03 Jun 2025

Switches to JSON output only when the site is live (to reduce unnecessary renderer options)

---

## 🌐 PostgreSQL Setup

### 1. Hosted PostgreSQL via Code Institute

For production, I used **PostgreSQL** instead of SQLite (which is only suitable for development).

As a Code Institute student, I was provided with a free, hosted PostgreSQL instance.
Once it was created, I copied the `DATABASE_URL` from the CI backend form — this string includes all the credentials needed to connect Django to the hosted database.

---

### 2. Connect PostgreSQL in `settings.py`

To plug the hosted database into Django, I updated my `DATABASES` setting like this:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

This tells Django to look for the DATABASE_URL in your environment variables — which Heroku will automatically provide if you’ve set it in your Config Vars.

### ☁️ Cloudinary Media Storage

Instead of storing user-uploaded images locally (which doesn’t work well with Heroku), I used Cloudinary to host all media files — like profile pictures, artwork images, etc.

#### ✅ Steps Taken:

- Installed the Cloudinary package (already covered in the dependencies section ✅)

- Created a free Cloudinary account

- Added the CLOUDINARY_URL to Heroku Config Vars

Then I updated my settings to tell Django where to store uploaded media:

```python
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

```

This ensures that all images uploaded by users are automatically stored in the cloud instead of trying to save to Heroku (which wipes your filesystem every time you redeploy).

📌 You’ll also want to set up your media/ path and make sure it's not ignored in development, depending on your DEBUG setting.

---

## 🌍 CORS Setup for Frontend Connection

To allow your frontend (hosted on a different domain) to talk to your Django backend, you’ll need to configure
**CORS** (Cross-Origin Resource Sharing) in `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [os.environ.get("CLIENT_ORIGIN")]
CORS_ALLOW_CREDENTIALS = True
JWT_AUTH_SAMESITE = 'None'
```

This allows credentials like JWT cookies to be sent securely across domains.

---

## ⚙️ Heroku Deployment (Backend)

### 1. Create a Heroku App

To deploy your Django backend to Heroku:

1. Go to [https://dashboard.heroku.com](https://dashboard.heroku.com)
2. Click the **“New”** dropdown button (top right), then select **“Create new app”**
3. Give your app a unique name (e.g. `artifexlab-api`)
4. Choose your region (I used Europe)
5. Click **“Create app”**

That sets up your Heroku app — ready for configuration and deployment.

---

### 2. Connect to GitHub

Instead of using the Heroku CLI, I connected my GitHub repo directly:

1. Go to your app’s **Deploy** tab
2. Under **Deployment method**, choose **GitHub**
3. Authorize access (if prompted), then search for your repo (e.g. `artifexlab-api`)
4. Click **Connect**

Once connected, you can either enable **Automatic Deploys** from the `main` branch or click **Deploy Branch** manually when you're ready.

---

### 3. Add Heroku Config Vars

Go to the **Settings** tab → click **Reveal Config Vars** and add the following:

| Key                     | Value (example)                       |
| ----------------------- | ------------------------------------- |
| `DATABASE_URL`          | From CI PostgreSQL or your own host   |
| `SECRET_KEY`            | Your Django secret key                |
| `CLOUDINARY_URL`        | From your Cloudinary account          |
| `DISABLE_COLLECTSTATIC` | `1` (only needed before first deploy) |

---

### 4. Add a `Procfile`

At the root of your backend repo (same level as `manage.py`), add a file called `Procfile` (no extension). Inside, add:

```Procfile
release: python manage.py migrate
web: gunicorn artlab_app.wsgi
```

**📝 Replace your_project_name with the name of the folder that contains your** settings.py.
_In my case that is artlab_api, however you could name your project anything you like that reflects your project._

### 5. Deploy from GitHub

**Now go back to the Deploy tab in Heroku:**

- Make sure your deployment method is GitHub

- Scroll down to **Manual deploy**

- Choose the branch (usually main) and click Deploy Branch

🎉 Heroku will build your app and let you know once it’s live!

🔙 [Back to README](./README.md)
