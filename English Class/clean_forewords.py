import os

def clean_foreword(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Убираем пустые строки и строки, состоящие только из пробелов
    non_empty_lines = [line for line in lines if line.strip() != '']

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(non_empty_lines)

    print(f"✅ Очищено: {filepath}")

def main():
    root_dir = os.getcwd()

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Игнорируем служебные папки
        if '__pycache__' in dirpath or '.git' in dirpath:
            continue
        for filename in filenames:
            if filename == '00. Foreword.txt':
                filepath = os.path.join(dirpath, filename)
                clean_foreword(filepath)

    print("🎉 Готово! Все foreword очищены.")

if __name__ == "__main__":
    main()