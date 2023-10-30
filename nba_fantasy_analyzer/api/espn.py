
from espn_api.basketball import League
from nba_fantasy_analyzer.settings import NBA_FANTASY_LEAGUE_ID, NBA_FANTASY_SEASON_ID, NBA_FANTASY_SWID, \
    NBA_FANTASY_ESPNS2


def get_my_team(my_team_name: str):
    league = League(
        league_id=NBA_FANTASY_LEAGUE_ID,
        year=int(NBA_FANTASY_SEASON_ID),
        espn_s2=NBA_FANTASY_ESPNS2,
        swid=NBA_FANTASY_SWID
    )
    my_team = None
    for team in league.teams:
        if team.team_name == my_team_name:
            my_team = team

    return my_team

