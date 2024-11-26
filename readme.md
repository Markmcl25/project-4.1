# **NewsSite**

NewsSite is a Reddit-style news aggregation platform where users can browse, create, vote, and comment on posts organized by categories. The platform also supports user profile customization with avatars.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Main Features](#main-features)
3. [Technologies Used](#technologies-used)
4. [Installation and Setup](#installation-and-setup)
5. [Database Configuration](#database-configuration)
6. [User Profile and Avatar](#user-profile-and-avatar)
7. [Deployment](#deployment)
8. [Project Structure Flowchart](#project-structure-flowchart)
9. [Author](#author)

---

## **Project Overview**

NewsSite is a full-stack web application that offers a seamless way for users to:
- Explore trending posts across multiple categories.
- Engage with posts by upvoting/downvoting or leaving comments.
- Add new posts with optional external source links and featured images.
- View content by category.
- Customize their profile with an avatar during signup.

---

## **Main Features**

- **Categories:** Posts are organized into categories like Health, Science, and Technology.
- **User Authentication:** Includes signup, login, logout, and profile management.
- **Content Interaction:** Users can vote on posts and add comments.
- **Post Creation:** Users can add new posts with a title, content, optional external links, and an image.
- **Responsive Design:** Optimized for mobile and desktop devices.

---

## **Technologies Used**

### **Frontend:**
- **HTML5, CSS3:** Markup and styling for a clean, user-friendly interface.
- **JavaScript:** For interactive features, including voting functionality.

### **Backend:**
- **Python + Django:** Framework for server-side logic and dynamic content rendering.
- **Relational Database:** PostgreSQL for production, SQLite3 for development.

### **Deployment:**
- **Heroku:** For hosting the application.
- **Cloudinary:** For media file storage.

---

## **Installation and Setup**

Follow the steps below to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Markmcl25/project-4.1.git
cd project-4.1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Use Postgres as the database. You can set up a local Postgres instance or use a managed Postgres database service.

- Update the DATABASE_URL in your .env file with your database credentials:

```bash
DATABASE_URL=postgres://<username>:<password>@<host>:<port>/<dbname>
```

- Run migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Set Up Cloudinary

This project uses Cloudinary for media storage. Create a Cloudinary account and get your API keys.

- Add the following to your .env file:

```bash
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```

### 5. Set Up Heroku

This project is configured to deploy on Heroku.

- Log in to Heroku:

```bash
heroku login
```