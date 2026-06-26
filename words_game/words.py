import tkinter as tk
from tkinter import messagebox
import os

class WordGameApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x450")
        self.root.resizable(True, True)
        
        # Загружаем словарь из файла
        self.words = self.load_words()
        
        # Переменные
        self.base_word = tk.StringVar(value="краскораспылительница")
        self.input_word = tk.StringVar()
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Привязываем клавишу Enter
        self.root.bind('<Return>', self.check_word_event)
        
        # Фокус на поле ввода
        self.word_entry.focus()
    
    def load_words(self):
        """Загружает слова из файла words.txt"""
        words = []
        filename = "words.txt"
        
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    words = [line.strip().lower() for line in f if line.strip()]
                print(f"✅ Загружено {len(words)} слов из {filename}")
            except Exception as e:
                print(f"⚠️ Ошибка загрузки файла: {e}")
                words = []
        else:
            # Если файла нет, создаем пример
            print(f"⚠️ Файл {filename} не найден. Создаем пример...")
            example_words = [
                "яблоко", "банан", "груша", "апельсин", "мандарин",
                "арбуз", "дыня", "виноград", "клубника", "малина"
            ]
            self.save_words(example_words)
            words = example_words
        
        return words
    
    def save_words(self, words):
        """Сохраняет слова в файл"""
        try:
            with open("words.txt", 'w', encoding='utf-8') as f:
                for word in words:
                    f.write(word + '\n')
            print("✅ Слова сохранены в words.txt")
        except Exception as e:
            print(f"⚠️ Ошибка сохранения: {e}")
    
    def count_letters(self, word):
        """Подсчитывает количество каждой буквы в слове"""
        letter_count = {}
        for letter in word.lower():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count
    
    def can_form_word(self, word, base_letters):
        """Проверяет, можно ли составить слово из букв базового слова"""
        word_letters = self.count_letters(word.lower())
        
        for letter, count in word_letters.items():
            if letter not in base_letters or base_letters[letter] < count:
                return False
        return True
    
    def check_word(self, word):
        """Проверяет слово по всем критериям"""
        word = word.strip().lower()
        
        if word == "":
            return "⚠️ Пожалуйста, введите слово!"
        
        # Проверка на составление из букв
        base = self.base_word.get().strip().lower()
        if not base:
            return "⚠️ Пожалуйста, введите базовое слово!"
        
        base_letters = self.count_letters(base)
        
        if not self.can_form_word(word, base_letters):
            return f"❌ НЕЛЬЗЯ составить из букв слова '{base}'"
        
        # Проверка наличия в словаре
        if word in self.words:
            return f"❌ Слово '{word}' ЕСТЬ в словаре"
        else:
            return f"✅ Слово '{word}' НЕТ в словаре (можно использовать!)"
    
    def create_widgets(self):
        """Создает все элементы интерфейса"""
        
        # Главный фрейм
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Заголовок
        title = tk.Label(
            main_frame,
            text="🔍 Игра в слова",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(0, 15))
        
        # Базовое слово
        base_frame = tk.Frame(main_frame)
        base_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            base_frame,
            text="📖 Базовое слово:",
            font=("Arial", 10, "bold")
        ).pack(anchor=tk.W)
        
        base_entry = tk.Entry(
            base_frame,
            textvariable=self.base_word,
            font=("Arial", 12),
            width=40,
            relief=tk.SUNKEN,
            bd=2
        )
        base_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Кнопка для обновления базового слова
        update_base_btn = tk.Button(
            base_frame,
            text="Обновить базовое слово",
            command=self.update_base_word,
            bg="#E8F4F8",
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        update_base_btn.pack(pady=(5, 0), anchor=tk.E)
        
        # Разделитель
        tk.Frame(main_frame, height=2, bg="#CCCCCC").pack(fill=tk.X, pady=10)
        
        # Поле для ввода слова
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            input_frame,
            text="✏️ Введите слово:",
            font=("Arial", 10, "bold")
        ).pack(anchor=tk.W)
        
        entry_frame = tk.Frame(input_frame)
        entry_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.word_entry = tk.Entry(
            entry_frame,
            textvariable=self.input_word,
            font=("Arial", 14),
            width=40,
            relief=tk.SUNKEN,
            bd=2
        )
        self.word_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        check_btn = tk.Button(
            entry_frame,
            text="✅ Проверить",
            command=self.check_word_callback,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            bd=2,
            cursor="hand2",
            padx=15
        )
        check_btn.pack(side=tk.RIGHT)
        
        # Результат
        result_frame = tk.Frame(main_frame)
        result_frame.pack(fill=tk.X, pady=(5, 15))
        
        self.result_label = tk.Label(
            result_frame,
            text="Введите слово для проверки",
            font=("Arial", 13),
            wraplength=600,
            justify=tk.LEFT,
            bg="#F5F5F5",
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=10
        )
        self.result_label.pack(fill=tk.X)
        
        # Статистика
        stats_frame = tk.Frame(main_frame)
        stats_frame.pack(fill=tk.X, pady=(5, 0))
        
        stats_frame_inside = tk.Frame(stats_frame, bg="#E8F4F8", relief=tk.RAISED, bd=2)
        stats_frame_inside.pack(fill=tk.X, padx=5, pady=5)
        
        self.stats_label = tk.Label(
            stats_frame_inside,
            text=self.get_stats_text(),
            font=("Arial", 10),
            bg="#E8F4F8",
            padx=10,
            pady=8
        )
        self.stats_label.pack(anchor=tk.W)
        
        # Привязываем Esc для очистки
        self.root.bind('<Escape>', self.clear_input)
    
    def get_stats_text(self):
        """Возвращает текст со статистикой"""
        base = self.base_word.get().strip()
        if base:
            base_letters = self.count_letters(base)
            total = sum(base_letters.values())
            unique = len(base_letters)
            return f"📊 Базовое слово: {base} | Букв: {total} | Уникальных: {unique} | Слов в словаре: {len(self.words)}"
        else:
            return f"📊 Базовое слово не задано | Слов в словаре: {len(self.words)}"
    
    def update_base_word(self):
        """Обновляет базовое слово"""
        base = self.base_word.get().strip()
        if base:
            self.stats_label.config(text=self.get_stats_text())
            self.result_label.config(
                text=f"✅ Базовое слово обновлено: '{base}'",
                bg="#E8F4F8"
            )
            self.word_entry.focus()
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, введите базовое слово!")
    
    def check_word_callback(self):
        """Обработчик нажатия кнопки проверки"""
        word = self.input_word.get()
        result = self.check_word(word)
        self.result_label.config(text=result)
        
        # Меняем цвет фона в зависимости от результата
        if "✅" in result:
            self.result_label.config(bg="#E8F5E9")  # Светло-зеленый
        elif "❌" in result:
            self.result_label.config(bg="#FFEBEE")  # Светло-красный
        else:
            self.result_label.config(bg="#FFF3E0")  # Светло-оранжевый
        
        # Очищаем поле ввода
        self.input_word.set("")
        self.word_entry.focus()
    
    def check_word_event(self, event):
        """Обработчик нажатия Enter"""
        self.check_word_callback()
    
    def clear_input(self, event):
        """Очищает поле ввода"""
        self.input_word.set("")
        self.word_entry.focus()
        return "break"

def main():
    root = tk.Tk()
    app = WordGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()