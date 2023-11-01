import datetime
from espn_api.basketball import Team
from nba_fantasy_analyzer.espn.utils import transform_team_class_in_json, get_team_expected_and_projected_points


def process_team_weekly_data(team: Team = None, current_week: int = None, first_day: datetime.date = None):
    team_in_json = transform_team_class_in_json(team)
    team_in_json |= {"week": current_week}
    team_cumulative_points = {
        "expected_points": 0,
        "projected_points": 0
    }
    for k in range(7):
        day = first_day + datetime.timedelta(days=k)
        team_points = get_team_expected_and_projected_points(
            team=team, today=day, consider_be_out=False
        )
        team_cumulative_points[f"day{k}"] = team_points
        team_cumulative_points["expected_points"] += team_points["expected_points"]
        team_cumulative_points["projected_points"] += team_points["projected_points"]

    team_in_json |= team_cumulative_points

    return team_in_json
