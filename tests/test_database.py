from config.database import DatabaseConfiguration, DatabaseNotConfiguredException
import pytest

def test_correct_configuration():
    env = {'DB_NAME': 'eels', 'DB_HOST': 'wall-e:5432',
           'DB_USER': 'captain', 'DB_PASSWORD': 'kirk'}
    dbconfig = DatabaseConfiguration(env)

    assert dbconfig.connection_string() == 'postgresql://captain:kirk@wall-e:5432/eels'

def test_broken_configuration():
    env = {'ship': 'flying dutchman'}
    dbconfig = DatabaseConfiguration(env)

    with pytest.raises(DatabaseNotConfiguredException):
        dbconfig.connection_string()
