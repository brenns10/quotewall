Quote Wall
==========

This is a simple Flask web application that lets users post quotes to a "quote
wall". Upcoming features include:

- star ratings on quotes
- commenting on quotes
- more inside jokes

There are many CRUD webapps that can do this sort of thing. But this one is
mine.

Screenshots
-----------

### Main Page

![homepage](screenshots/homepage.png)

### Quote detail

![homepage](screenshots/detail.png)

Instructions
------------

The application needs to be installed with pip into a virtualenv.

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -e .
$ pip install -r requirements.txt

# Run shell in the application context
$ make shell

# Create your db and first user so you can log in.
In [1]: from quotewall.models.user import User
In [2]: from quotewall import db
In [3]: db.create_all()
In [4]: admin = User('username', 'email@example.com', 'password', 'Real Name')
In [5]: db.session.add(admin)
In [6]: db.session.commit()

# Run development server on localhost:5000
$ make run
```

Deployment
----------

I have written a docker file, and this application can be deployed with
`docker-compose`. The Makefile doesn't do everything, but it does automate a few
of the tasks.

```bash
# This will do the first build process and start the docker container running.
$ make docker-first-run

# After you make changes, you need to rebuild the image.
$ make docker-update

# You can stop everything with the following command.
$ docker-compose stop

# And start it back up again.
$ docker-compose start
```
