Flask-Bootstrap
---

Is a skeleton of a "Large" Flask application with the integration of Twitter bootstrap.


Initialize db
---

Set the db parameters in the default_settings.py or in the production.cfg file and then go to the interactive python shell and run:

* \>>> from application import db
* \>>> db.create_all()

***note: You must first create the database in Postgresql***

Changelog
---

**v0.1 / 2012/12/22**
  * Create Flask-Bootstrap skeleton.
  * Add Twitter bootstrap 2.2.2 to project.
  * Add SQLAlchemy to default skeleton.

ToDo
---

* Add db create.
* Add css and js bootstrap files.
* Add template.
* Add Tests folder & actions.