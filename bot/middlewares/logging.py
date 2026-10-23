import logging
import time
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    """
    Har bir kiruvchi Telegram update uchun:
      - Kim yuborganini log qiladi
      - Bajarilish vaqtini millisekund (ms) da ko'rsatadi
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        start_time = time.perf_counter()

        user: User | None = data.get("event_from_user")
        user_info = (
            f"User ID: {user.id} | @{user.username or 'no_username'} | {user.full_name}"
            if user else "Unknown User"
        )

        logger.info(f"⬇️  {type(event).__name__} | {user_info}")

        result = await handler(event, data)

        elapsed_ms = (time.perf_counter() - start_time) * 1000
        logger.info(f"✅  Done in {elapsed_ms:.1f}ms")

        return result
