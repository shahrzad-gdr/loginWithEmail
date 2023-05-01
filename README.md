
# Django Email Login
This is a Django web application that provides email-based login and registration functionality. Upon successful registration, users are redirected to their dashboard, where they can view their information, including their first name, last name, and email address. Users can update their first name and last name on the dashboard page via a modal window.

# Getting Started
# Prerequisites
To run this project, you will need the following installed on your machine:

Python 3
Django 3 or higher

# Installation
Clone this repository to your local machine.
Navigate to the project directory in your terminal.
Run python manage.py migrate to create the necessary database tables.
Run python manage.py runserver to start the development server.

# Usage
When you run the development server, navigate to the homepage at http://localhost:8000/. The homepage has two links: "Login" and "Register". Click "Register" to create a new account.

When you register successfully, you will be redirected to your dashboard. You can view your information on the dashboard page, and update your first name and last name by clicking the "Update" button. A modal window will open allowing you to edit your details. Note that the email address is a readonly field and cannot be changed.

To log in, click the "Login" link on the homepage and enter your email and password. Once you are logged in, you can access your dashboard and update your details.

This project uses Django's built-in @login_required decorator to ensure that users must be logged in to access the dashboard. It also uses the messages library to display simple and direct messages to the user, for example if passwords do not match during registration or if an email address is not unique.

# Static Files
This project also includes static files that demonstrate how to use static URLs in Django. There are two images on the homepage that are loaded from static URLs.


# Note
There are images in documentation directory.
