from config import *
from table import *
from datetime import datetime



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



async def add_user(user_id: int, name: str, surname: str, phone_number: str, password: str): #добавление юзера в базу данных
    conn = None
    try:
        
        #cоединение с бд
        conn = await asyncpg.connect(**DB_CONFIG)
        logger.info('Соединение прошло успешно!')

        #команда в бд для добавления пользователя в бд
        await conn.execute('''
            INSERT INTO users(user_id, name, surname, phone_number, password) 
            VALUES($1, $2, $3, $4, $5)
        ''', user_id, name, surname , phone_number, password)
        logger.info(f'Пользователь {user_id} успешно добавлен в бд!')

    except Exception as e: #обработка исключений 

        logger.error(f'Пользователь {user_id} не был добавлен в бд!, Ошибка: {e}')
        return False
    
    finally:
        if conn is not None:
            await conn.close()
            logger.info('Соединение с базой данных закрыто.')
            return True




async def add_service_to_user(user_id: int, service: str, date_service: str): #запись юзера на определнное число и услугу
    conn = None
    try:

        date_obj = datetime.strptime(date_service, '%Y-%m-%d')
        #cоединение с бд
        conn = await asyncpg.connect(**DB_CONFIG)
        logger.info('Соединение прошло успешно!')


        #проверка на число записей и на повторную запись
        if await chek_date(date_obj) or await chek_service(user_id, service, date_obj):


            logger.info(f'Пользователь {user_id} не может быть записан на {service} на {date_service}, тк число записей на этот день больше и равно 7 или же запись отпользователя уже есть в бд')
            return False
        

        else: 


            await conn.execute('''
                INSERT INTO service(user_id, service, date_service) 
                VALUES($1, $2, $3)
            ''', user_id, service, date_obj)
            logger.info(f'Пользователь {user_id} успешно записался на {service} на {date_service}')

            
            #закрытие бд
            if conn is not None:
                await conn.close()
                logger.info('Соединение с базой данных закрыто.')

            return True

    except Exception as e:
        logger.error(f'Пользователь {user_id} не был записан!, Ошибка: {e}')




async def add_message(user_id: int, message: str, now: datetime):
    conn = None
    try:
        #соединение с бд
        conn = await asyncpg.connect(**DB_CONFIG)
        logger.info('Соединение прошло успешно!')
        #команда в бд для записи вопроса от пользователя
        await conn.execute('''
            INSERT INTO help(user_id, message, date_publish) 
            VALUES($1, $2, $3)
        ''', user_id, message, now)
        logger.info(f'Вопрос от пользователя {user_id} успешно занесен в бд')
        
        
    except Exception as e: #обработка осключений

        logger.error(f'Вопрос от пользователя {user_id} не был записан!, Ошибка: {e}')
        return False

    finally:
        if conn is not None:
            await conn.close()
            logger.info('Соединение с базой данных закрыто.')
            return True





async def get_user(user_id): #проверка наличия юзера в бд
    #соединение с дб
    conn = await asyncpg.connect(**DB_CONFIG)
    #команда в дб на поиск юзера по id
    user = await conn.fetchrow('''
        SELECT * FROM users WHERE user_id = $1
    ''', user_id)
    
    if user:

        logger.info(f"Пользователь найден: {user}")
        await conn.close()
        return True
    
    else:

        logger.info("Пользователь не найден.")
        await conn.close()
        return False




async def chek_date(date: str):
    #соединение с дб
    conn = await asyncpg.connect(**DB_CONFIG)
    logger.info('Соединение прошло успешно!')
    #команда в дб на число записей, на дату, на которую пользователь хочет записаться
    count = await conn.fetchval('SELECT COUNT(*) FROM service WHERE date_service = $1', date)
    #проверка на число записей на число
    if count >= 5:
        return True
    else:
        return False



async def chek_service(user_id: int, service: str, date: str):
    #соединение с дб
    conn = await asyncpg.connect(**DB_CONFIG)
    logger.info('Соединение прошло успешно!')
    #команда в дб на повторную запись на определенное число
    count = await conn.fetchval('''
            SELECT COUNT(*) 
            FROM service 
            WHERE user_id = $1 AND date_service = $2 AND service = $3
        ''', user_id, date, service)
    #проверка на повторную запись
    if count:
        return True
    else:
        return False
