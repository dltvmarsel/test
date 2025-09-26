from abc import ABC, abstractmethod

# Базовый интерфейс
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


# Конкретные стратегии
class RegularStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price


class StudentStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.9


class PensionerStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.85


class VipStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.7


# Фабрика стратегий
def get_strategy(name: str) -> DiscountStrategy:
    strategies = {
        "regular":     RegularStrategy(),
        "student": StudentStrategy(),
        "pensioner": PensionerStrategy(),
        "vip": VipStrategy(),
    }
    return strategies.get(name.lower())


def main():
    print("Доступные стратегии: regular, student, pensioner, vip")

    while True:
        strategy_name = input("\nВведите стратегию (или 'exit' для выхода): ")
        if strategy_name.lower() == "exit":
            break

        strategy = get_strategy(strategy_name)
        if not strategy:
            print("Такой стратегии нет.")
            continue

        try:
            price = float(input("Введите цену товара: "))
            final_price = strategy.apply_discount(price)
            print(f"Итоговая цена: {final_price:.2f}")
        except ValueError:
            print("Ошибка: цена должна быть числом.")


if __name__ == "__main__":
    main()
