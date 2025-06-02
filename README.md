# ArtifexLab API 🎨

---

**The brains behind the art.** 🧠
_A Django REST API powering a creative showcase platform._

---

A RESTful backend API built with Django REST Framework to power **ArtifexLab** — a creative hub where digital artists, designers, and creators can showcase their work, grow their skills, and connect with a supportive community.
At its heart, ArtifexLab is about collaboration and encouragement. Users can cheer each other on through likes and thoughtful comments, while mentors provide guidance and feedback to those engaging with tutorials. Whether you're here to share your passion, learn something new, or support fellow artists — **ArtifexLab** is built to help you thrive.

---

<details>
  <summary><strong>📚 Table of Contents</strong></summary>

- [Project Overview](#project-overview)

- [API Aims](#api-aims)

- [User Stories](#user-stories)

- [Database Schema](#database-schema)

- [Agile Development](#agile-development)

- [Features](#features)

- [Authentication & Permissions](#authentication--permissions)

- [Helpful Resources](#helpful-resources)

- [Future Enhancements](#future-enhancements)

- [Testing](#testing)

- [Deployment](#deployment)

- [Technologies Used](#technologies-used)

- [Credits](#credits)

- [Honourable Mentions](#honourable-mentions)

</details>

<br>
<div align="center">
  <a href="https://github.com/SamAtkinsonModeste/artifexlab-api/commits/main">
    <img src="https://img.shields.io/github/last-commit/SamAtkinsonModeste/artifexlab-api" alt="GitHub last commit">
  </a>
  <a href="https://github.com/SamAtkinsonModeste/artifexlab-api">
    <img src="https://img.shields.io/github/repo-size/SamAtkinsonModeste/artifexlab-api" alt="Repo size">
  </a>
  <a href="https://github.com/SamAtkinsonModeste/artifexlab-api/issues">
    <img src="https://img.shields.io/github/issues/SamAtkinsonModeste/artifexlab-api" alt="GitHub issues">
  </a>
  <img src="https://img.shields.io/badge/Built%20With-Django%20REST-092E20?logo=django" alt="Built With Django REST">
</div>

---

## Project Overview

The **ArtifexLab API** is the backend system behind a vibrant creative platform where users can share digital artwork, engage with community tutorials, and interact through likes, comments, and follows.

Built using **Django REST Framework**, the API handles secure authentication, user profile management, and full CRUD functionality for artworks and tutorials. It also supports custom feedback features and social interactions to encourage learning, growth, and mentorship within the creative community.

Designed to integrate seamlessly with the React-based frontend, this API provides a scalable and structured foundation that empowers creators to connect, inspire, and thrive.

---

## API Aims

The **ArtifexLab API** was developed to serve as the backend for a creative community platform. Its primary goals are:

- To manage user authentication and secure access to protected content
- To provide full CRUD (Create, Read, Update, Delete) functionality for:
  - Artworks uploaded by users
  - Tutorials created by mentors
  - User profiles and bios
  - Comments on artworks and tutorials
  - Like and favourite actions
- To enable social interactions through follows, likes, and comments
- To allow mentors to provide feedback on tutorial attempts submitted by users
- To deliver filtered and personalized content (e.g., artwork from followed users, favourited tutorials)
- To support learning and growth through structured tutorial content
- To integrate cleanly with the React-based frontend via RESTful endpoints

---

## User Stories

These user stories reflect the core functionality supported by the ArtifexLab API.

### As a **Registered User**, I can:

- Create an account, log in, and log out securely
- View a feed of artworks from all users or just those I follow
- Upload new artwork with images and captions
- Update or delete my own artworks
- View tutorials created by mentors
- Comment on both artworks and tutorials
- Like or unlike artworks
- Favourite or unfavourite tutorials
- Follow or unfollow other users
- Create and edit my user profile, including uploading a profile image and writing a bio
- Submit a tutorial attempt and receive feedback from a mentor

### As an **Unregistered User**, I can:

- Sign up for an account to access features and interact with the community

### As a **Mentor**, I can:

- Create, edit, or delete tutorials
- Create, edit or delete steps for my tutorials
- View and provide feedback on tutorial attempts submitted by users

### As a **Site Admin**, I can:

- Manage all content through the Django admin panel
- Moderate inappropriate content or user activity as needed

These user stories focus specifically on the backend API. Frontend functionality is handled in a separate repository.

---

📁 The frontend repository that connects with this API can be found here:
🔗 [ArtifexLab Frontend](https://github.com/SamAtkinsonModeste/artifexlab)

---

### 🔧 Core Technologies Used

- **Python 3.11** — Core programming language
- **Django** — High-level Python web framework
- **Django REST Framework** — Used to build the API
- **PostgreSQL** — Production database (via ElephantSQL)
- **Cloudinary** — Media hosting for user-uploaded images
- **dj-rest-auth** — Authentication and token handling
- **Heroku** — Platform for API deployment
- **CORS Headers** — Enables frontend-backend communication

---

### 🗂️ Database Schema

The ArtifexLab API is powered by a relational PostgreSQL database. The schema was designed using Luna Modeler, allowing for clear relationships between users, creative content, social interactions, and educational features.

It follows Django’s relational model structure, with one-to-many and many-to-one relationships across artworks, tutorials, tutorial attempts, and their associated likes, comments, and feedback. Each model is tightly scoped for clarity, scalability, and separation of concerns.

#### 🖼️ Schema Diagram

![Database Schema](docs/images/artifexlab-schema.png)

Schema diagram created with Luna Modeler and exported from the final database structure.

##### 🔑 Key Models Overview\*\*

**User** – Default Django user model storing account credentials

**Profiles** – Extends the User model with display name, image, and bio; used for linking to all user-created content

**Artworks** – Represents digital artwork submitted by users, including image, title, and description

**Likes Artwork / Comments Artwork** – Tracks likes and comments on individual artworks

**Tutorials** – Authored by mentors, these contain educational content including images and step-by-step instructions

**Tutorial Steps** – A breakdown of individual steps for each tutorial

**Tutorial Likes / Comments** – Enables user interaction with tutorial content

**Tutorial Attempts** – Stores submissions from users attempting tutorials, including optional images and written descriptions

**Tutorial Feedback** – Feedback left by mentors in response to tutorial attempts

**Tutorial Attempt Likes / Comments** – Lets users appreciate or comment on each other’s submissions

**Follows** – Tracks user-following relationships to power personalized feeds

This schema supports full CRUD functionality, detailed user interaction, and a mentorship workflow that encourages collaboration and growth in the ArtifexLab community.

[Creating a Base Serilizer](https://stackoverflow.com/questions/33137165/django-rest-framework-abstract-class-serializer?newreg=adb169505ce64135a559eed23d578f26)
[Creating Custom Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-base-classes)
[How to create Abstract Model Class in Django?](https://www.geeksforgeeks.org/how-to-create-abstract-model-class-in-django/)
[Docs: Django - Abstract base classes](https://docs.djangoproject.com/en/5.2/topics/db/models/#model-inheritance)
