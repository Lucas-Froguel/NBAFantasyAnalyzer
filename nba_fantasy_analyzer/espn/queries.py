
from nba_fantasy_analyzer.mongodb.settings import MONGODB_NAME, ALL_TEAMS_WEEKLY_DATA_COLLECTION
from nba_fantasy_analyzer.mongodb.queries.general_queries import get_many_documents_query, get_one_document_query


def get_all_teams_weekly_data(week: int) -> dict:
    query = {
        "week": week
    }
    projection = {
        "_id": False,
        "team_id": True,
        "team_name": True,
        "expected_points": True,
        "projected_points": True,
    }

    data = get_many_documents_query(
        database=MONGODB_NAME, collection=ALL_TEAMS_WEEKLY_DATA_COLLECTION, query=query, projection=projection
    )

    return data


def get_one_team_weekly_score(week: int = None, team_id: int = None) -> dict:
    query = {
        "week": week,
        "team_id": team_id
    }
    projection = {
        "_id": False,
        "team_name": True,
        "expected_points": True,
        "projected_points": True,
    }

    data = get_one_document_query(
        database=MONGODB_NAME, collection=ALL_TEAMS_WEEKLY_DATA_COLLECTION, query=query, projection=projection
    )

    return data
