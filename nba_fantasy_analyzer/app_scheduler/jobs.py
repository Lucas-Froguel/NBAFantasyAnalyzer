from apscheduler.triggers.cron import CronTrigger

from nba_fantasy_analyzer.espn.jobs import save_all_team_daily_data, save_weekly_matchup_predictions, \
    save_all_teams_weekly_data


def add_jobs_to_scheduler(scheduler):
    scheduler.add_job(
        save_all_team_daily_data,
        trigger=CronTrigger(month="*", week="*", day_of_week="*", hour="16"),
        replace_existing=True,
        id="save_all_team_daily_data_espn"
    )
    scheduler.add_job(
        save_all_teams_weekly_data,
        trigger=CronTrigger(month="*", week="*", day_of_week="1", hour="6"),
        replace_existing=True,
        id="save_all_teams_weekly_data_espn"
    )
    scheduler.add_job(
        save_weekly_matchup_predictions,
        trigger=CronTrigger(month="*", week="*", day_of_week="1", hour="8"),
        replace_existing=True,
        id="save_weekly_matchup_predictions_espn"
    )
