import sys
from typing import List, Dict
import os

def parse_log_line(line: str) -> Dict[str, str]:
    """Парсує рядок логу у словник з компонентами: дата, час, рівень, повідомлення."""
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Завантажує лог-файл і парсує всі рядки."""
    logs = []
    try:
        with open(file_path, "r") as file:
            logs = [parse_log_line(line) for line in file if line.strip()]
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """Фільтрує логи за заданим рівнем логування."""
    return [log for log in logs if log.get("level") == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """Виводить статистику за рівнями логування."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")

def main():
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Використання: python main.py /Users/mac/Desktop/goit-algo-hw-05/task_3.py [level]")
        return

    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Завантажуємо логи
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено.")
        return

    logs = load_logs(file_path)

    # Підрахунок кількості записів за рівнями
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо користувач вказав рівень логування, фільтруємо і виводимо деталі
    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()