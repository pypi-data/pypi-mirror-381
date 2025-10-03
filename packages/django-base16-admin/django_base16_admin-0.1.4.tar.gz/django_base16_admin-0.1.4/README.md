# django-base16-admin

🎨 Base16 color themes for Django Admin.\
Includes multiple themes with easy setup, live previews, and ready-to-use CSS files.

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
[base16_admin/static/admin/themes/](/src/base16_admin/static/admin/themes/).

3. Run `collectstatic` (prod):

```bash
python manage.py collectstatic
```

4. Start your project and enjoy your new admin look 🎉

## Available Themes

Here are the currently available Base16 themes for Django Admin:

| Theme Name       | Key                | Preview                                      | Theme CSS                                                                            |
| ---------------- | ------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------ |
| Circus           | `circus`           | [Preview](/docs/assets/circus.png)           | [`circus.css`](/src/base16_admin/static/admin/themes/circus.css)                     |
| Cupcake          | `cupcake`          | [Preview](/docs/assets/cupcake.png)          | [`cupcake.css`](/src/base16_admin/static/admin/themes/cupcake.css)                   |
| Tokyo City Dark  | `tokyo-city-dark`  | [Preview](/docs/assets/tokyo-city-dark.png)  | [`tokyo-city-dark.css`](/src/base16_admin/static/admin/themes/tokyo-city-dark.css)   |
| Tokyo City Light | `tokyo-city-light` | [Preview](/docs/assets/tokyo-city-light.png) | [`tokyo-city-light.css`](/src/base16_admin/static/admin/themes/tokyo-city-light.css) |

## Contributing

Contributions are welcome!\
Feel free to open issues or submit PRs for new Base16 themes or improvements.

## License

[MIT](LICENSE) Copyright (c) [stabldev](https://github.com/stabldev)
