"""
Главный файл программы.
Только запуск основной логики.
"""

from automaton.manager import AutomatonManager


def main():
    """Основная функция программы."""
    try:
        automaton = AutomatonManager()
        automaton.run()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена")
    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()