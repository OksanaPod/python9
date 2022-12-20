from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import commands as com


key = input('Enter your telegram token: ')

app = ApplicationBuilder().token(f"{key}").build()

app.add_handler(CommandHandler("start", com.start_command))
app.add_handler(CommandHandler("help", com.help_command))
app.add_handler(CommandHandler("calc", com.calc_command))

print('server start')
app.run_polling()