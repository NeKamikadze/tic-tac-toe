print('Добро пожаловать в игру крестики-нолики!')

# Создание игрового поля
field = list(range(1, 10))

def draw_field(field):
    print()
    print('  ', field[0], '|', field[1], '|', field[2])
    print("-" * 15)
    print('  ', field[3], '|', field[4], '|', field[5])
    print("-" * 15)
    print('  ', field[6], '|', field[7], '|', field[8])
    print()

# Ввод данных игроков и проверка правильности ввода
def player_input(player_move):
    while True:
        move = input('Введите номер клетки, чтобы сделать ход: ')

        n = move

        if not (n.isdigit()):
            print('Необходимо ввести число!')
            continue

        n = int(n)

        if 1 > n > 9:
            print('Данный номер клетки отсутствует в диапазоне!')
            continue

        if 1 <= n <= 9:
            if str(field[n-1]) not in 'X0':
                field[n-1] = player_move
                return True
            else:
                print('Данная клетка занята!')
            continue

        return move

# Проверка выигрышных комбинаций
def check_win():
    win_row = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in win_row:
        if field[row[0]] == field[row[1]] == field[row[2]]:
            return field[row[0]]
    return False

# Игровой процесс
count = 0
while True:
    draw_field(field)
    if count % 2 == 0:
        print('Ходит игрок крестиками!')
        player_input('X')
    else:
        print('Ходит игрок ноликами!')
        player_input('0')
    count += 1
    if count > 4:
        draw_field(field)
        win = check_win()
        if win:
            print(f'Выиграл {win}!')
            break
    if count == 9:
        print('Ничья!')
        break
