from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


take_seat_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Занять место🏖')]],
    resize_keyboard=True
)


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Проверить сумку👛")],
    [KeyboardButton(text="Подарить другу коктейль🍹")],
    [KeyboardButton(text="Правила🥥")],
    [KeyboardButton(text="Привязать свой TON💎")]
    ],
    resize_keyboard=True
)


back_to_main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Главное меню")]],
    resize_keyboard=True
)