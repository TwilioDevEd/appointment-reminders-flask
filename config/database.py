import os

class DatabaseConfiguration(object):
    def connection_string(self):
        connection_string_template = "postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
        return connection_string_template.format(**self._configuration())

    def _configuration(self):
        return {
            'db_name': os.environ.get('DB_NAME'),
            'db_host': os.environ.get('DB_HOST'),
            'db_user': os.environ.get('DB_USER'),
            'db_password': os.environ.get('DB_PASSWORD')
        }
