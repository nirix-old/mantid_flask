Mantid
======

Mantid is a project manager and issue tracker powered by Flask and SQLAlchemy.

Requirements
------------

* Python
* A database
* SQLAlchemy
* Flask

Setup
------------

Rename the `settings.yml.default` to `settings.yml` and edit the database URL.

The URL is constructed like so:

    [database]://[username]:[password]@[server]/[database_name]

So a typical MySQL connection would be:

    mysql://myuser:mypass@localhost/mydatabase

Then all that's left to do is setup the database tables:

    python tables.py

Now you can start Mantid by simply running:

    python app.py
