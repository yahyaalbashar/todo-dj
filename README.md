<div align="center" styl="text-align: center">

<img src="./app/static/images/favicon.ico" height="100" alt="To Do App fevicon">

### To Do App

<p> A simple to do list app built with <a href="https://www.djangoproject.com/">Django</a> and <a href="https://www.postgresql.org/">PostgreSQL</a>. </p>
 
---
</div>

### Features

- Create a user account
- Create a to do list
- Edit tasks in the list
- Delete tasks from the list
- Mark tasks as complete
- Mark tasks as incomplete (default)
- Logout and login to your account on any device not just the one you created it on
- Change your user account password

### Tech Stack

- [Python v3.10.2](https://docs.python.org/3.10/)
- [Django v4.0.1](https://docs.djangoproject.com/en/4.0/)
- [Heroku-Postgres v13.5](https://www.heroku.com/postgres)

### Deployment on localhost

- With `existing PostgreSQL database`
  (follow [this](https://www.postgresql.org/docs/current/tutorial-install.html) for setting up a local PostgreSQL database)

1. Clone the repository

```
git clone https://github.com/HemantSachdeva/ToDoApp.git
```

2. Change current directory to the cloned repository
3. Run the following command to install all the dependencies

```
pip install -r requirements.txt
```

> **_Prequisites_**: Python must be installed on your machine to run pip command.

4. Rename the `change_this_to.env` file to `.env` and add your PostgreSQL database credentials

```
mv change_this_to.env .env
```

> **_NOTE:_** Make sure the `.env` file is in the root directory of the cloned repository and you fill the fields correctly.

5. Run following commands to make migrations, migrate the database, collect static file to the root and run the server

```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

- With `SQLite3 database`

Follow all the above 1 to 3 steps.

4. Rename the `change_this_to.env` file to `.env` and add your just add any SECRET_KEY you want for local use. (You can use any string you want and ignore other fields)

5. Open [project/settings.py](./project/settings.py) and change the following lines about database

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

to the following

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

6. Commands to run the localhost server with SQLite3 database are same as above mentioned for `PostgreSQL` in Step 5.

> **_NOTE:_** Everytime you run the server, login/register a new user and create a new to do list, everything will be saved in the [db.sqlite3](./db.sqlite3) database file. Make sure not to add the `db.sqlite3` file to the your commits for public/production use.

### Want to contribute to this project?

Follow the [Contributing Guide](./CONTRIBUTING.md)

---

Made with ❤ by [Hemant Sachdeva](https://github.com/HemantSachdeva)
