from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text ="О нас")],
  [KeyboardButton(text ="Направления")], [KeyboardButton(text = "Контакты")]
])

setting = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Backend", callback_data="backend_info")],
  [InlineKeyboardButton(text="Frontend", callback_data="frontend_info")],
  [InlineKeyboardButton(text="UX/UI", callback_data="ux_ui_info")]
])
