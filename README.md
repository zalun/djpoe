# Boilerplate Django project.

Code is written for a series of articles:

1. ["Django with Poetry"](https://medium.com/@zalun/django-with-poetry-ea95bd5083f7)
2. ["Linting Django"](https://medium.com/django-unleashed/linting-django-9878c7ed8feb)
3. ["Lint and Test with GitHub Actions"](https://medium.com/django-unleashed/3-lint-and-test-with-github-actions-efa80197b303)
4. ["Deploy Django on DigitalOcean"](https://medium.com/@zalun/4-deploy-django-on-digitalocean-dc4b713e52c2)

## Installation

The system uses the following environment variables:

* `DEBUG` - Is the server in debug mode (default: `False`)
* `DATABASE_URL` - Postgresql database URL (default: `"sqlite"`)
* `SECRET_KEY` - A random string unique per installation (required)

To run it locally call `poe dev` and navigate to the http://127.0.0.1:8001

```bash
$ poe dev
Poe => python ./djpoe/manage.py runserver 127.0.0.1:8001
Watching for file changes with StatReloader
Performing system checks...

August 16, 2024 - 03:26:02
Django version 5.1, using settings 'djpoe.settings'
Starting development server at http://127.0.0.1:8001/
Quit the server with CONTROL-C.
```
