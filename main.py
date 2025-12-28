"""
Главный файл программы.
Оптимизация: использование __main__ guard
"""

import sys
import time
from automaton.manager import AutomatonManager


def main():
    """Основная функция программы."""
    print("="*50)
    print("АВТОМАТНОЕ ПРОГРАММИРОВАНИЕ - ОПТИМИЗИРОВАННАЯ ВЕРСИЯ")
    print("="*50)
    print("Оптимизации:")
    print("• Кэширование вычислений")
    print("• Использование генераторов")
    print("• Эффективные структуры данных")
    print("• Минимизация аллокаций памяти")
    print("="*50)
    
    start_time = time.time()
    
    try:
        automaton = AutomatonManager()
        automaton.run()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена пользователем")
    except Exception as e:
        print(f"\nКритическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        end_time = time.time()
        print(f"\nВремя работы программы: {end_time - start_time:.2f} секунд")
        print("="*50)


if __name__ == "__main__":
    # Оптимизация: запуск через main guard
    main()