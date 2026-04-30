
def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                
                if not line:
                    continue  # пропускаємо пусті рядки

                parts = line.split(',')

                if len(parts) != 2:
                    continue  # пошкоджений рядок

                name, salary = parts

                try:
                    total += int(salary)
                    count += 1
                except ValueError:
                    continue  # якщо зарплата не число

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Помилка: файл не знайдено")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return (0, 0)
    