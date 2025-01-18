from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from datetime import datetime, timedelta


start_button  = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, #начальные кнопки
    keyboard=[
        [KeyboardButton('📅Запись📅')],
        [KeyboardButton('📝Отзывы📝')],
    ]
)

services = InlineKeyboardMarkup(  #кнопки различных услуг
    inline_keyboard = [
        [InlineKeyboardButton('Маникюр', callback_data='manicure')], 
        [InlineKeyboardButton('Брови | Ресницы', callback_data='eyelashes')], 
        [InlineKeyboardButton('Макияж', callback_data='makeup')], 
        [InlineKeyboardButton('Чистка лица', callback_data='cleaning')], 
        [InlineKeyboardButton('Консультация с специалистом', callback_data='help')]
    ]
)

extended_services_manicure = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Наращивание | от 750₽ | 25 - 35 мин', callback_data='build_up')], 
        [InlineKeyboardButton('Дизайн одного ногтя | 20₽ | 40 - 50 мин', callback_data='one_nail')], 
        [InlineKeyboardButton('Наращивание ногтей | от 1100₽ | 35 - 45 мин', callback_data='build_up_nail')], 
        [InlineKeyboardButton('Маникюр+гель лак | от 750₽ | 30 - 40 мин ', callback_data='Manicure_gel_polish')], 
        [InlineKeyboardButton('Педикюр полный с покрытием | от 1200₽ | 15 - 25 мин', callback_data='Full_pedicure')]
    ]
)

extended_services_eyelashes = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Окрашивание бровей | от 500₽ | 10 - 15 мин', callback_data='eyebrow_coloring')], 
        [InlineKeyboardButton('Коррекция бровей | от 500₽ | 20 - 30 мин', callback_data='eyebrow_correction')], 
        [InlineKeyboardButton('Архитектура бровей | от 1100₽ | 35 - 45 мин', callback_data='eyebrow_architecture')], 
        [InlineKeyboardButton('Наращивание ресниц | от 1200₽ | 30 - 40 мин ', callback_data='eyelash_extensions')], 
    ]
)

extended_services_makeup = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Макияж и грим | от 2000₽ | 30 - 60 мин', callback_data='makeup_and_grim')], 
        [InlineKeyboardButton('Контуринг лица | от 1800 ₽ | 40 - 90 мин', callback_data='face_contouring')], 
        [InlineKeyboardButton('Временные тату | от 950₽ | 10 - 40 мин', callback_data='temporary_tattoos')]
    ]
)

extended_services_cleaning = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Механическая чистка | от 2000₽ | 40 - 90 мин', callback_data='mechanical_cleaning')], 
        [InlineKeyboardButton('Ультразвуковая чистка | от 4000 ₽ | 20 - 50 мин', callback_data='ultrasonic_cleaning')], 
        [InlineKeyboardButton('Вакуумная чистка лица | от 3000₽ | 35 - 50 мин', callback_data='vacuum_cleaning')], 
        [InlineKeyboardButton('Лазерная чистка | от 3500₽ | 30 - 40 мин', callback_data='laser_cleaning')]
    ]
)


log = InlineKeyboardMarkup(
    inline_keyboard = [ 
        [InlineKeyboardButton('Регистрация', callback_data='Регистрация')]
    ]
)


feedback = InlineKeyboardMarkup(
    inline_keyboard = [ 
        [InlineKeyboardButton('Отзывы', url='https://ru.stackoverflow.com/')]
    ]
)

def create_date_keyboard():
    keyboard = InlineKeyboardMarkup()
    now = datetime.now()
    for i in range(7):
        date = now + timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        keyboard.add(InlineKeyboardButton(date_str, callback_data=date_str))

    return keyboard