

def get_cats_info(path) -> dict:

    try:
        cats = []
        count = 0
        with open(path, 'r') as file:

            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')

                if len(parts) != 3:
                    continue
                    
                id_, name,age = parts
                cats.append({
                    "id": id_,
                    "name":name,
                    "age" : age,
                    })

                count += 1
        
        if count == 0:
            return cats
        
        return cats
 

    except FileNotFoundError:
        print("Помилка: файл не знайдено")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return [] 
            
cats_info = get_cats_info("text.txt")

print(cats_info)