def calculate_shopping_cart(items):
    total_cost = 0
    receipt = []
    for item in items:
        name, price, quantity = item
        item_total = price * quantity
        total_cost += item_total
        receipt.append((name, quantity, item_total))
    return total_cost, receipt
print("ТЕСТ 1: Обычная покупка")
cart1 = (
    ("Хлеб", 50, 2),
    ("Молоко", 80, 1),
    ("Яблоки", 120, 3)
)
total1, receipt1 = calculate_shopping_cart(cart1)
print(f"Общая стоимость: {total1} руб.")
print("Чек:")
for item in receipt1:
    print(f"  {item[0]} x{item[1]}: {item[2]} руб.")
print("\nТЕСТ 2: Покупка одного товара")
cart2 = (("Книга", 500, 1),)
total2, receipt2 = calculate_shopping_cart(cart2)
print(f"Общая стоимость: {total2} руб.")
print("Чек:")
for item in receipt2:
    print(f"  {item[0]} x{item[1]}: {item[2]} руб.")
print("\nТЕСТ 3: Пустая корзина")
cart3 = ()
total3, receipt3 = calculate_shopping_cart(cart3)
print(f"Общая стоимость: {total3} руб.")
print("Чек пуст" if not receipt3 else "В чеке есть товары")