from aiogram.filters.command import Command
from aiogram import F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import FSInputFile
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram.utils.deep_linking import create_start_link, decode_payload
import src.keyboards as kb
import src.db as db
import base64


router = Router()
CHANEL_NAME = "@test_chanel_46"


class User_TON(StatesGroup):
    link = State()


async def is_referral(message):
    encoded_string = message.text
    encoded_string = encoded_string.replace("/start ", "")
    if len(encoded_string) > 7:
        if len(encoded_string)%4 != 0:
            encoded_string += "=" * (4 - len(encoded_string)%4)
        decoded_id = base64.b64decode(encoded_string).decode()
        
        if decoded_id != str(message.from_user.id):
            ref_fullname = db.get_fullname(decoded_id)
            db.add_invitation(decoded_id)
            db.add_shells(decoded_id, 20)
            db.add_shells(message.from_user.id, 20)
            await message.answer(f"Пользователь {ref_fullname} отправил вам коктейль🍹")
            return True
    
    return False


@router.message(F.text, Command("start"))
async def start_loop(message: Message, bot: Bot):
    await message.answer(f"☀️Привет! :3 Для начала, займи лежак на нашем пляже👇\n{CHANEL_NAME}", reply_markup=kb.take_seat_keyboard)
    if not db.is_old(message.from_user.id):
        db.add_new_user(message.from_user.id, message.from_user.full_name)
        
    await is_referral(message)


@router.message(F.text == "Занять место🏖")
async def take_seat(message: Message, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=f"{CHANEL_NAME}", user_id=message.from_user.id)
    if user_channel_status.status != 'left':
        await message.answer("🔆 Добро пожаловать на пляж SUN in SUM!\n"
                        "Тут, ты можешь начать собирать ракушки🐚, которые, позже, можно будет обменять на солнышки $SUN🌞\n"
                        "Чем займемся сегодня?"
                        , reply_markup=kb.main_keyboard)
    else:
        await message.answer(f"Для начала, займи лежак на нашем пляже👇\n{CHANEL_NAME}", reply_markup=kb.take_seat_done_keyboard)


@router.message(F.text == "Занял!⛱")
async def сheck_bag(message: Message, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=f"{CHANEL_NAME}", user_id=message.from_user.id)
    if user_channel_status.status != 'left':
        await message.answer("🔆 Добро пожаловать на пляж SUN in SUM!\n"
                        "Тут, ты можешь начать собирать ракушки🐚, которые, позже, можно будет обменять на солнышки $SUN🌞\n"
                        "Чем займемся сегодня?"
                        , reply_markup=kb.main_keyboard)
    else:
        await message.answer(f"Для начала, займи лежак на нашем пляже👇\n{CHANEL_NAME}", reply_markup=kb.take_seat_done_keyboard)
    
    
@router.message(F.text == "Проверить сумку👛")
async def сheck_bag(message: Message, bot: Bot):
    user_balance = db.get_balance(message.from_user.id)
    await message.answer(f"На данный момент у тебя имеется {user_balance} ракушек🐚", reply_markup=kb.back_to_main_keyboard)
    
    
@router.message(F.text == "Подарить другу коктейль🍹")
async def gift_cocktail(message: Message, bot: Bot):
    user_ref_link = await create_start_link(bot, str(message.from_user.id), encode=True)
    await message.answer(f"Пригласи друга попить коктейли на наш пляж, и получи 20 ракушек в подарок!\n"
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
async def сheck_bag(message: Message, bot: Bot, state = FSMContext):
    await state.set_state(User_TON.link)
    await message.answer("Укажи свой TON кошелек формата EQ, UQ или домен, если имеется", reply_markup=kb.back_to_main_keyboard)
    
    
@router.message(User_TON.link)
async def get_name(message: Message,state = FSMContext):
    if message.text != "Главное меню":
        await state.update_data(link = message.text)
        db.add_ton_link(message.from_user.id, message.text)
        await message.answer("Ваш TON кошелек успешно сохранён!", reply_markup=kb.main_keyboard)
        

@router.message(F.text == "Главное меню")
async def сheck_bag(message: Message, bot: Bot):
    await message.answer("Главное меню", reply_markup=kb.main_keyboard)
    

@router.message(F.text)
async def unidentified_text(message: Message, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=f"{CHANEL_NAME}", user_id=message.from_user.id)
    if user_channel_status.status != 'left':
        await message.answer("🔆 Добро пожаловать на пляж SUN in SUM!\n"
                        "Тут, ты можешь начать собирать ракушки🐚, которые, позже, можно будет обменять на солнышки $SUN🌞\n"
                        "Чем займемся сегодня?"
                        , reply_markup=kb.main_keyboard)
    else:
        await message.answer(f"Для начала, займи лежак на нашем пляже👇\n{CHANEL_NAME}", reply_markup=kb.take_seat_done_keyboard)