# Boilerplate Django project.

Code is written for a series of articles:

1. ["Django with Poetry"](https://medium.com/@zalun/django-with-poetry-ea95bd5083f7)
2. ["Linting Django"](https://medium.com/django-unleashed/linting-django-9878c7ed8feb)
3. ["Lint and Test with GitHub Actions"](https://medium.com/django-unleashed/3-lint-and-test-with-github-actions-efa80197b303)
4. ["Deploy Django on DigitalOcean"](https://medium.com/@zalun/4-deploy-django-on-digitalocean-dc4b713e52c2)
5. ["3rd party authentication in Django"](https://medium.com/@zalun/base-5-3rd-party-authentication-in-django-887cad242a38)

## Installation

The system uses the following environment variables:

* `DEBUG` - Is the server in debug mode (default: `False`)
* `DATABASE_URL` - Postgresql database URL (default: `"sqlite"`)
* `SECRET_KEY` - A random string unique per installation (required)
* `GOOGLE_AUTH_CLIENT_ID` - Google OAuth client ID (required)
* `GOOGLE_AUTH_CLIENT_SECRET` - Google OAuth client secret (required)

Migrate the database:

```bash
$ poe migrate
Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, sessions, socialaccount
Running migrations:
  Applying account.0001_initial... OK
  Applying account.0002_email_max_length... OK
  Applying account.0003_alter_emailaddress_create_unique_verified_email... OK
  Applying account.0004_alter_emailaddress_drop_unique_email... OK
  Applying account.0005_emailaddress_idx_upper_email... OK
  Applying account.0006_emailaddress_lower... OK
  Applying account.0007_emailaddress_idx_email... OK
  Applying account.0008_emailaddress_unique_primary_email_fixup... OK
  Applying account.0009_emailaddress_unique_primary_email... OK
  Applying socialaccount.0001_initial... OK
  Applying socialaccount.0002_token_max_lengths... OK
  Applying socialaccount.0003_extra_data_default_dict... OK
  Applying socialaccount.0004_app_provider_id_settings... OK
  Applying socialaccount.0005_socialtoken_nullable_app... OK
  Applying socialaccount.0006_alter_socialaccount_extra_data... OK
```

To run it locally call `poe dev` and navigate to the <http://127.0.0.1:8001>.

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
