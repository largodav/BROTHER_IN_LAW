import logging
import os 
from telegram import Update 
from telegram.ext import ApplicationBuilder,ContextTypes,CommandHandler 

#PAra cargar claves, etc...
from dotenv import load_dotenv
load_dotenv()

#Esta parte es para configurar loggingel módulo, para que sepas cuándo (y por qué) las cosas no funcionan como se esperaba:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Soy tu brother in law.Habla conmigo")
    
    
if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("KEY_BOT_TELEGRAM")).build()
    
    start_handler = CommandHandler('start',start)
    application.add_handler(start_handler)
    
    application.run_polling()
    
    