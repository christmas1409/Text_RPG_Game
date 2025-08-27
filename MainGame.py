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
