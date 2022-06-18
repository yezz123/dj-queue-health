# dj-queue-health  - [![framework](https://img.shields.io/badge/Framework-Django-green?style)](https://www.djangoproject.com/)

Simple django app for checking queue health. Targeted to be used for Kubernetes deployments to periodically schedule `update_queue_timestamp` and set timestamp and verified by `test_queue_health` as a probe to verify if worker works and is not stacked.

## Installation

- Using pip:

```bash
pip install dj-queue-health
```

## Usage

- Add `dj_queue_health` to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
...,
"dj_queue_health",
]
```

- Add variable `django_queue_health` to your settings like this:

```python
# Minutes django_queue_health to check if there is queue log and if queue is running
django_queue_health = 10
```

- Configure default [django cache](https://docs.djangoproject.com/en/4.0/topics/cache/).
- Queue Health use [django rq](https://github.com/rq/django-rq) or [celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html).
- Use commands:

```bash

# Push job to queue that updates the timestamp

python manage.py update_queue_timestamp

# Check if timestamp in cache less than django_queue_health

python manage.py test_queue_health
```
