import os

class DatabaseConfiguration(object):
    def __init__(self, env):
        self.env = env

    def connection_string(self):
        connection_string_template = 'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
        return connection_string_template.format(**self._configuration())

    def _configuration(self):
        config = {
            'db_name': self.env.get('DB_NAME'),
            'db_host': self.env.get('DB_HOST'),
            'db_user': self.env.get('DB_USER'),
            'db_password': self.env.get('DB_PASSWORD')
        }
        if any(config_value == None for config_value in config.values()):
            message = 'Database not configured. Refer to .env.example'
            raise DatabaseNotConfiguredException(message)
        else:
            return config

class DatabaseNotConfiguredException(Exception):
    pass
