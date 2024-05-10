from aiogram.filters.command import Command
from aiogram import F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from time import sleep
from aiogram.types import FSInputFile
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio
from datetime import datetime, timedelta
import src.keyboards as kb
import src.db as db


router = Router()


@router.message(F.text, Command("start"))
async def start_loop(message: Message, bot: Bot):
    await message.answer("☀️Привет! :3 Для начала, займи лежак на нашем пляже👇", reply_markup=kb.take_seat_keyboard)
    if not db.is_old(message.from_user.id):
        db.add_new_user(message.from_user.id, message.from_user.full_name)
    db.add_shells(message.from_user.id, 10)
    db.add_shells(message.from_user.id, 10)


@router.message(F.text == "Занять место🏖")
async def take_seat(message: Message, bot: Bot):
    await message.answer("🔆 Добро пожаловать на пляж SUN in SUM!\n"
                        "Тут, ты можешь начать собирать ракушки🐚, которые, позже, можно будет обменять на солнышки $SUN🌞\n"
                        "Чем займемся сегодня?"
                        , reply_markup=kb.main_keyboard)
    
    
@router.message(F.text == "Проверить сумку👛")
async def сheck_bag(message: Message, bot: Bot):
    user_balance = db.get_balance(message.from_user.id)
    await message.answer(f"На данный момент у тебя имеется {user_balance} ракушек🐚", reply_markup=kb.back_to_main_keyboard)
    
    
@router.message(F.text == "Подарить другу коктейль🍹")
async def gift_cocktail(message: Message, bot: Bot):
    user_ref_link = f"хттпс:\\т.ме\реферассылка-{message.from_user.id}"
    await message.answer(f"Пригласи друга попить коктейли на наш пляж, и получи 20 ракушек в подарок!"
                        f"{user_ref_link}"
                        , reply_markup=kb.back_to_main_keyboard)
    

@router.message(F.text == "Правила🥥")
async def сheck_bag(message: Message, bot: Bot):
    user_balance = message.from_user.id
    await message.answer("Чтобы получить доступ к будущему рынку ракушек и солнц, ты должен:\n"
                        "1.  Находится на нашем пляжном канале\n"
                        "2. Пригласить как минимум 2 друга\n"
                        "3. Указать свой холодный TON кошелек"
                        , reply_markup=kb.back_to_main_keyboard)


@router.message(F.text == "Привязать свой TON💎")
async def сheck_bag(message: Message, bot: Bot):
    await message.answer("Укажи свой TON кошелек формата EQ, UQ или домен, если имеется", reply_markup=kb.back_to_main_keyboard)
    

@router.message(F.text == "Главное меню")
async def сheck_bag(message: Message, bot: Bot):
    await message.answer("Главное меню", reply_markup=kb.main_keyboard)
    

@router.message(F.text)
async def unidentified_text(message: Message, bot: Bot):
    await message.answer("🔆 Добро пожаловать на пляж SUN in SUM!\n"
                        "Тут, ты можешь начать собирать ракушки🐚, которые, позже, можно будет обменять на солнышки $SUN🌞\n"
                        "Чем займемся сегодня?"
                        , reply_markup=kb.main_keyboard)