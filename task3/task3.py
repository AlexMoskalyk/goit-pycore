import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows
init(autoreset=True)

def print_tree(directory: Path, prefix=""):
    """
    Виводить дерево директорій, ігноруючи папки `.venv` та `.git`.
    Використовує pathlib для роботи з файловою системою та colorama для кольорів.
    """
    # Ігнорування папок `.venv` та `.git`
    ignore_folders = {".venv", ".git"}
    if directory.name in ignore_folders:
        return

    # Вивід назви директорії
    print(f"{prefix}{Fore.BLUE}📂 {directory.name}{Style.RESET_ALL}")

    try:
        # Отримання списку файлів та папок
        entries = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name))
    except PermissionError:
        # Вивід повідомлення, якщо доступ заборонений
        print(f"{prefix}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")
        return

    # Рекурсивний обхід вмісту директорії
    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "┗━ " if is_last else "┣━ "
        if entry.is_dir():
            print_tree(entry, prefix + connector)
        else:
            print(f"{prefix + connector}{Fore.GREEN}📜 {entry.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    # Отримання шляху з командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.{Style.RESET_ALL}")
        sys.exit(1)
    
    root_dir = Path(sys.argv[1])
    if not root_dir.exists() or not root_dir.is_dir():
        print(f"{Fore.RED}Шлях {root_dir} не є дійсною директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print_tree(root_dir)
