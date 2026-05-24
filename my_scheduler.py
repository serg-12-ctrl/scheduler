import schedule
import time
from datetime import datetime

def test_job():
    
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f" Тест успешный! Функция сработала в: {current_time}")

    if datetime.now().day == 24:
        print(f"Задача выполнена! Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#schedule.every(5).seconds.do(test_job)
schedule.every().day.at("16:07").do(test_job)


print("Планировщик запущен. Ждем...")

while True:
    schedule.run_pending()
    time.sleep(1)
