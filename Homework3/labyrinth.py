import random
from typing import List

N = 4
MAX_HEALTH = 3
MAX_INVENTORY = 8
ROOM_TYPES = ["пусто", "сундук", "монстр", "ловушка", "ключ", "руна", "охранник"]
ROOM_WEIGHTS = [35, 25, 15, 15, 5, 5, 10]
ITEM_POOL = ["зелье", "камень", "монета", "меч", "щит"]

def join_inv(inv: List[str]):
    return ", ".join(inv) if inv else "пустой"

def generate_chest():
    return [random.choice(ITEM_POOL) for _ in range(random.randint(1, 3))]

def generate_room():
    return random.choices(ROOM_TYPES, weights=ROOM_WEIGHTS, k=1)[0]

def generate_labyrinth():
    labyrinth = [[generate_room() for _ in range(N)] for _ in range(N)]
    labyrinth[0][0] = "пусто"
    labyrinth[N-1][N-1] = "портал"
    while True:
        key_pos = (random.randint(0, N-1), random.randint(0, N-1))
        if key_pos != (0,0) and key_pos != (N-1,N-1):
            labyrinth[key_pos[0]][key_pos[1]] = "ключ"
            break
    while True:
        rune_pos = (random.randint(0, N-1), random.randint(0, N-1))
        if rune_pos != (0,0) and rune_pos != (N-1,N-1) and rune_pos != key_pos:
            labyrinth[rune_pos[0]][rune_pos[1]] = "руна"
            break
    return labyrinth

def handle_room(room: str, inventory: List[str], health: int):
    if room == "пусто":
        print("Комната пустая.")
    elif room == "сундук":
        chest = generate_chest()
        print("Вы нашли сундук! Внутри:", ", ".join(chest))
        print("Что взять?")
        print("1) Всё")
        print("2) Конкретный предмет")
        print("3) Не брать")
        choice = input("Выбор: ").strip()
        if choice == "1":
            inventory.extend(chest)
            if len(inventory) > MAX_INVENTORY:
                dropped = inventory.pop()
                print(f"Инвентарь переполнен, вы случайно уронили: {dropped}")
            print("Вы взяли всё.")
        elif choice == "2":
            for idx, item in enumerate(chest, 1):
                print(f"{idx}) {item}")
            while True:
                sel = input("Номер предмета: ").strip()
                if sel.isdigit() and 1 <= int(sel) <= len(chest):
                    inventory.append(chest[int(sel)-1])
                    print(f"Вы взяли: {chest[int(sel)-1]}")
                    break
        else:
            print("Вы ничего не взяли.")
    elif room == "монстр":
        if "меч" in inventory:
            print("Монстр! Но у вас есть меч — вы отбиваетесь, не теряете жизнь.")
        else:
            health -= 1
            if health > 0:
                print(f"Монстр атакует! Жизней осталось: {health}")
            else:
                print("Монстр атакует!\nЖизней нет. Игра окончена.")
    elif room == "ловушка":
        health -= 1
        if health > 0:
            print(f"Ловушка! Жизней осталось: {health}")
        else:
            print("Ловушка! Жизней нет. Игра окончена.")
    elif room == "ключ":
        if "ключ" not in inventory:
            inventory.append("ключ")
            print("Вы нашли ключ!")
    elif room == "руна":
        if "руна" not in inventory:
            inventory.append("руна")
            print("Вы нашли руну!")
    elif room == "охранник":
        print("Перед вами пост охраны.")
        if "зелье" in inventory:
            health -= 1
            if health > 0:
                print(f"Охранник жестко дерется за зелье! Жизней осталось: {health}")
            else:
                print("Охранник жестко дерется за зелье! Жизней нет. Игра окончена.")
        else:
            print("Охранник пропускает вас.")
    elif room == "портал":
        if "ключ" in inventory and "руна" in inventory:
            print("Вы используете ключ и руну. Портал открывается! Победа!")
        else:
            print("Портал закрыт. Нужны ключ и руна.")
    return health

def game() -> None:
    labyrinth = generate_labyrinth()
    pos = [0, 0]
    inventory: List[str] = []
    health = MAX_HEALTH
    print("Добро пожаловать в Лабиринт! Двигайтесь w/a/s/d, i — инвентарь, q — выйти. Цель: дойти до портала.")

    while health > 0:
        x, y = pos
        room = labyrinth[x][y]
        health = handle_room(room, inventory, health)
        if health <= 0:
            return

        print(f"Инвентарь: {join_inv(inventory)}")
        move = input("Куда идти? (w/a/s/d): ").strip().lower()
        if move == "w" and x > 0:
            pos[0] -= 1
        elif move == "s" and x < N-1:
            pos[0] += 1
        elif move == "a" and y > 0:
            pos[1] -= 1
        elif move == "d" and y < N-1:
            pos[1] += 1
        elif move == "i":
            print("Инвентарь:", join_inv(inventory))
        elif move == "q":
            print("Вы вышли из игры.")
            return
        else:
            print("Невозможное движение или пустой ввод.")

if __name__ == "__main__":
    game()
