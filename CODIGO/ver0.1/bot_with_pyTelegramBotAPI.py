import telebot
from telebot import types 
import os
# PAra cargar claves, etc...
from dotenv import load_dotenv
from scrap_selenium import buscar_por_ref
load_dotenv()

bot = telebot.TeleBot(os.getenv("KEY_BOT_TELEGRAM"))


#*************FUNCIONES DE LAS LLAMADAS DE LOS BOTONES....*******************
def buscar_referencia(message):
    ref = message.text 
    print (ref , len(ref))
    print(ref.isdigit())
    #Portatil pruebas 15215500693
    
    if  ref.isdigit() and len(ref) == 11 :
        #Respuesta ok, tenemos la ref del producto....
        print(f"Buscando referencia {ref}")     
        #Ahora debemos empezar el proceso de scraping...
        imagen_producto,nombre_producto,caracteristicas_producto=  buscar_por_ref(ref)
        print(f"TENEMOS :\n Nombre del producto: {nombre_producto},\n Descripcion: {caracteristicas_producto},\n Imagen del producto:{imagen_producto}")
        bot.send_message(message.chat.id, 'Este es tu producto: ')
        bot.send_photo(message.chat.id,imagen_producto)
        bot.send_message(message.chat.id,nombre_producto)
        bot.send_message(message.chat.id,caracteristicas_producto)
        
    else:
        #Debemos chequer que la respuesta sea correcta, numerica y maximo 10 nº
        bot.send_message(message.chat.id, 'El formato no es correcto, debe ser numerico, 10 digitos¡¡¡¡')
        respuesta = bot.send_message(message.chat.id, 'Por favor introduce la REFERNCIA a buscar. (###########)',parse_mode="Markdown")
        bot.register_next_step_handler(respuesta,buscar_referencia)
#*****************************************************************************

#Funcion start
@bot.message_handler(commands=['start'])
def _start(message):
    msg = ("Hola " +str(message.chat.username))
    bot.send_message(message.chat.id,msg)    
 

    

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
            respuesta = bot.send_message(callback.message.chat.id, 'Por favor introduce la REFERNCIA a buscar. (###########)',parse_mode="Markdown")
            bot.register_next_step_handler(respuesta,buscar_referencia)
            
                            

#Funcion Loro
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    #1. Determinamos que buscar
    bot.reply_to(message,message.text)




bot.infinity_polling(
    #Reiniciar ante cambios
    restart_on_change=True,
    )

