def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES = {
        'default': {
        'ENGINE': 'db_engine',
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
            }
        }
    )
    django.setup()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()