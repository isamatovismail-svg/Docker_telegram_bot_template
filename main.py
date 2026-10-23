import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import config
from bot.database import init_db
from bot.handlers import router as main_router
from bot.middlewares import LoggingMiddleware


async def main() -> None:
    # ── Logging ────────────────────────────────────────────────
    logging_level = getattr(logging, config.logging_level.upper(), logging.INFO)
    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    logging.info("🚀 Bot ishga tushmoqda...")

    # ── Database ───────────────────────────────────────────────
    await init_db()

    # ── Bot & Dispatcher ───────────────────────────────────────
    bot = Bot(
        token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    # ── Middleware ─────────────────────────────────────────────
    dp.update.outer_middleware(LoggingMiddleware())

    # ── Routerlar ──────────────────────────────────────────────
    dp.include_router(main_router)

    # ── Polling ────────────────────────────────────────────────
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("✅ Bot muvaffaqiyatli ishga tushdi! Xabarlar kutilmoqda...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logging.info("🛑 Bot to'xtatildi.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
