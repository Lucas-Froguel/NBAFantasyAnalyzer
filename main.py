
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler

from nba_fantasy_analyzer.app_scheduler.settings import jobstores, executors, job_defaults
from nba_fantasy_analyzer.app_scheduler.jobs import add_jobs_to_scheduler

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
add_jobs_to_scheduler(scheduler)
scheduler.start()

