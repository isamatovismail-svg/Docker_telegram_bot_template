import os
import logging
import aiosqlite

# SQLite bazasi saqlanadigan fayl yo'li
DB_PATH = os.path.join("data", "bot_database.db")

logger = logging.getLogger(__name__)


async def init_db() -> None:
    """
    Ma'lumotlar bazasini yaratish va jadvallarni tayyorlash.
    Bot ishga tushganda bir marta chaqiriladi.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id  INTEGER PRIMARY KEY,
                full_name    TEXT    NOT NULL,
                username     TEXT,
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()

    logger.info("Database initialized successfully.")


async def add_user(telegram_id: int, full_name: str, username: str | None = None) -> None:
    """
    Yangi foydalanuvchini bazaga qo'shish.
    Agar allaqachon mavjud bo'lsa, ismini va username ini yangilaydi.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (telegram_id, full_name, username)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET
                full_name = excluded.full_name,
                username  = excluded.username
        """, (telegram_id, full_name, username))
        await db.commit()


async def get_user_count() -> int:
    """
    Bazadagi jami foydalanuvchilar sonini qaytaradi.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0


async def get_all_users() -> list[dict]:
    """
    Barcha foydalanuvchilar ro'yxatini dict formatida qaytaradi.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT telegram_id, full_name, username, created_at FROM users ORDER BY created_at DESC"
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
