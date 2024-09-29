# Boilerplate Django project

Code is written for a series of articles:

1. ["Django with Poetry"](https://medium.com/@zalun/django-with-poetry-ea95bd5083f7)
2. ["Linting Django"](https://medium.com/django-unleashed/linting-django-9878c7ed8feb)
3. ["Lint and Test with GitHub Actions"](https://medium.com/django-unleashed/3-lint-and-test-with-github-actions-efa80197b303)
4. ["Deploy Django on DigitalOcean"](https://medium.com/@zalun/4-deploy-django-on-digitalocean-dc4b713e52c2)
5. ["3rd party authentication in Django"](https://medium.com/@zalun/base-5-3rd-party-authentication-in-django-887cad242a38)
6. ["Wagtail CMS for the content"](https://medium.com/@zalun/base-6-wagtail-cms-for-the-content-f60d8ec7ac9e)

## Installation

### Set variables

The system uses the following environment variables. Some of them are required.

* `DEBUG` - Is the server in debug mode (default: `False`)
* `DATABASE_URL` - Ddatabase URL (default: `"sqlite:///djpoe/db.sqlite3"`)
* `SECRET_KEY` - A random string unique per installation (required)
* `ACCOUNT_AUTHENTICATION_METHOD` - (default: `"email"`)
* `ACCOUNT_EMAIL_REQUIRED` - (default: `True`)
* `GOOGLE_AUTH_CLIENT_ID` - Google OAuth client ID (required)
* `GOOGLE_AUTH_CLIENT_SECRET` - Google OAuth client secret (required)
* `WAGTAIL_SITE_NAME` - Name used in the CMS (deefault: `"DJPoe"`)
* `WAGTAILADMIN_BASE_URL` - URL used in Wagtail notifications (default: `"http://localhost:8001"`)
* `DEFAULT_FROM_EMAIL` - Email used as author of Django emails (default: `"email@example.com"`)

### Migrate the database

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
  ... A lot of wagtail migrations
```

### Add homepage from fixture

```bash
$ poe manage loaddata homepage
Poe => python ./djpoe/manage.py loaddata homepage
Installed 4 object(s) from 1 fixture(s)
```

### Run locally

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

### Deployment

Look into ["Deploy Django on DigitalOcean"](https://medium.com/@zalun/4-deploy-django-on-digitalocean-dc4b713e52c2)
and modify the GitHub variables accordingly.
