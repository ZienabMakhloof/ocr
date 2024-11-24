# استخدم صورة Python الرسمية
FROM python:3.10-slim

# تعيين مسار العمل
WORKDIR /app

# نسخ متطلبات المشروع
COPY requirements.txt .

# تثبيت المكتبات المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ جميع الملفات إلى الحاوية
COPY . .

# تعيين الأمر الذي سيتم تشغيله عند بدء الحاوية
CMD ["python", "app.py"]
