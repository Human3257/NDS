import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите число")

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = float(update.message.text)
        result = 12 / 112 * user_input
        await update.message.reply_text(f"{user_input} = {result}")
    except ValueError:
        await update.message.reply_text("Пожалуйста, введи корректное число.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    print("Бот запущен...")
    app.run_polling()
