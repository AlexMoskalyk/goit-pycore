import sys
import re
from collections import defaultdict
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    """Парсить рядок логу та повертає словник з компонентами: дата, час, рівень, повідомлення."""
    parts = line.strip().split(maxsplit=3)
    if len(parts) == 4:
        date, time, level, message = parts
        return {"date": date, "time": time, "level": level, "message": message}
    return {}

def load_logs(file_path: str) -> List[dict]:
    """Завантажує лог-файл та повертає список розібраних записів."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """Фільтрує логи за вказаним рівнем."""
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """Виводить кількість записів для кожного рівня логування у вигляді таблиці."""
    print(f"{'Рівень логування':<20} | {'Кількість':<10}")
    print("-" * 32)
    for level, count in counts.items():
        print(f"{level:<20} | {count:<10}")

def display_filtered_logs(logs: List[dict], level: str):
    """Виводить деталі логів для конкретного рівня."""
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    """Основна функція для запуску скрипта."""
    if len(sys.argv) < 2:
        print("Використання: python code.py path/to/logs.log ")
        sys.exit(1)

    log_file = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_filtered_logs(filtered_logs, level_filter)

if __name__ == "__main__":
    main()
