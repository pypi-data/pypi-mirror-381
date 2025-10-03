# django-base16-admin

🎨 Base16 color themes for Django Admin.

## Installation

```bash
pip install django-base16-admin
# uv add django-base16-admin
```

## Usage

1. Add `base16_admin` before `django.contrib.admin` in your `INSTALLED_APPS`:

```py
INSTALLED_APPS = [
    "base16_admin",  # must come first
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    ...
]
```

2. (Optional) Choose a theme in your Django settings.py:

```py
BASE16_THEME = "circus"  # default = "circus"
```

Available themes are stored in  
[base16_admin/static/base16_admin/themes/](/src/base16_admin/static/base16_admin/themes/).

3. Run `collectstatic` (prod):

```bash
python manage.py collectstatic
```

4. Start your project and enjoy your new admin look 🎉

## Contributing

Contributions are welcome!  
Feel free to open issues or submit PRs for new Base16 themes or improvements.

## License

[MIT](LICENSE) Copyright (c) [stabldev](https://github.com/stabldev)
