#import stats_manager
from tracemalloc import start
#import level_select
from base64 import decode
from cgitb import text
from email.mime import audio
from tkinter import END
#from telegram import ChatAction, Update
#from telegram.ext import Updater, CommandHandler, CallbackContext 
#import requests
from telegram import *
from telegram.ext import *
from requests import *
import requests

token_test = "5700589533:AAHQDSdt0hPFGlx6laOD-_1wcysKacI42ik"
token = "5567751406:AAETq81wEWNsEtIhjStsb2UOzqGfJoRXI-E" 
updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 
 
commands = '/start\n/help\n/stats\n/audio\n/photo'

url = "https://russianwarship.rip/api/v1/statistics/latest"

response = requests.get(url)
json = response.json()
data = json['data']
increase = data['increase']
stats = data['stats']
personnel, tanks, armoured_fighting_vehicles, artillery_systems, mlrs, aa_warfare_systems, warships_cutters, special_military_equip, atgm_srbm_systems = stats['personnel_units'], stats['tanks'], stats['armoured_fighting_vehicles'], stats['artillery_systems'], stats['mlrs'], stats['aa_warfare_systems'], stats['warships_cutters'], stats['special_military_equip'], stats['atgm_srbm_systems']
personnel_increase = increase['personnel_units']
tanks_increase = increase['tanks']
armoured_fighting_vehicles_increase = increase['armoured_fighting_vehicles']
artillery_systems_increase = increase['artillery_systems']
mlrs_increase = increase['mlrs']
aa_warfare_systems_increase = increase['aa_warfare_systems']
warships_cutters_increase = increase['warships_cutters']
special_military_equip_increase = increase['special_military_equip']
atgm_srbm_systems_increase = increase['atgm_srbm_systems']

statsTxt = 'за час повномасштабного вторгнення московії на територію України:\n \nЗнищено, кількість, (\"поповнення\") \n \nорки {personnel}  (+{personnel_increase}) \nчмоня 1 (0) \nтанки {tanks}  (+{tanks_increase}) \nбронетранспортери {armoured_fighting_vehicles}  (+{armoured_fighting_vehicles_increase}) \nартилерійські устаговки {artillery_systems}  (+{artillery_systems_increase}) \nРеактивні системи залпового вогню {mlrs}  (+{mlrs_increase}) \nППО {aa_warfare_systems}  (+{aa_warfare_systems_increase}) \nРПГ {atgm_srbm_systems}  (+{atgm_srbm_systems_increase}) \nспец. спорядження {special_military_equip}  (+{special_military_equip_increase}) \nвійськові кораблі {warships_cutters} (+{warships_cutters_increase})'

def start_handler(update: Update, context: CallbackContext): 
    buttons = [[KeyboardButton("help")],[KeyboardButton("war stats")]]
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!\nfor more info write \"/help\"",
    reply_markup=ReplyKeyboardMarkup(buttons))
    pass

def message_handler(update: Update, context: CallbackContext):
    if "help" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"commands, that u can use: \n{commands}")
        pass
    if "war stats" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f'{statsTxt}')
    pass

def stats_handler(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f'{statsTxt}')
pass  

def audio_handler(update: Update, context: CallbackContext):
    with open('OMFG-Hello.mp3', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_AUDIO)
        context.bot.send_audio(update.effective_chat.id, audio=file)
    pass

def photo_handler(update: Update, context: CallbackContext):
    with open('Wise_mystical_tree.jfif', 'rb') as photo:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(update.effective_chat.id, photo=photo)
    pass

def help_handler(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text = f"commands, that u can use: \n{commands}")
    pass

start_command_handler = CommandHandler("audio", audio_handler)
dispatcher.add_handler(start_command_handler)

start_command_handler = CommandHandler("photo", photo_handler)
dispatcher.add_handler(start_command_handler)

start_command_handler = CommandHandler("stats", stats_handler) 
dispatcher.add_handler(start_command_handler) 

start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
dispatcher.add_handler(MessageHandler(Filters.text ,message_handler))

start_command_handler = CommandHandler("help", help_handler) 
dispatcher.add_handler(start_command_handler)

# Start bot 
updater.start_polling()