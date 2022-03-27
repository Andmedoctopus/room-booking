import pytest
import pytest_factoryboy

from tests.factories import __all_facotories__
from room_booking.webapp import init_dependency

for factory_implementation in __all_facotories__:
    pytest_factoryboy.register(factory_implementation)

@pytest.fixture
def di():
    return init_dependency()

@pytest.fixture
def datasource(di):
    return di.resources.datasource()

@pytest.fixture(scope="function", autouse=True)
def transaction_rollback(datasource):
    with datasource.open_transaction() as transaction:
        yield
        transaction.rollback()

@pytest.fixture
def room_repository(di):
    return di.repositories.room()

