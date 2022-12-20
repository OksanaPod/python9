from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import functions as f
import logger as log

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.print_start(update.effective_user.first_name,update.effective_user.id,'/start')
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\n'
                                    f'Введи /help помощь\n'
                                    f'Или /calc  рассчет')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.print_start(update.effective_user.first_name,update.effective_user.id,'/help')
    await update.message.reply_text(f'/start - начало\n'
                                    f'/help - командаы\n'
                                    f'/calc  доступные действия: + - * / ( ) ')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    log.print_start(update.effective_user.first_name,update.effective_user.id,msg)
    msg = msg.replace('/calc ', '')
    msg = msg.replace(' ', '')
    result = str(f.calc(msg))
    log.print_result(update.effective_user.first_name,update.effective_user.id,result)
    await update.message.reply_text(f'{msg} => {result}')