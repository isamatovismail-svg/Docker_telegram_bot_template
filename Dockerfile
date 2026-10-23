# ==============================================================
# 1. Base image: Python 3.11 slim (kichik va tez)
# ==============================================================
FROM python:3.11-slim

# ==============================================================
# 2. Environment o'zgaruvchilar
#    - PYTHONDONTWRITEBYTECODE: .pyc fayllar yozilmaydi
#    - PYTHONUNBUFFERED: stdout/stderr buferlanmaydi (real-time logs)
# ==============================================================
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ==============================================================
# 3. Konteyner ichidagi ishchi katalog
# ==============================================================
WORKDIR /app

# ==============================================================
# 4. Faqat requirements.txt ni avval ko'chirish (Docker cache uchun)
# ==============================================================
COPY requirements.txt .

# ==============================================================
# 5. Pip yangilash va kutubxonalarni o'rnatish
# ==============================================================
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==============================================================
# 6. Barcha loyiha fayllarini ko'chirish
# ==============================================================
COPY . .

# ==============================================================
# 7. data/ papkasini yaratib qo'yish (SQLite uchun)
# ==============================================================
RUN mkdir -p /app/data

# ==============================================================
# 8. Botni ishga tushirish
# ==============================================================
CMD ["python", "main.py"]
