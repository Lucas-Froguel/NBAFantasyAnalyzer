import bson
import pytest
import mongomock
from mongomock.collection import Collection
from pandas import DataFrame
from pymongo.results import InsertOneResult, UpdateResult

from nba_fantasy_analyzer.exceptions import DatabaseError
from nba_fantasy_analyzer.mongodb.mongodb import MongoConnection


def test_get_db_status(fake, monkeypatch):
    db = "db"
    db_fake = mongomock.MongoClient()

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()
    with pytest.raises(DatabaseError) as e:
        mongo.get_db_status(db_name=db)

    assert isinstance(e.value, DatabaseError)


def test_get_db_collections(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()
    collection = db_fake.db.col
    objects = [
        dict(is_active=True, is_deleted=False),
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()

    response = mongo.get_db_collections(db_name=db)

    assert isinstance(response, list)
    assert response[0] is col


def test_get_db_collection(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()
    db_fake.db.col

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()

    response = mongo.get_db_collection(db_name=db, collection_name=col)

    assert isinstance(response, Collection)


def test_get_all_collection_documents(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()
    collection = db_fake.db.col
    objects = [
        dict(is_active=True, is_deleted=False),
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()

    response = mongo.get_all_collection_documents(db_name=db, collection_name=col)

    assert isinstance(response, list)
    assert response[0] == objects[0]


def test_insert_data(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()
    object = dict(
        is_active=True, is_deleted=False
    )

    monkeypatch.setattr("pandas.DataFrame.to_csv", lambda x: "")

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()

    response = mongo.insert_document(db_name=db, collection_name=col, document=object)
    assert isinstance(response, InsertOneResult)
    assert response.acknowledged is True


def test_bulk_insert_data(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()

    object = [
        dict(is_active=True, is_deleted=False),
    ]

    monkeypatch.setattr("pandas.DataFrame.to_csv", lambda x: "")

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient", lambda x: db_fake
    )

    mongo = MongoConnection().__enter__()

    response = mongo.bulk_insert_documents(db_name=db, collection_name=col, documents=object)
    assert response is None


def test_update_data(fake, monkeypatch):
    db = "db"
    col = "col"
    db_fake = mongomock.MongoClient()
    collection = db_fake.db.col
    objects = [
        dict(is_active=True, is_deleted=False),
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id
    query = {"_id": objects[0]["_id"], "is_active": True, "is_deleted": False}
    newvalue = {"$set": {"is_active": False, "is_deleted": True}}

    monkeypatch.setattr("pandas.DataFrame.to_csv", lambda x: "")

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.mongodb.pymongo.MongoClient",
        lambda x: mongomock.MongoClient(),
    )

    mongo = MongoConnection().__enter__()
    response = mongo.update_data(
        db_name=db, collection_name=col, filter=query, newvalues=newvalue
    )
    assert isinstance(response, UpdateResult)
    assert response.acknowledged is True
