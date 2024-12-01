from pathlib import Path

def get_cats_info():
    try:
        # Перетворюємо шлях на об'єкт Path
        current_dir = Path(__file__).parent
        
        file_path = current_dir / "cats.txt"
        
        if not file_path.is_file():
            raise FileNotFoundError("Файл не знайдено. Перевірте шлях до файлу.")
        
        cats = []
        
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line.strip()}")
                    continue
        
        return cats
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info()
    
    if cats_info:  
        print("Інформація про котів:")
        for cat in cats_info:
            print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
    else:
        print("Список котів порожній або файл не знайдено.")