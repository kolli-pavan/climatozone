import telegram.ext
import datetime as dt
import requests


TELE_KEY='6263514078:AAGCvoCBs6yGVWJcDiwY5S50MWZToLCyxac';

def start(update,context): 
  update.message.reply_text("welcome to Bot !!!")

def help(update,context): 
  update.message.reply_text("""The following commands are available: 
                                                  /start for Starting the bot 
                                                  /weather cityname for knowing weather of the city
                                                  /help for help
                                                  /about for About info 
                                                  
                                                  Wish you a Happy day !!! """)

def about(update,context):
  update.message.reply_text("""
                                                Hello , How are you? 
                                                This bot will help you in knowing the weater details of the city you are interested in. '
                                                You can try it by writing command /weather city_name .
                                                For example, /weather London
                                                
                                                Thanks & Regards: 
                                                Pavan Kolli.
                                              """)
  

'''

{'coord': {'lon': -0.1257, 'lat': 51.5085}, 
'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
 'base': 'stations', 
 'main': {'temp': 2.37, 'feels_like': -0.73, 'temp_min': 1.4, 'temp_max': 3.53, 'pressure': 1024, 'humidity': 83}, 
 'visibility': 10000, 
 'wind': {'speed': 3.09, 'deg': 50}, 
 'clouds': {'all': 24}, 'dt': 1677398706, '
 sys': {'type': 2, 'id': 2075535, 
 'country': 'GB', 'sunrise': 1677394393, 
 'sunset': 1677432844}, 
 'timezone': 0, 
 'id': 2643743, 
 'name': 'London', 
 'cod': 200}
'''


def weather(update,context): 
  BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
  API_KEY='4fb2a0f35b8dabb8a075864c1f93e54b'
  city=context.args[0]
  url=BASE_URL+"units=metric&q="+city+"&appid="+API_KEY;
  response=requests.get(url).json()
  temp=response['main']['temp']
  feels_like=response['main']['feels_like']
  description=response['weather'][0]['description']
  update.message.reply_text(f"""City={city}
                                                      Temperature={temp}
                                                      feels like ={feels_like}
                                                      Description={description}
                                """)
  

updater=telegram.ext.Updater(TELE_KEY,use_context=True)
disp=updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("about",about))
disp.add_handler(telegram.ext.CommandHandler("weather",weather))
disp.add_handler(telegram.ext.CommandHandler("help",help))

updater.start_polling()
updater.idle()



