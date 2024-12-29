import telebot
from telebot import types 
import os
# PAra cargar claves, etc...
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("KEY_BOT_TELEGRAM"))


#*************FUNCIONES DE LAS LLAMADAS DE LOS BOTONES....*******************
def buscar_referencia(message):
    ref = message.text 
    print(f"Busacndo referencia {ref}")

#Funcion start
@bot.message_handler(commands=['start'])
def _start(message):
    msg = ("Hola " +str(message.chat.username))
    bot.send_message(message.chat.id,msg)    
 
#Funcion Loro
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    #1. Determinamos que buscar
    bot.reply_to(message,message.text)
    
   
#funcion Buscar    
@bot.message_handler(commands=['buscar'])
def buscar(message):
    msg2 = ("Buscando...") 
    bot.send_message(message.chat.id,msg2)  
    #BOTONES PARA SELECCIONAR TIPO DE BUSQUEDA
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    boton_buscar_ref = types.InlineKeyboardButton('Buscar por REF',callback_data='buscar_ref')
    
    markup.add(boton_buscar_ref)
    bot.send_message(message.chat.id, 'Selecciona una opcion :', reply_markup=markup)
    

    

#Implementar las respuestas de los BOTONES
@bot.callback_query_handler(func=lambda call:True)
def respuesta_boton(callback):
    if callback.message:
        #DETERMINAMOS EL BOTON PULSADO...
        if callback.data == 'buscar_ref':
            # 1.Preguntamos ref a buscar, chequeamos respuesta correcta, y mandamos a funcion para buscar ref...
            #Debemos chequer que la respuesta sea correcta, numerica y maximo 11 nº
            respuesta = bot.send_message(callback.message.chat.id, 'Por favor introduce la REFERNCIA a buscar. (###.###.#####)',parse_mode="Markdown")
            if type(respuesta) == int:
                bot.register_next_step_handler(respuesta,buscar_referencia)
            print("no es un texto")
bot.infinity_polling(
    #Reiniciar ante cambios
    restart_on_change=True,
    )

