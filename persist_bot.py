from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters,
)

# Replace this with your actual token securely
TOKEN = "7897481897:AAH8n7nGE4z6QYFRmG5dsi7YMehHNpf17E4"

# Define command handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Welcome to Persist Ventures write /help")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
    The following commands are available:

    /start -> Welcome to the channel
    /help -> This message
    /content -> Simplilearn offers various courses free of course through Skillup by Persist Ventures
    /Python -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Persist Ventures
    /contact -> Contact information
    """)

async def content(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("We have various playlists and articles available!")

async def python_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=rfscVS0vtbw")

async def sql_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=HXV3zeQKqGY")

async def java_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=A74TOX803D0")

async def skillup_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Visit: https://persistventures.com/")

async def contact(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("You can contact us via our official email.")

async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"You said: {update.message.text}. Use the commands starting with /")

# Main function
def main() -> None:
    # Create Application and pass in your bot's token
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("content", content))
    application.add_handler(CommandHandler("Python", python_command))
    application.add_handler(CommandHandler("SQL", sql_command))
    application.add_handler(CommandHandler("Java", java_command))
    application.add_handler(CommandHandler("Skillup", skillup_command))
    application.add_handler(CommandHandler("contact", contact))

    # Register a message handler for general text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
