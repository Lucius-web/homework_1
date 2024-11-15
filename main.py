# from aiogram import Bot, Dispatcher,F
# from aiogram.types import Message
# from aiogram.filters import CommandStart, Command
# import asyncio

# bot = Bot(token = "7134147814:AAHQPlaA0xKe_159rPSByXMpWJ6zgtZOHaA")
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def start(message: Message):
#   await message.answer("Hello пользователь\nможете ввести команду /help чтобы увидеть\n все команды")
  
# @dp.message(Command('help'))
# async def help(message: Message):
#   await message.reply("Чем могу помочь? вы можете запустить остальные команды /about, /contact, /location, /photo, '")
  
# @dp.message(Command('about'))
# async def about(message: Message):
#   await message.reply("Geeks - это айти курсы в Оше, Кара-Балте, Бишкеке основанная в 2018г")
  
# @dp.message(Command('contact'))
# async def contact(message: Message):
#   await message.reply_contact(phone_number='+996505180600', last_name='isko', first_name='isko')
  
# @dp.message(Command('location'))
# async def location(message: Message):
#   await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)
  
# @dp.message(F.text.lower() == 'Исхак')
# async def iskhak(message: Message):
#   await message.reply('Ученик 3-го месяца') 
  
# async def main():
#   await dp.start_polling(bot)
  
# if __name__ == "__main__":
#   asyncio.run(main())
