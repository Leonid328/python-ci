import os
import tempfile

import db


def setup_function():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    db.db.init(path)
    db.db.connect()
    db.db.create_tables([db.ProductModel], safe=True)
    db._add_default_data()


def teardown_function():
    db.db.close()


def test_default_products_count():
    assert db.ProductModel.select().count() == 5


def test_create_and_get():
    p = db.create_product("Eggs", 12)
    found = db.get_product_by_id(p.id)
    assert found is not None
    assert found.name == "Eggs"


def test_update_product():
    p = db.create_product("Tea", 10)
    db.update_product(p.id, name="Green tea", price=15)
    found = db.get_product_by_id(p.id)
    assert found.name == "Green tea"
    assert found.price == 15


def test_delete_product():
    p = db.create_product("Temp", 1)
    assert db.delete_product(p.id) is True
    assert db.get_product_by_id(p.id) is None
