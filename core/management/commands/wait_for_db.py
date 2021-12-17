from _typeshed import Self
import time
from typing import Any, ClassVar, Optional
from django import db

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):


    '''command to pause db untill its available'''


    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        self.stdout.write('waiting for db')
        db_con=None

        while not db_con:

            try:
              db_con=connections['default']
            except OperationalError:
              self.stdout.write('db unavailable wait....')
              time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Connected'))
