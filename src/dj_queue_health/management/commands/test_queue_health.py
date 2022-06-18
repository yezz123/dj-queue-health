import logging
import time

from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        setting = int(settings.django_queue_health)
        str_timestamp = cache.get("django_queue_health_TIMESTAMP")
        if str_timestamp is not None:
            timestamp = float(str_timestamp)
            treshold = float(setting * 60)
            down_time = time.time() - treshold
            if timestamp < down_time:
                raise CommandError(f"No queue log in last {setting} minutes.")
            logger.info(f"Queue log in last {setting} minutes.")
        else:
            logger.info(f"No queue log in last {setting} minutes.")
