import logging
import os
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import (
    filters,
    CallbackContext,
    MessageHandler,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
)

# PAra cargar claves, etc...
from dotenv import load_dotenv

load_dotenv()

user_chat = " "
username_chat = ""

# Define states for conversation
MENU, OPTION1, OPTION2 = range(3)

# Esta parte es para configurar loggingel módulo, para que sepas cuándo (y por qué) las cosas no funcionan como se esperaba:
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


# Funcion para el /start comando.... ESTE COMANDO ES EL QUE ARRANCA ¡¡¡¡
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensaje de presentacion Y AYUDA DEL BOT..
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="HOLA Soy tu brother in law.UN BOT PARA AYUDARTE CON TUS BUSQUEDAS DE PRODUCTOS DENTRO DEL CATALOGO DEL DEPTO DE INFORMATICA.",
    )

    # Recuperar el nombre del user del chat..., con esto ... debemos obtener el username.. para comprobacion de la B.D
    user = update.message.from_user
    global user_chat, username_chat
    user_chat = user["first_name"]
    username_chat = user["username"]
    # print(user)
    # print(user_chat)
    # print('You talk with user {} and his user ID: {} '.format(user_chat, user['id']))


# Comando de busqueda de producto...
async def buscar(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data="option1")],
        [InlineKeyboardButton("Option 2", callback_data="option2")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Please choose an option:", reply_markup=reply_markup
    )
    return MENU


# Controlador de clic de botón
async def button(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    if query.data == "option1":
        await query.edit_message_text(text="Seleccionó la opción 1.")
        return OPTION1
    elif query.data == "option2":
        await query.edit_message_text(text="Seleccionó la opción 2.")
        return OPTION2
    else:
        await query.edit_message_text(text="Opción desconocida seleccionada.")
        return MENU


# Agregando otro controlador , para escuchar mensajes regulares, Use MessageHandler, otra Handlersubclase, para hacer eco de todos los mensajes de texto.
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


# Comando para comando desconocido
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Perdon¡¡. no entiendo lo que me quieres pedir.")

# Cancel handler
async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token(os.getenv("KEY_BOT_TELEGRAM"))
        .read_timeout(10)
        .write_timeout(10)
        .concurrent_updates(True)
        .build())
    #ConversationHandler para manejar maquina de estados
    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler("start",start)],
    #     states={
    #         MENU: [CallbackQueryHandler(button)],
    #         OPTION1: [MessageHandler(filters.TEXT & ~filters.COMMAND,cancel)],
    #         OPTION2: [MessageHandler(filters.TEXT & ~filters.COMMAND,cancel)],
    #     },
    #     fallbacks=[CommandHandler("start",start)],
    #)
    
    # Comando /start
    start_handler = CommandHandler("start", start)
    # Comando "repite"
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    # Comando buscar
    buscar_handler = CommandHandler("buscar", buscar)
    # Comando desconocido
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(buscar_handler)
    application.add_handler(unknown_handler)
    
    
    application.run_polling()
