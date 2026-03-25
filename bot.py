import asyncio, os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("8793939585")
CHANNEL = "@https://t.me/oq_pubg_store"

bot = Bot(8793939585)
dp = Dispatcher()

async def is_joined(user_id):
    try:
        member = await bot.get_chat_member(https://t.me/oq_pubg_store)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

def join_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Join Channel", url=f"https://t.me/oq_pubg_store.replace('@','')}")],
        [InlineKeyboardButton(text="✅ Check", callback_data="check")]
    ])

@dp.message(Command("start"))
async def start(message: types.Message):
    if not await is_joined(message.from_user.id):
        await message.answer("🚫 اول چینل join کړه!", reply_markup=join_button())
        return
    await message.answer("🎉 ښه راغلاست!")

@dp.callback_query(lambda c: c.data == "check")
async def check(callback: types.CallbackQuery):
    if await is_joined(callback.from_user.id):
        await callback.message.edit_text("✅ ته join کړی دی!")
    else:
        await callback.answer("❌ لا هم نه یې!", show_alert=True)

@dp.message()
async def all_msg(message: types.Message):
    if not await is_joined(message.from_user.id):
        await message.answer("🚫 اول چینل join کړه!", reply_markup=join_button())
        return

async def main():
    print("Running...")
    await dp.start_polling(bot)

asyncio.run(main())