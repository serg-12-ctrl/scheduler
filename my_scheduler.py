import schedule
import time
from datetime import datetime

def job():
    print(f"Задача выполнена! Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
