import datetime
import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    Defaults,
    MessageHandler,
    filters,
)

load_dotenv()
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


T2LOGSEQ_BOT_TOKEN = os.getenv("T2LOGSEQ_BOT_TOKEN")
T2LOGSEQ_JOURNALS_PATH = os.getenv("T2LOGSEQ_JOURNALS_PATH")
T2LOGSEQ_FILE_FORMAT = os.getenv("T2LOGSEQ_FILE_FORMAT")
T2LOGSEQ_TIME_FORMAT = os.getenv("T2LOGSEQ_TIME_FORMAT")
T2LOGSEQ_ADMIN_USERNAME = os.getenv("T2LOGSEQ_ADMIN_USERNAME")


async def retranslate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.username != T2LOGSEQ_ADMIN_USERNAME:
        return

    message_date = update.message.date
    current_file = f"{message_date.strftime(T2LOGSEQ_FILE_FORMAT)}.md"
    with open(os.path.join(T2LOGSEQ_JOURNALS_PATH, current_file), "a") as f:
        print("\n-", message_date.strftime(T2LOGSEQ_TIME_FORMAT), file=f)
        print("\t-", update.message.text, file=f)

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Got it")


if __name__ == "__main__":
    if not os.path.isdir(T2LOGSEQ_JOURNALS_PATH):
        print("Invalid journals path")
        os.exit(1)

    defaults = Defaults(tzinfo=datetime.datetime.now().astimezone().tzinfo)
    application = ApplicationBuilder().token(T2LOGSEQ_BOT_TOKEN).defaults(defaults).connect_timeout(1000).build()

    retranslate_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), retranslate)
    application.add_handler(retranslate_handler)

    application.run_polling()
