import logging
import time

from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--engine",
            choices=["django_rq", "celery"],
            default="celery",
            help="app which used for queue celery (default) / django_rq",
        )

    def handle(self, *args, **options):
        if options["engine"] == "django_rq":
            import django_rq

            django_rq.enqueue(set_timestamp)
        elif options["engine"] == "celery":
            from celery import shared_task

            @shared_task
            def task():
                set_timestamp()


def set_timestamp():
    if settings.django_queue_health is None:
        CommandError("django_queue_health not specified in settings.")
    setting = int(settings.django_queue_health)
    timestamp = time.time()
    cache.set(
        key="django_queue_health_TIMESTAMP",
        value=str(timestamp),
        timeout=setting * 60 * 6,
    )
    logger.info(f"Set timestamp {timestamp} in cache")
