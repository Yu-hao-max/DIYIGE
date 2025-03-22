import os
import together
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 载入 API Key
TOGETHER_API_KEY = os.getenv("0c801eaa44731f3c82dc1aeb3b9939b8eaf188f3f0b37f6504e1b17f930cb959")
TELEGRAM_TOKEN = os.getenv("7733194461:AAH04GU8w6gxivKXzHONyCL5gvCRVyfm7Z8")

# 配置 Together AI
together.api_key = TOGETHER_API_KEY

# 初始化 Bot
updater = Updater(TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# /start 命令
def start(update, context):
    update.message.reply_text("你好，我是你的 AI 机器人！")

# 处理用户消息
def handle_message(update, context):
    user_message = update.message.text

    # 调用 Together AI API
    response = together.ChatCompletion.create(
        model="Qwen/Qwen2.5-72B",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response['choices'][0]['message']['content']
    update.message.reply_text(bot_reply)

# 添加指令
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# 启动 Bot
updater.start_polling()
updater.idle()
