from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота (убедитесь, что он правильный)
TOKEN = "8185165520:AAFCEpH2YTilmhh5gX9bVhqoFc4XbJIzK9A"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с кнопкой."""
    keyboard = [[InlineKeyboardButton("Нажми меня", callback_data='hello')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Пожалуйста, нажмите кнопку:', reply_markup=reply_markup)


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает нажатие на кнопку."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Привет!")


def main() -> None:
    """Запуск бота."""
    # Явно указываем использование UTC, чтобы избежать проблем с часовыми поясами
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()


if __name__ == '__main__':
    main()
'''

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Явно устанавливаем часовой пояс
scheduler = AsyncIOScheduler(timezone=pytz.UTC)

BOT_TOKEN = "8185165520:AAFCEpH2YTilmhh5gX9bVhqoFc4XbJIzK9A"
GROUP_CHAT_ID = "-4623466305"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text="Привет!")

async def main():
    # Создаем Application с явным указанием scheduler
    application = Application.builder() \
        .token(BOT_TOKEN) \
        .scheduler(scheduler) \
        .build()

    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
'''