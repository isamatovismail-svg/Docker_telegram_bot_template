# 🤖 Docker + Telegram Bot Template

**Python 3.11 · Aiogram 3.x · SQLite (aiosqlite) · Docker Compose**

---

## 📁 Fayl Strukturasi

```
├── bot/
│   ├── database/
│   │   ├── __init__.py       # Eksportlar
│   │   └── db.py             # init_db, add_user, get_user_count, get_all_users
│   ├── handlers/
│   │   ├── __init__.py       # Barcha routerlarni birlashtiradi
│   │   ├── start.py          # /start, /help, inline callback
│   │   ├── form.py           # /form, FSM (so'rovnoma), /cancel
│   │   ├── admin.py          # /admin, /stats
│   │   └── echo.py           # Menyu tugmalari va echo
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── default.py        # main_menu_keyboard, cancel_keyboard
│   │   └── inline.py         # get_sample_inline_keyboard, SampleCallbackData
│   ├── middlewares/
│   │   ├── __init__.py
│   │   └── logging.py        # LoggingMiddleware
│   ├── states/
│   │   ├── __init__.py
│   │   └── user_state.py     # UserFormState (name, age, feedback)
│   ├── __init__.py
│   └── config.py             # Settings (BOT_TOKEN, ADMIN_IDS, LOGGING_LEVEL)
├── .dockerignore
├── .env.example              # .env namunasi
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py                   # Kirish nuqtasi
├── README.md
└── requirements.txt
```

---

## 🚀 Ishga Tushirish

### 1. `.env` faylini yarating
```bash
cp .env.example .env
```
`.env` ichiga tokeningizni yozing:
```env
BOT_TOKEN=123456789:ABCdef...
ADMIN_IDS=12345678
LOGGING_LEVEL=INFO
```

### 2. Docker orqali (tavsiya etiladi)
```bash
docker compose up --build -d   # ishga tushirish
docker compose logs -f          # loglarni ko'rish
docker compose down             # to'xtatish
```

### 3. Local (Docker-siz)
```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🔧 Kengaytirish

| Nima qo'shmoqchisiz?     | Qaysi faylni o'zgartirish kerak? |
|--------------------------|----------------------------------|
| Yangi buyruq / handler   | `bot/handlers/` papkasida yangi `.py` yarating va `__init__.py` ga qo'shing |
| Yangi tugma              | `bot/keyboards/default.py` yoki `inline.py` |
| Yangi FSM holati         | `bot/states/user_state.py` |
| Yangi DB jadvali         | `bot/database/db.py` |

---

## 📄 Litsenziya

Ochiq kodli shablon — tijorat va shaxsiy loyihalarda erkin foydalaning.
