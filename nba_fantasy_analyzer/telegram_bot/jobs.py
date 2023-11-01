import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

from nba_fantasy_analyzer.espn.api import get_team_by_name, get_current_week
from nba_fantasy_analyzer.espn.usecases import process_team_weekly_data
from nba_fantasy_analyzer.utils.datetime import get_first_and_last_day_of_week


async def get_team_week_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    team_name = update.message.text

    team = get_team_by_name(team_name)
    current_week = get_current_week()
    first_day, last_day = get_first_and_last_day_of_week(datetime.date.today())

    team_in_json = process_team_weekly_data(team=team, current_week=current_week, first_day=first_day)
    team_in_json.pop("roster")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(team_in_json)
    )


def add_handlers(telegram_bot: ApplicationBuilder):
    team_handler = CommandHandler('team', get_team_week_status)
    telegram_bot.add_handler(team_handler)


