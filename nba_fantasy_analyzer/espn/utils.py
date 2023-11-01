from datetime import date
from espn_api.basketball import Team, Player


def get_team_expected_and_projected_points(team: Team = None, today: date = None, consider_be_out: bool = True) -> float:
    # TODO:
    # get realized points as well
    projected_points = 0
    expected_points = 0
    for player in team.roster:
        if check_if_player_will_play_today(player=player, today=today, consider_be_out=consider_be_out):
            projected_points += player["projected_avg_points"]
            expected_points += player["avg_points"]

    points_data = {
        "projected_points": projected_points,
        "expected_points": expected_points
    }

    return points_data


def check_if_player_will_play_today(player: Player = None, today: date = None, consider_be_out: bool = True) -> bool:
    positions_out = ["IR", "BE"] if consider_be_out else ["IR"]
    player_will_play = player["lineupSlot"] not in positions_out or not player["injured"]
    if not player_will_play:
        return player_will_play

    for game in player["schedule"].values():
        if game["date"].date() == today:
            return player_will_play

    player_will_play *= False
    return player_will_play


def transform_team_class_in_json(team: Team):
    team_in_json = vars(team)
    team_in_json.pop("schedule")
    roster = team_in_json.pop("roster")
    roster_in_json = [
        vars(player)
        for player in roster
    ]

    team_in_json["roster"] = roster_in_json

    return team_in_json
