name = input()
hero_class = input()
health = int(input())
armor = int(input())
damage = float(input())

print(f"=== Создание героя ===\n\nИмя: {name}\nКласс: {hero_class}\nЗдоровье: {health}, "
      f"Броня: {armor}, Урон: {damage}\n")

guard_health = int(input())  # Здоровье стражника
guard_armor = int(input())  # Броня стражника
guard_damage = float(input())  # Базовый урон стражника

magic_damage = (damage * 1.5) - guard_armor
guard_attack = (guard_damage * 1.2) - armor

print(f"=== Магическое противостояние ===\n\n{name} использовал магическую атаку и нанёс стражнику "
      f"{round(magic_damage, 1)} урона!\nЗдоровье стражника теперь: {round(guard_health - magic_damage, 1)}\n"
      f"Стражник атаковал героя и нанёс {round(guard_attack, 1)} урона!\nЗдоровье героя теперь: {health - guard_attack}")

copper_coins = int(input())

total_weight_before = copper_coins * 25.6
gold_coins = round(copper_coins / 336)
silver_coins = round((copper_coins - gold_coins * 336) / 28)
copper_coins -= (gold_coins * 336 + silver_coins * 28)
total_weight_after = gold_coins * 31.103 + silver_coins * 16.4 + copper_coins * 25.6

print(f"=== Лут ===\n\nВес до обмена: {round(total_weight_before, 2)}\nЗолото: {gold_coins}, Серебро: {silver_coins}, "
      f"Медь: {copper_coins}\nВес после обмена: {round(total_weight_after, 2)}")

import math

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"=== Я свободен! ===\n\nРасстояние между мной ({x1}; {y1}) и ближайшим поселением ({x2}; {y2}) составляет "
      f"{round(distance, 2)} точек")

cnt1, amount1 = int(input()), int(input())
cnt2, amount2 = int(input()), int(input())
cnt3, amount3 = int(input()), int(input())

print(f"=== Травушки-муравушки ===\n\nОжидаемая прибыль: {max(cnt1 * amount1, cnt2 * amount2, cnt3 * amount3)} медяков")
