from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
from datetime import datetime

BOT_TOKEN = "7631993904:AAEY6zWrEpwl3eGjVyhCHTLKV5Ec-3djo1s"

# Greet based on time
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 18:
        return "Good Afternoon 🌤️"
    else:
        return "Good Evening 🌙"

# Show options keyboard
def get_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton("📺 YouTube"), KeyboardButton("💼 LinkedIn")],
        [KeyboardButton("📧 Gmail"), KeyboardButton("📰 News")],
        [KeyboardButton("ℹ️ Help"), KeyboardButton("❌ Exit")]
    ], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"{get_greeting()}, {user.first_name}! 👋\nI'm your friendly Telegram bot.\n\nChoose an option below:",
        reply_markup=get_keyboard()
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available Commands:\n/start\n/help\nOr click an option below ⬇️")

async def respond_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "youtube" in text:
        await update.message.reply_text("📺 https://youtube.com/")
    elif "linkedin" in text:
        await update.message.reply_text("💼 https://linkedin.com/")
    elif "gmail" in text:
        await update.message.reply_text("📧 https://mail.google.com/")
    elif "news" in text:
        await update.message.reply_text("📰 https://news.google.com//")
    elif "help" in text:
        await help_command(update, context)
    elif "exit" in text:
        await update.message.reply_text("Goodbye! 👋 Type /start to begin again.")
    else:
        await update.message.reply_text("❓ I didn’t understand that. Try using the buttons or type /help.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_text))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
