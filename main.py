
from pytz import utc
from telegram.ext import ApplicationBuilder
from apscheduler.schedulers.background import BackgroundScheduler

from nba_fantasy_analyzer.app_scheduler.settings import jobstores, executors, job_defaults
from nba_fantasy_analyzer.app_scheduler.jobs import add_jobs_to_scheduler

from nba_fantasy_analyzer.telegram_bot.settings import TELEGRAM_BOT_KEY
from nba_fantasy_analyzer.telegram_bot.jobs import add_handlers

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
add_jobs_to_scheduler(scheduler)
scheduler.start()

telegram_bot = ApplicationBuilder().token(TELEGRAM_BOT_KEY).build()
add_handlers(telegram_bot)
telegram_bot.run_polling()

