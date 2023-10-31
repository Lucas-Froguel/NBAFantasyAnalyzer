
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger

from nba_fantasy_analyzer.settings import MONGODB_NAME, MONGO_DATABASE_URL
from nba_fantasy_analyzer.jobs.espn import save_all_team_daily_data, save_weekly_matchup_predictions, \
    save_all_teams_weekly_data


jobstores = {
    'default': MongoDBJobStore(
        database=MONGODB_NAME, host=MONGO_DATABASE_URL
    )
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.start()

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

