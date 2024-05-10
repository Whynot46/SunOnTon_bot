import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from src.handlers import router


API_TOKEN = "API_KEY"


bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

                
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
