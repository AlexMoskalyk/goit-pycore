from pathlib import Path

def total_salary():
    try:
        current_dir = Path(__file__).parent
        
        salary_file = current_dir / "salary_file.txt"
        
        if not salary_file.is_file():
            raise FileNotFoundError("Файл 'salary_file.txt' не знайдено у поточній директорії.")
        
        with salary_file.open('r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line.strip()}")
                    continue
            
            if not salaries:
                raise ValueError("Файл порожній або всі рядки мають некоректний формат.")
            
            total = sum(salaries)
            average = total / len(salaries)
            
            return total, average
    except FileNotFoundError as e:
        print(e)
        return None, None
    except ValueError as e:
        print(e)
        return None, None
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        return None, None

if __name__ == "__main__":
    total, average = total_salary()
    if total is not None and average is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
