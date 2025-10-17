from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# =====================
# Bot Configuration
# =====================
BOT_TOKEN = "8331836488:AAHRRCPePtRrAdgJyUWwSOrGqqfmWH0gR1g"
GROUP_LINK = "https://t.me/+JPbwhQwSfiBlN2Q1"
CONTACT = "@shahi_vai"
BANNER_URL = "https://i.ibb.co/ccvRwVBr/Gemini-Generated-Image-luotytluotytluot.png"  # direct image URL

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    username = update.effective_user.username

    # Personalized greeting
    if username:
        greet_name = f"{user_first_name} (@{username})"
    else:
        greet_name = f"{user_first_name}"

    # Buttons
    keyboard = [
        [InlineKeyboardButton("✅ JOIN", url=GROUP_LINK)],
        [InlineKeyboardButton("💥 JOINED", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Caption text
    text = f"""
📢 Hello!!! Scammer🤨 {greet_name}! 👋

Contact - {CONTACT}
Join our channel, click JOIN ✅
Then press JOINED after joining to /start chatting 💬
"""

    # Send banner picture
    await update.message.reply_photo(
        photo=BANNER_URL,          # Picture উপরে
        caption=text,              # Caption picture এর নিচে
        parse_mode="Markdown",
        reply_markup=reply_markup  # Buttons caption এর নিচে
    )

# JOINED button click
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    try:
        chat_member = await context.bot.get_chat_member(chat_id=GROUP_LINK, user_id=user_id)
        if chat_member.status in ["member", "administrator", "creator"]:
            await query.message.reply_text(f"🎉 Thanks {query.from_user.first_name}! এখন তুমি chat করতে পারো।")
        else:
            await query.message.reply_text("⚠️ আগে group join করো, তারপর 'JOINED' চাপো।")
    except:
        await query.message.reply_text("⚠️ আগে group join করো, তারপর 'JOINED' চাপো।")

# Run Bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.run_polling()