import pprint
import re
import os
from django.db import connection
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils.module_loading import import_string
from django.conf import settings


class Command(BaseCommand):

    def handle(self, **options):
        self.drop_tables()
        #call_command('migrate')

        # initial_data_file = os.path.join(settings.BASE_DIR, 'fixtures', 'json', 'initial.json')
        # if os.path.exists(initial_data_file):
        #     call_command('loaddata', initial_data_file)
        # main_seeder = import_string(settings.FIXTURES_MAIN_SEEDER)
        # main_seeder.run()

    handle.short_description = u"Database reset"

    def drop_tables(self):
        cursor = connection.cursor()
        tables = connection.introspection.table_names()
        connection_driver = settings.DATABASES['default']['ENGINE']
        end_command = None
        if connection_driver == 'django.db.backends.sqlite3':
            cursor.execute('PRAGMA foreign_keys = OFF;')
            drop_table_command = 'DROP TABLE IF EXISTS %s;'
            end_command = 'PRAGMA foreign_keys = ON;'
        elif connection_driver == 'django.db.backends.postgresql':
            drop_table_command = 'DROP TABLE IF EXISTS %s CASCADE;'
        for table in tables:
            cursor.execute(drop_table_command % table)

        if end_command:
            cursor.execute(end_command)

    def flush_data(self):
        cursor = connection.cursor()
        tables = connection.introspection.table_names()
        cursor.execute('BEGIN;')
        for table in tables:
            if re.match(r'^django_\w+', table) is None:
                # pprint.pprint(table)
                try:
                    cursor.execute('DELETE FROM ' + table + ';')
                except Exception as e:
                    pprint.pprint(e.message)
        cursor.execute('COMMIT;')
