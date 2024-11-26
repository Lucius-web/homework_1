import sqlite3
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram import F
from config import token


bot = Bot(token=token)
dp = Dispatcher()
router = Router()


def setup_database():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_text TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        adding_task INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    return conn


db_conn = setup_database()
db_cursor = db_conn.cursor()


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить задачу")],
        [KeyboardButton(text="Показать задачи")],
        [KeyboardButton(text="Очистить список")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    db_cursor.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))
    db_conn.commit()

    await message.answer(
        "Привет! Я ToDo бот. Вы можете добавлять, просматривать и очищать свои задачи.",
        reply_markup=reply_keyboard
    )


@router.message(F.text == "Добавить задачу")
async def add_task(message: types.Message):
    await message.answer("Напишите текст задачи, которую хотите добавить.")
    db_cursor.execute("UPDATE users SET adding_task = 1 WHERE id = ?", (message.from_user.id,))
    db_conn.commit()


@router.message(F.text)
async def handle_task_text(message: types.Message):
    user_id = message.from_user.id
    db_cursor.execute("SELECT adding_task FROM users WHERE id = ?", (user_id,))
    adding_task = db_cursor.fetchone()

    if adding_task and adding_task[0] == 1:
        
        task_text = message.text

        db_cursor.execute("INSERT INTO tasks (user_id, task_text) VALUES (?, ?)", (user_id, task_text))
        db_cursor.execute("UPDATE users SET adding_task = 0 WHERE id = ?", (user_id,))
        db_conn.commit()
        await message.answer("Задача успешно добавлена!")
    else:
        await message.answer("Я не понимаю этот текст. Используйте команды с клавиатуры.")

@router.message(F.text == "Показать задачи")
async def show_tasks(message: types.Message):
    user_id = message.from_user.id
    db_cursor.execute("SELECT id, task_text FROM tasks WHERE user_id = ?", (user_id,))
    tasks = db_cursor.fetchall()

    if tasks:
        inline_kb = InlineKeyboardMarkup()
        for task_id, task_text in tasks:
            task_preview = " ".join(task_text.split()[:2])  # Первые два слова задачи
            inline_kb.add(InlineKeyboardButton(text=task_preview, callback_data=f"task:{task_id}"))
        await message.answer("Выберите задачу:", reply_markup=inline_kb)
    else:
        await message.answer("У вас пока нет задач.")


@router.message(F.text == "Очистить список")
async def clear_list(message: types.Message):
    confirm_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подтвердить", callback_data="clear:confirm"),
                InlineKeyboardButton(text="Отменить", callback_data="clear:cancel")
            ]
        ]
    )
    await message.answer("Вы уверены, что хотите очистить список задач?", reply_markup=confirm_kb)


router.callback_query(F.data.startswith("clear:"))
async def clear_tasks_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    action = callback.data.split(":")[1]

    if action == "confirm":
        db_cursor.execute("DELETE FROM tasks WHERE user_id = ?", (user_id,))
        db_conn.commit()
        await callback.message.edit_text("Список задач успешно очищен!")
    elif action == "cancel":
        await callback.message.edit_text("Очистка списка отменена.")


@router.callback_query(F.data.startswith("task:"))
async def task_callback(callback: types.CallbackQuery):
    task_id = int(callback.data.split(":")[1])
    db_cursor.execute("SELECT task_text FROM tasks WHERE id = ?", (task_id,))
    task = db_cursor.fetchone()

    if task:
        await callback.message.answer(f"Текст задачи: {task[0]}")
    else:
        await callback.message.answer("Задача не найдена.")


dp.include_router(router)

if __name__ == "__main__":
    print("Бот запущен!")
    dp.run_polling(bot)
