import os
import django

# Спочатку налаштування середовища
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "m3l4.settings")
django.setup()

# Тепер можна імпортувати моделі
from users.models import User

# Приклад створення користувача
user = User(name="Roma", email="Roma@gmail.com", role="admin")
user.save()
