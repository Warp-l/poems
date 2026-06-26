# Список слов для проверки (ваш массив из A2:K300)
WORDS = []

# Базовое слово для составления
BASE_WORD = "краскораспылительница"

def count_letters(word):
    """
    Подсчитывает количество каждой буквы в слове
    """
    letter_count = {}
    for letter in word.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def can_form_word(word, base_letters):
    """
    Проверяет, можно ли составить слово из букв базового слова
    """
    word_letters = count_letters(word.lower())
    
    for letter, count in word_letters.items():
        if letter not in base_letters or base_letters[letter] < count:
            return False
    return True

def check_word(word):
    """
    Проверяет слово по всем критериям
    """
    word = word.strip().lower()
    
    if word == "":
        return "⚠️  Вы не ввели слово!"
    
    # Проверка на составление из букв
    base_letters = count_letters(BASE_WORD)
    
    if not can_form_word(word, base_letters):
        return f"❌ Слово '{word}' НЕЛЬЗЯ составить из букв слова '{BASE_WORD}'"
    
    # Проверка наличия в массиве
    if word in WORDS:
        return f"❌ Слово '{word}' ЕСТЬ в массиве (красный)"
    else:
        return f"✅ Слово '{word}' НЕТ в массиве (зеленый)"

def show_base_word_info():
    """
    Показывает информацию о базовом слове
    """
    base_letters = count_letters(BASE_WORD)
    print(f"\n📖 Базовое слово: {BASE_WORD}")
    print(f"📊 Буквы в слове:")
    for letter, count in sorted(base_letters.items()):
        print(f"   '{letter}': {count} раз(а)")
    
    total_letters = sum(base_letters.values())
    unique_letters = len(base_letters)
    print(f"\n📊 Всего букв: {total_letters}")
    print(f"📊 Уникальных букв: {unique_letters}")

def main():
    print("=" * 70)
    print("🔍 ИГРА В СЛОВА")
    print("=" * 70)
    print(f"📖 Базовое слово: {BASE_WORD}")
    print(f"📊 Слов в словаре: {len(WORDS)}")
    print("💡 Правила:")
    print("   - Введите слово для проверки")
    print("   - Слово должно состоять только из букв базового слова")
    print("   - Каждая буква может использоваться столько раз, сколько есть в базовом слове")
    print("💡 Команды:")
    print("   - 'info' - показать информацию о базовом слове")
    print("   - 'exit' - выход")
    print("=" * 70)
    
    while True:
        # Ввод слова
        word = input("\n📝 Введите слово: ").strip()
        
        # Проверка на выход
        if word.lower() in ['exit', 'выход', 'quit']:
            print("\n👋 До свидания!")
            break
        
        # Проверка на информацию
        if word.lower() == 'info':
            show_base_word_info()
            continue
        
        # Проверка слова
        result = check_word(word)
        print(f"   {result}")

if __name__ == "__main__":
    main()