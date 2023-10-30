
from nba_fantasy_analyzer.api.espn import get_my_team_players
from nba_fantasy_analyzer.settings import NBA_FANTASY_MY_TEAM

my_team = get_my_team_players(NBA_FANTASY_MY_TEAM)
print(my_team)
