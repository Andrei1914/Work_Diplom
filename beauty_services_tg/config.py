from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='7796429951:AAHWeYPPCG-bZTvcRBntDzyuxU78XgJGPTw')
dp = Dispatcher(bot, storage=MemoryStorage())
DB_CONFIG = {
    'user': 'postgres',
    'password': '1914',
    'database': 'beauty_services_db',
    'host': 'localhost',
    'port': '5433'
}
