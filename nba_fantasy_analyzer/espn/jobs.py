
import datetime

from nba_fantasy_analyzer.mongodb.settings import MONGODB_NAME, ALL_TEAMS_DAILY_DATA_COLLECTION, \
    ALL_TEAMS_WEEKLY_DATA_COLLECTION, MATCHUP_PREDICTION_ESPN_COLLECTION
from nba_fantasy_analyzer.mongodb.queries.general_queries import insert_one_document_query, insert_many_documents_query

from nba_fantasy_analyzer.espn.api import get_all_teams, get_current_week, get_current_matchups
from nba_fantasy_analyzer.espn.queries import get_one_team_weekly_score
from nba_fantasy_analyzer.espn.utils import get_team_expected_and_projected_points, transform_team_class_in_json
from nba_fantasy_analyzer.espn.usecases import process_team_weekly_data

from nba_fantasy_analyzer.utils.datetime import get_first_and_last_day_of_week


def save_all_team_daily_data():
    today = datetime.date.today()
    teams = get_all_teams()

    for team in teams:
        team_in_json = transform_team_class_in_json(team)
        team_in_json |= get_team_expected_and_projected_points(team=team, today=today)

        team_in_json |= {"date": today}

        insert_one_document_query(
            database=MONGODB_NAME, collection=ALL_TEAMS_DAILY_DATA_COLLECTION, data=team_in_json
        )


def save_all_teams_weekly_data():
    teams = get_all_teams()
    current_week = get_current_week()
    first_day, last_day = get_first_and_last_day_of_week(datetime.date.today())

    for team in teams:
        team_in_json = process_team_weekly_data(team=team, current_week=current_week, first_day=first_day)

        insert_one_document_query(
            database=MONGODB_NAME, collection=ALL_TEAMS_WEEKLY_DATA_COLLECTION, data=team_in_json
        )


def save_weekly_matchup_predictions():
    matchups = get_current_matchups()
    current_week = get_current_week()

    matchups_results = []
    considered_teams = []
    for matchup in matchups:
        if matchup["home_team"] in considered_teams:
            continue
        considered_teams.append(matchup["home_team"])
        considered_teams.append(matchup["away_team"])

        matchup_result = {}
        home_team_score = get_one_team_weekly_score(week=current_week, team_id=matchup["home_team"])
        away_team_score = get_one_team_weekly_score(week=current_week, team_id=matchup["away_team"])

        home_team_mean_score = (home_team_score["expected_points"] + home_team_score["projected_points"]) / 2
        away_team_mean_score = (away_team_score["expected_points"] + away_team_score["projected_points"]) / 2

        matchup_result["home_team"] = home_team_score
        matchup_result["away_team"] = away_team_score

        winner_team = "home_team" if home_team_mean_score > away_team_mean_score else "away_team"
        win_probability = 0.5 + abs(home_team_mean_score - away_team_mean_score) / (home_team_mean_score + away_team_mean_score)

        matchup_result["winner"] = matchup_result[winner_team]["team_name"]
        matchup_result["win_probability"] = win_probability

        matchups_results.append(matchup_result)

    insert_many_documents_query(
        database=MONGODB_NAME, collection=MATCHUP_PREDICTION_ESPN_COLLECTION, data=matchups_results
    )

