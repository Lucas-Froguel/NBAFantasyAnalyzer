
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from nba_fantasy_analyzer.mongodb.settings import MONGODB_NAME, MONGO_DATABASE_URL


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

