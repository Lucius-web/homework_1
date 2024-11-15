from aiogram import Bot, Dispatcher,F
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
import asyncio
import random

bot = Bot(token = "7134147814:AAHQPlaA0xKe_159rPSByXMpWJ6zgtZOHaA")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await message.answer("Hello пользователь\nможете ввести команду /help чтобы увидеть\n все команды")

@dp.message(Command('help'))
async def help(message: Message):
  await message.reply("что-бы запустить напишите я готов")

@dp.message(F.text.lower() == 'Я готов')
async def start_random(message : Message):
  await message.answer("загадйтк число от 1 до 3")
  user = int(message.text)
  run_um = random.choice([1,2,3])
  if user == run_um:
    await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
  else:
    await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')
  
async def main():
  await dp.start_polling(bot)
  
if __name__ == "__main__":
  asyncio.run(main())



