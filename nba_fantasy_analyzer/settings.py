"""
Settings for nba_fantasy_analyzer project.
"""
from pathlib import Path
import decouple

BASE_DIR = Path(__file__).resolve().parent.parent

config = decouple.AutoConfig(BASE_DIR)


NBA_API_KEY = config("NBA_API_KEY")
NBA_API_DAILY_LIMIT = config("NBA_API_DAILY_LIMIT")
NBA_FANTASY_MY_TEAM = config("NBA_FANTASY_MY_TEAM")
