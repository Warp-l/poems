import os
import re

def add_title_to_file(filepath):
    # Получаем имя файла (например, "01. McAndrew's Hymn.txt")
    filename = os.path.basename(filepath)
    # Убираем номер в начале и расширение .txt
    # Ищем: цифры, точка, пробел, потом всё до .txt
    match = re.match(r"^\d+\.\s(.+)\.txt$", filename)
    if not match:
        print(f"⚠️ Пропускаю: {filename} (не соответствует шаблону)")
        return
    
    title = match.group(1).strip()  # "McAndrew's Hymn"

    # Читаем содержимое файла
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Формируем новое содержимое: заголовок + два переноса + исходный текст
    new_content = f"{title}\n\n{content}"

    # Записываем обратно в тот же файл
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Обработано: {filename}")

def main():
    # Корневая папка — там, где лежит этот скрипт
    root_dir = os.getcwd()

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Игнорируем папку со скриптом и служебные папки
        if '__pycache__' in dirpath or '.git' in dirpath:
            continue
        for filename in filenames:
            if filename.endswith('.txt') and filename != '00. Foreword.txt':
                filepath = os.path.join(dirpath, filename)
                add_title_to_file(filepath)

    print("🎉 Готово! Все файлы обработаны.")

if __name__ == "__main__":
    main()