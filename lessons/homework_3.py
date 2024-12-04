from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from aiogram import types
import keyboard as kb

from lessons.config import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветствую вас {message.from_user.first_name}!\nЯ ваш проводник, если хотите узнать какие у нас бренды то нажмите на нижние кнопки', reply_markup=kb.main)


@dp.message(F.text == 'О нас')
async def about(message: Message):
    await message.answer('Мы продаем сопртивные и Сунна одежды любых видов,любых цыетов и разных размеров .')
    
@dp.message(F.text == 'Направления')
async def direction(message: Message):
    await message.answer('У нас имеются 3 бренда одежды, нажмите на кнопки что-бы увидеть', reply_markup=kb.main)
    
@dp.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('@vip_odejda\n+996 755 18 2008\nАкмалидин Мурзаев')
    
@dp.message(F.text == 'Lining')
async def lining_info(message: Message):
    await message.answer('''Это качественные,стильные спортивные одежды.Если вы занимаетесь спортом то как раз для вас
    стоимость:от 7000 до 10 000 
    и у нас скида покупка одежды за 10 000 вы можете выбрать любые кроссовки в подарок''')
@dp.message(F.text == 'Nike')
async def Nike_info(message: Message):
    await message.answer('''Это тоже спортивная,и стильная одежда есть много вариантов для вас 
    стоимость: от 6000 до 9000''')

@dp.message(F.text == 'Sajda')
async def Sajda_info(message: Message):
    await message.answer('''Это бренд продает Сунна одежды,разных цветов и разных размеров,разных видов
    стоимость: от 2500 до 5000''')
async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Вы отключились от бота!")
