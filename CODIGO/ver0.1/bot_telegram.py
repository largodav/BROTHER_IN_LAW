import logging
import os 
from telegram import Update 
from telegram.ext import filters, MessageHandler,ApplicationBuilder,ContextTypes,CommandHandler 

#PAra cargar claves, etc...
from dotenv import load_dotenv
load_dotenv()

user_chat=" "
username_chat =""


#Esta parte es para configurar loggingel módulo, para que sepas cuándo (y por qué) las cosas no funcionan como se esperaba:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

#Funcion para el /start comando.... ESTE COMANDO ES EL QUE ARRANCA ¡¡¡¡
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    #Mensaje de presentacion Y AYUDA DEL BOT..
    await context.bot.send_message(chat_id=update.effective_chat.id,text="HOLA Soy tu brother in law.UN BOT PARA AYUDARTE CON TUS BUSQUEDAS DE PRODUCTOS DENTRO DEL CATALOGO DEL DEPTO DE INFORMATICA.")
    
    #Recuperar el nombre del user del chat..., con esto ... debemos obtener el username.. para comprobacion de la B.D
    user = update.message.from_user
    global user_chat, username_chat
    user_chat = user['first_name']
    username_chat = user['username']
    #print(user)
    #print(user_chat)
    #print('You talk with user {} and his user ID: {} '.format(user_chat, user['id']))
    
#Comando de busqueda de producto...




#Agregando otro controlador , para escuchar mensajes regulares, Use MessageHandler, otra Handlersubclase, para hacer eco de todos los mensajes de texto.
async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text)

#Comando para comando desconocido
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Perdon¡¡. no entiendo lo que me quieres pedir.") 
    
if __name__ == '__main__':
    
    application = ApplicationBuilder().token(os.getenv("KEY_BOT_TELEGRAM")).build()
    
    #Comando /start
    start_handler = CommandHandler('start',start)
    #Comando "repite"
    echo_handler = MessageHandler(filters.TEXT &(~filters.COMMAND),echo)
    
    #Comando desconocido
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    

    
    application.run_polling()
    
    
    