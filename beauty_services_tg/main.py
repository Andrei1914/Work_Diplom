from config import *
from text import *
from interaction import *
from aiogram import executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import *
import asyncio
from table import *
from datetime import date

class RegistrationState(StatesGroup):#поля для регистрации пользователя
    name: str = State()
    surname: str = State()
    phone_number: str = State()
    password: str = State()

class Help(StatesGroup):#поля для вопроса от пользователя
    help_message = State()


#хендлеры общей информации и взаимодействий
@dp.message_handler(commands=['start'])
async def hello_func(message):
    if await get_user(message.from_user.id):
        await message.reply(f"🌸{message.from_user.username}, добро пожаловать "+ hello_text, reply_markup=start_button)
    else:
        await message.reply(f"{message.from_user.username}, добро пожаловать! Вы не зарегестрированны, но что бы записываться на услуги, нужно войти в систему👀", reply_markup = log)
     


@dp.message_handler(text ="📅Запись📅")
async def services_func(message):
    await message.answer('👇Нажмите на кнопку интересующей вас услуги:👇', reply_markup=services)
 
@dp.message_handler(text="📝Отзывы📝")
async def services_func(message):
    description = (
        "Мы всегда стремимся к совершенству и ценим ваше мнение! 🌟\n\n"
        "Ваши отзывы помогают нам улучшать наш сервис и делать его более удобным для вас. "
        "Если у вас есть идеи, предложения или вы просто хотите поделиться своим опытом, "
        "пожалуйста, нажмите на кнопку ниже, чтобы оставить свой отзыв или посмотреть другие. "
        "Каждое ваше слово имеет значение для нас, и мы будем рады услышать ваше мнение!"
    )
    await message.answer(description, reply_markup=feedback)
 


#хендлеры для регистрации
@dp.callback_query_handler(text="Регистрация")
async def register_name_func(call):
    await call.message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.name.set()

@dp.message_handler(state=RegistrationState.name)
async def register_surname_func(message, state):
    await state.update_data(name = message.text) 
    await message.answer("Введите свою фамилию, если хотите пропустить, то просто поставьте прочерк:")
    await RegistrationState.surname.set()

@dp.message_handler(state=RegistrationState.surname)
async def register_phone_number_func(message, state):
    await state.update_data(surname = message.text)    
    await message.answer("Введите ваш номер(Для связи с мастером):")
    await RegistrationState.phone_number.set()   

@dp.message_handler(state=RegistrationState.phone_number)
async def register_password_func(message, state):
    await state.update_data(phone_number = message.text)    
    await message.answer("Введите пароль для входа в аккаунт")
    await RegistrationState.password.set()   

@dp.message_handler(state=RegistrationState.password)
async def full_register_func(message, state):
    await state.update_data(password = message.text)   
    data = await state.get_data()
    if await add_user(message.from_user.id, data['name'], data['surname'], data['phone_number'], data['password']):   
        await message.answer("✅Регистрация пройдена!✅", reply_markup=start_button)   
    else:
        await message.answer("Ошибка данных", reply_markup=start_button)

    await state.finish() 





#Сообщение для специалиста
@dp.callback_query_handler(text="help")
async def help_func(call):
    await call.message.answer("😊Задайте вопрос, а мы отправим его мастеру😊")
    await Help.help_message.set()

@dp.message_handler(state=Help.help_message)
async def message_help_db(message, state): 
    await state.update_data(help_message = message.text) 
    now = date.today()
    data = await state.get_data()
    user_id = message.from_user.id
    if await add_message(user_id, data['help_message'], now):
        await message.answer("Благодарим за вопрос, мы ответим на него в ближайшее время!🙏❤️📞 ")
    else:
        await message.answer("Непредвиденная ошибка! ")

    await state.finish() 






service_num = {}

# Маникюр
@dp.callback_query_handler(text="manicure")
async def manicure_func(call):
    await call.message.answer("Выберите интерисующий вас тип услуги :", reply_markup=extended_services_manicure)


@dp.callback_query_handler(text="build_up")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Наращивание'

@dp.callback_query_handler(text="one_nail")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Дизайн одного ногтя'

@dp.callback_query_handler(text="build_up_nail")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Наращивание ногтей'

@dp.callback_query_handler(text="Manicure_gel_polish")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Маникюр+гель лак'

@dp.callback_query_handler(text="Full_pedicure")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Полный педикюр с покрытием'







# Ресницы
@dp.callback_query_handler(text="eyelashes")
async def eyelashes_func(call):
    await call.message.answer("Выберите интерисующий вас тип услуги :", reply_markup=extended_services_eyelashes)

@dp.callback_query_handler(text="eyebrow_coloring")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Окрашивание бровей'

@dp.callback_query_handler(text="eyebrow_correction")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Коррекцию бровей'

@dp.callback_query_handler(text="eyebrow_architecture")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Архитектуру бровей'

@dp.callback_query_handler(text="eyelash_extensions")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Наращивание ресниц'






# Макияж
@dp.callback_query_handler(text="makeup")
async def makeup_func(call):
    await call.message.answer("Выберите интерисующий вас тип услуги :", reply_markup=extended_services_eyelashes)


@dp.callback_query_handler(text="makeup_and_grim")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Макияж и грим'

@dp.callback_query_handler(text="face_contouring")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Контуринг лица'

@dp.callback_query_handler(text="temporary_tattoos")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Временные тату'








# Чистка лица
@dp.callback_query_handler(text="cleaning")
async def cleaning_func(call):
    await call.message.answer("Выберите интерисующий вас тип услуги :", reply_markup=extended_services_cleaning)

@dp.callback_query_handler(text="mechanical_cleaning")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Механическую чистку'

@dp.callback_query_handler(text="ultrasonic_cleaning")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Ультразвуковую чистку'

@dp.callback_query_handler(text="vacuum_cleaning")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Вакуумнную чистку лица'

@dp.callback_query_handler(text="laser_cleaning")
async def manicure_func(call):
    await call.message.answer("Выберите удобную для вас дату📝 :", reply_markup=create_date_keyboard())
    service_num[call.from_user.id] = 'Лазерную чистку'






#запись на определенное число
@dp.callback_query_handler(lambda c: True)
async def process_cleaning_date(callback_query: types.CallbackQuery):
    date = callback_query.data
    user_id = callback_query.from_user.id 
    service_name = service_num.get(user_id)
    if await add_service_to_user(user_id, service_name, date):
        await callback_query.message.answer(f"Вы записались на {service_name}, на {date}, ждем вас!🔥❤️", reply_markup=start_button)
    else:
        await callback_query.message.answer(f"Вы не можете записаться на {service_name}, на {date}, тк записей на этот день больше 5 или же вы записаны на эту процедуру((", reply_markup=start_button)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(connection_db())