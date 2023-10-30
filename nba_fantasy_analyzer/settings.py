"""
Django settings for nba_fantasy_analyzer project.

Generated using django-split-settings, dj-database-url and python-decouple
"""
from pathlib import Path
import decouple

BASE_DIR = Path(__file__).resolve().parent.parent

config = decouple.AutoConfig(BASE_DIR)


MONGO_DATABASE_URL = config("MONGO_DATABASE_URL")
MONGODB_NAME = config("MONGO_DATABASE")
MONGO_MONGO_MY_TEAM_DATA_COLLECTION=config("MONGO_MY_TEAM_DATA")
MONGO_MONG_PLAYERS_DATA_COLLECTION=config("MONG_PLAYERS_DATA")

NBA_API_KEY = config("NBA_API_KEY")
NBA_API_DAILY_LIMIT = config("NBA_API_DAILY_LIMIT")
NBA_FANTASY_LEAGUE_ID = config("NBA_FANTASY_LEAGUE_ID")
NBA_FANTASY_SEASON_ID = config("NBA_FANTASY_SEASON_ID")
NBA_FANTASY_ESPNS2 = config("NBA_FANTASY_ESPNS2")
NBA_FANTASY_SWID = config("NBA_FANTASY_SWID")
NBA_FANTASY_MY_TEAM = config("NBA_FANTASY_MY_TEAM")
