import mongomock
from pymongo.results import InsertOneResult
from nba_fantasy_analyzer.mongodb.queries.general_queries import (
    get_one_document_query,
    insert_one_document_query,
    insert_many_documents_query,
)


def mock_bulk_insert_documents(*args, **kwargs):
    return []


def mock_bulk_insert_document(*args, **kwargs):
    class mock_mongo_obj:
        inserted_id = 1
    return mock_mongo_obj


def test_get_one_document_query(fake, monkeypatch):
    db = "db"
    col = "col"
    collection = mongomock.MongoClient().db.col

    objects = [
        dict(is_active=True, is_deleted=False),
    ]
    for obj in objects:
        obj["_id"] = collection.insert_one(obj).inserted_id
    query = {"_id": objects[0]["_id"], "is_active": True, "is_deleted": False}

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.queries.general_queries.MongoConnection.get_db_collection",
        lambda x, y, z: collection,
    )
    response = get_one_document_query(
        database=db, collection=col, query=query, convert_id=True
    )

    assert isinstance(response, dict)


def test_insert_one_document_query(fake, monkeypatch):
    db = "db"
    col = "col"
    collection = mongomock.MongoClient().db.col

    object = dict(is_active=True, is_deleted=False)

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.queries.general_queries.MongoConnection.insert_document",
        lambda *args, **kwargs: InsertOneResult,
    )
    response = insert_one_document_query(database=db, collection=col, data=object)

    assert response == str(InsertOneResult.inserted_id)


def test_bulk_insert_data_query(fake, monkeypatch):
    db = "db"
    col = "col"

    objects = [
        dict(is_active=True, is_deleted=False),
        dict(is_active=True, is_deleted=False),
    ]

    monkeypatch.setattr(
        "nba_fantasy_analyzer.mongodb.queries.general_queries.MongoConnection.bulk_insert_documents",
        mock_bulk_insert_documents,
    )
    response = insert_many_documents_query(database=db, collection=col, data=objects)

    assert response is None
