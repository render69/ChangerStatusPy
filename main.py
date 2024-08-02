from pypresence import Presence
import time

# Вставьте сюда ваш Application ID
client_id = 'Application ID'
RPC = Presence(client_id)
RPC.connect()

# Установить кастомный статус
RPC.update(
    state="Ваше состояние", # Краткое описание состояния
    details="Подробности вашего состояния", # Детальное описание
    large_image="large_image_key", # Ключ большого изображения
    large_text="Описание большого изображения", # Описание при наведении на большое изображение
    small_image="small_image_key", # Ключ маленького изображения
    small_text="Описание маленького изображения", # Описание при наведении на маленькое изображение
)

print("Кастомный статус установлен. Нажмите Ctrl+C для выхода.")
try:
    while True:
        time.sleep(15) # Discord требует обновление статуса каждые 15 секунд
except KeyboardInterrupt:
    print("Выход...")
