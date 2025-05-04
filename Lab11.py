#Завдання 1
phonebook = [
    {"ім'я": "Іван", "прізвище": "Шевченко", "телефон": "0671112233", "місто": "Київ"},
    {"ім'я": "Марія", "прізвище": "Іваненко", "телефон": "0503334455", "місто": "Львів"},
    {"ім'я": "Олег", "прізвище": "Коваль", "телефон": "0739876543", "місто": "Одеса"},
    {"ім'я": "Анна", "прізвище": "Петренко", "телефон": "0935556677", "місто": "Київ"},
    {"ім'я": "Наталя", "прізвище": "Мельник", "телефон": "0991122334", "місто": "Харків"}
]

print("=== Завдання 1: Повна телефонна книга ===")
print(f"{'Ім\'я':<10} {'Прізвище':<15} {'Телефон':<12} {'Місто':<10}")
for contact in phonebook:
    print(f"{contact['ім\'я']:<10} {contact['прізвище']:<15} {contact['телефон']:<12} {contact['місто']:<10}")

#Завдання 2
print("\n=== Завдання 2: Пошук контактів ===")
try:
    parameter = input("Введіть параметр пошуку (ім'я, прізвище або місто): ").strip().lower()
    if not parameter:
        raise ValueError("Порожній ввід!")

    value = input(f"Введіть значення для {parameter}: ").strip()
    if not value:
        raise ValueError("Порожнє значення для пошуку!")

    found = False
    for contact in phonebook:
        if contact.get(parameter, "").lower() == value.lower():
            print(f"{contact['ім\'я']} {contact['прізвище']} | Телефон: {contact['телефон']} | Місто: {contact['місто']}")
            found = True
    if not found:
        print("Контакти не знайдено.")
except ValueError as ve:
    print("Помилка:", ve)
except Exception:
    print("Неправильний параметр пошуку.")

#Завдання 3
print("\n=== Завдання 3: Оновлення, видалення та аналітика ===")
name_to_update = input("Введіть ім’я контакту для оновлення або видалення: ").strip()
found = False

for contact in phonebook:
    if contact['ім\'я'].lower() == name_to_update.lower():
        found = True
        action = input("Бажаєте оновити чи видалити контакт? (оновити/видалити): ").strip().lower()
        if action == "оновити":
            new_phone = input("Новий номер телефону: ").strip()
            new_city = input("Нове місто: ").strip()
            confirm = input("Підтвердити оновлення? (так/ні): ").strip().lower()
            if confirm == "так":
                contact["телефон"] = new_phone
                contact["місто"] = new_city
                print("Контакт оновлено.")
        elif action == "видалити":
            confirm = input("Підтвердити видалення? (так/ні): ").strip().lower()
            if confirm == "так":
                phonebook.remove(contact)
                print("Контакт видалено.")
        break

if not found:
    print("Контакт не знайдено.")

# Аналітика
cities = set(contact["місто"] for contact in phonebook)
print("\nУнікальні міста:", cities)

city_counts = {}
for contact in phonebook:
    city = contact["місто"]
    city_counts[city] = city_counts.get(city, 0) + 1

print("\nКількість контактів у кожному місті:")
for city, count in city_counts.items():
    print(f"{city}: {count}")

most_common_city = max(city_counts, key=city_counts.get)
print(f"\nМісто з найбільшою кількістю контактів: {most_common_city}")
