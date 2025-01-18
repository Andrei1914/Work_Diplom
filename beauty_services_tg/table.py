import asyncpg
import logging
import asyncio
from config import *
from datetime import date,timedelta

#логирование всех процессов
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('log_db.py')

#создание соединения с бд
async def create_connection():
    try:


        logger.info('Подключение к бд')
        conn = await asyncpg.connect(**DB_CONFIG)
        logger.info('Успешное подключение!')
        return conn
    

    except Exception as e:
        logger.info(e)


#создание таблиц при их отсутствии
async def create_table(conn):
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                name VARCHAR(200),
                surname VARCHAR(200),
                phone_number VARCHAR(100),
                password VARCHAR(200)
                )
        ''')
    
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS service (
                user_id BIGINT,
                service VARCHAR(200),
                date_service DATE
                )
            ''')
        
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS help (
                user_id BIGINT,
                message VARCHAR(200)
                date_publish DATE
                )
            ''')
        

        conn.execute("SELECT MIN(date_service) FROM service")
        min_date = conn.fetchone()[0]
        date_now = date.today() - timedelta(days=7)

        if min_date == date_now:

            conn.execute("DELETE FROM service")  
            logger.info('Очистка таблицы с записями на услуги выполнена успешно')

        else:
            logger.info('Очистка таблицы с записями на услуги не требуется')

        conn.execute("SELECT MIN(date_publish) FROM help")
        min_date_help = conn.fetchone()[0]
        date_now_help = date.today() - timedelta(days=7)

        if min_date_help == date_now_help:

            conn.execute("DELETE FROM help")  
            logger.info('Очистка таблицы с вопросами выполнена успешно')

        else:
            logger.info('Очистка таблицы с вопросами не требуется')


        logger.info('Успешное создание таблиц!')
    except Exception as e:
        logger.info('Ошибка при создании таблиц, проверьте передаваемые агрументы')


#проверка соеденения с базой данных
async def connection_db():
    conn = await create_connection()
    try:
        await create_table(conn)
    finally:
        await conn.close()