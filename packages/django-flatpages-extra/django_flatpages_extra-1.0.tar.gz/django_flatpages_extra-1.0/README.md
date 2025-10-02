# Django Flatpages Extra 💅

A drop-in replacement for Django's `contrib.flatpages` with **extra 💅** features.


## Features

* **Drop-in replacement**: installing the app only requires 2 line changes, and optionally a management command.
* **Non-destructive**: no flatpage data is lost if you uninstall it.
* **Revisions**: direct edits to a page's content are forbidden in favor of creating page revisions.
* **Better history**: every revision has a detailed description, and a diff view to see exactly what changed.
* **Previews**: revisions can be previewed before they're published, and even shared via a private URL.
* **1-click revert**: once published, revisions can be reverted via a single click.


## Compatibility

`flatpages_extra` should compatible with all curently supported versions of Python and Django.


## Installation

First make sure the package is installed:
```bash
uv add django-flatpages-extra
```

Or if you're using `pip`:
```bash
pip install django-flatpages-extra
```

Then add `flatpages_extra` to your `settings.INSTALLED_APPS`, making sure it comes before `contrib.flatpages`:
```python
# settings.py
INSTALLED_APPS = [
    ...
    "flatpages_extra",
    "contrib.flatpages",
    ...
]
```

Finally, include the URL configuration. The exact path doesn't matter as long as it's reachable somewhere:
```python
# urls.py
urlpatters = [
    ...
    # Replace `flatpagesextra` with whatever you'd like:
    path("flatpagesextra/", include("flatpages_extra.urls")),
    ...
]
```

Once you've done all that, the app should be installed and running. Optionally you can run this command to import data from `contrib.flatpages`:
```bash
python manage.py flatpages_extra_import_initial
```

Running this command will do the following:

* create initial `Revision`s for all existing flatpages;
* copy the pages' history from `contrib.flatpages` (otherwise the "History" page in the admin would be empty);
* copy any custom `FlatPage` permission;
* copy user and group permissions.


## How to use it

`flatpages_extra` is meant to be used from the Django admin.
Once installed, it replaces Django's `contrib.flatpages` in the admin interface with its own (look for its signature 💅 emoji).

When you want to make changes to an existing page, create a new revision (the `FlatPage` change form will prompt you to do so).

Once a revision is created, you can make changes to it, preview it, and even share the preview link.

When you're happy with the changes, you can publish the revision via the "publish" button on the `Revision` changelist.

Publishing a revision will automatically update the related page's content and create a descriptive entry in that page's history.


## Configuration

`flatpages_extra` does not currently have any configurable options at the moment.


## How it works

`flatpages_extra` works by creating a [proxy model](https://docs.djangoproject.com/en/stable/topics/db/models/#proxy-models) to Django's original `FlatPage`, which lets us change how the model works in the admin while keeping the same database table.
It also adds a new `Revision` model that lets us preview, revert, and track changes to flat pages.
Both of those models are registered in the admin and will replace the original `contrib.flatpages` admin pages.
