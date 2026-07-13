import os
import re

def collect_poetry_collection(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        # Сортируем папки, чтобы сохранить порядок 01, 02, 03...
        folders = sorted([f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f))])

        for folder in folders:
            # Проверяем, что папка соответствует формату "01. Rudyard Kipling"
            match = re.match(r"(\d+)\.\s(.+)", folder)
            if not match:
                continue
            number = match.group(1)
            author_name = match.group(2)

            author_path = os.path.join(root_dir, folder)

            # --- ТИТУЛЬНЫЙ ЛИСТ АВТОРА ---
            out.write(f"{author_name}\n")
            out.write(f"{'~' * len(author_name)}\n")
            out.write(f"Автор №{number}\n\n")
            out.write("\f")  # Разрыв страницы

            # --- ПРЕДИСЛОВИЕ ---
            foreword_path = os.path.join(author_path, "00. Foreword.txt")
            if os.path.exists(foreword_path):
                with open(foreword_path, 'r', encoding='utf-8') as f:
                    foreword_text = f.read().strip()
                if foreword_text:
                    out.write("ПРЕДИСЛОВИЕ\n")
                    out.write("-----------\n")
                    out.write(foreword_text)
                    out.write("\n\n")
                    out.write("\f")  # Разрыв страницы после предисловия

            # --- СТИХОТВОРЕНИЯ ---
            # Собираем все файлы, кроме foreword
            poem_files = sorted([f for f in os.listdir(author_path) if f.endswith('.txt') and f != '00. Foreword.txt'])

            for poem_file in poem_files:
                poem_path = os.path.join(author_path, poem_file)

                # Извлекаем название стихотворения из имени файла
                title_match = re.match(r"\d+\.\s(.+)\.txt", poem_file)
                if not title_match:
                    continue
                poem_title = title_match.group(1)

                # Читаем содержимое стихотворения (там уже есть заголовок)
                with open(poem_path, 'r', encoding='utf-8') as f:
                    poem_content = f.read().strip()

                # Если вдруг в файле нет заголовка — добавляем
                if not poem_content.startswith(poem_title):
                    out.write(f"{poem_title}\n\n")
                out.write(poem_content)
                out.write("\n\n")
                out.write("\f")  # Каждое стихотворение с новой страницы

    print(f"✅ Сборник собран: {output_file}")

if __name__ == "__main__":
    root = os.getcwd()  # или укажи путь вручную
    output = "poetry_collection.txt"
    collect_poetry_collection(root, output)
    print("📄 Теперь открой poetry_collection.txt в Word и сохрани как .docx")