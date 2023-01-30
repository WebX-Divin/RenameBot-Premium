import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5609721310:AAEo034QWlWz50WEbwIk-S53tplMOFe-VPw")

API_ID = int(os.environ.get("API_ID", "17318541"))

API_HASH = os.environ.get("API_HASH", "3f0136ab75eaa468e7b5f3020be17588")

STRING = os.environ.get("STRING", "BQDX80IAHdm-FxxN3cIlvkjwlgEKJH4h_s9b3sRpPsfyPeXMqTxAEQsXMFTk4p3kXQc5HZQqFmjk89QK5Iv8RwYySkpPjf2XIp76QpMziFxvgxK7EIiyIb2AMHBRi0PYOQ-a749YPz211vj6DuftMe3v3laS580OP1ofPWOIWjDnT3C9kG3Te7KXkFut4D9FYI7a031mu-tFKdCtkcyK9KBPw47trkDu6nJNcTpmYlP_P-vFyZK0jHV1AuE5lS3z0pIOBbqOHw66VLk3f9AEwipVNkvlYpHPU2N2SnXsLrVeWXt3ysjjLCLYFs4QRwxKRFTKqjfbme6DE_g-UMaIzO6fQHulQQAAAABHGLSQAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
