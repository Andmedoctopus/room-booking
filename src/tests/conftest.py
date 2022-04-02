import pytest
import pytest_factoryboy

from tests.factories import __all_facotories__
from room_booking.webapp import init_dependency

for factory_implementation in __all_facotories__:
    pytest_factoryboy.register(factory_implementation)

@pytest.fixture(scope='session')
def di():
    with init_dependency() as di:
        yield di

@pytest.fixture
def datasource(di):
    return di.resources.datasource()

@pytest.fixture(scope="function", autouse=True)
def transaction_rollback(datasource):
    with datasource.open_connection() as connection:
        with connection.begin_nested() as nested:
            yield
            nested.rollback()

@pytest.fixture
def room_repository(di):
    return di.repositories.room()

