# Description
<p>In this project, it is aimed to create an application where personnel users can create blogs, update, delete or read the blogs they have created. Users without staff features will be able to read all published blogs. We also used class-based views to create custom functions and override some methods.📃</p>

# Models

- Blog
- Category
- User
- Comment
- PostViews
- Likes

![Model](https://github.com/sultankeles/django_blog_app/blob/main/blog_app_erd.png)

# Category

    - Client_User
        - view category only

    - Staff_User
        - CRUD department

# Blog

    - Client_User
        - view blog only

    - Staff_User
        - CRUD blog (their own blog)

<!-- # Live Project

- <a href="https://pakize.pythonanywhere.com/">Live of the project</a>
- <a href="https://pakize.pythonanywhere.com/swagger/">For the swagger of the project</a> -->

# Project Installation

<p>Here's an example of how you can instruct your audience to download and install your app. This template is not based on any external dependencies or services.</p>

1- Python venv installation: <br>
python -m venv <venv_name>

2- env activation: <br>
Powershell => .\<venv_name>\Scripts\activate <br>
bash => source <venv_name>/Scripts/Activate

3- Install packages: <br>
pip install -r requirements.txt

4- For database: <br>
python manage.py migrate

5- .env file: <br>
    SECRET_KEY= <br>
    DEBUG=True <br>
    SQL_DATABASE=docker_django <br>
    SQL_USER= <br>
    SQL_PASSWORD= <br>
    SQL_HOST=db <br>
    SQL_PORT=5432

6- Create user for Admin Panel. <br>
python manage.py createsuperuser

7- The project is ready, you can start using it now. <br>
python manage.py runserver

Runs the application in development mode. To view in the browser http://127.0.0.1:8000/
open.