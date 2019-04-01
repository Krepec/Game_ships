import random

random_ship_index = random.randint(0, 24)
result = list(range(0, 25))
end_game = True

def print_table():
    print(f" | {result[0]}  | {result[1]}  | {result[2]}  | {result[3]}  | {result[4]}  |")
    print(f" --------------------------")
    print(f" | {result[5]}  | {result[6]}  | {result[7]}  | {result[8]}  | {result[9]}  |")
    print(f" --------------------------")
    print(f" | {result[10]} | {result[11]} | {result[12]} | {result[13]} | {result[14]} |")
    print(f" --------------------------")
    print(f" | {result[15]} | {result[16]} | {result[17]} | {result[18]} | {result[19]} |")
    print(f" --------------------------")
    print(f" | {result[20]} | {result[21]} | {result[22]} | {result[23]} | {result[24]} |")
    print(f" --------------------------")

print_table()

def user_move():
    global end_game

    try:
        index = input("Podaj numer indeksu: ")
        chosen_index = int(index)
        if chosen_index == random_ship_index:
            print("Trafiony zatopiony")
            end_game = False
        elif chosen_index < 0 or chosen_index >24:
            print("Wybrano zły indeks!")
        else:
            result[chosen_index] = "X"
            print_table()
    except TypeError:
        print("Wpisz liczbę całkowitą")

while end_game:
    user_move()