board = list(range(1,10)) #Поле

def draw_board(board): #Процедура создания поля
    for i in range(3):# Цикл строк 3 шт.
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|") # Создание клеток 3 шт.

def take_input(player_token): #Процедура хода, зависит от x/o
    valid = False # По умолчанию пользователь ввел неправильное значение
    while not valid: #Цикл, пока пользователь не введет правильное значение
        player_answer = input("Put " + player_token) # Спрашиваем у пользователя, куда поставить x/o
        try:
            player_answer = int(player_answer) #Проверка, ввел ли пользователь число
        except:
            print ("Error. Enter a number") # Если строчка оказалась не числом, то просим пользователя ввести число
            continue
        if player_answer >= 1 and player_answer <= 9: # Проверяем, попадает ли введеное пльзователем число в поле
            if (str(board[player_answer-1]) not in "XO"): # Проверяем, занята ли клетка, куда пользователь хочет сходить
                board[player_answer-1] = player_token # Если пользователь ввел корректное число, то в нужную ячейку ставим x/o
                valid = True
            else:
                print ("Error. The cell is busy. Enter another number") #Если клетка занята, то просим ввести другое число
        else:
            print ("Error. Enter another number.") # Если чило не попадает в диапазон клеток 1-9, то просим ввести другое число

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # Кортеж значений-"победителей"
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board): # Основная процедура
    counter = 0 # К-во ходов
    win = False # Сначала никто не победил
    while not win:
        draw_board(board)
        if counter % 2 == 0: # Проверка, какой по счету ход (т. к. 2 игрока)
            take_input("X")# X - 1,3,5... ход
        else:
            take_input("O")# O - 2,4,6... ход
        counter += 1 # Ход закончен, переход на следующий
        if counter > 4: # Выиграть можно только после 4-ого хода
            tmp = check_win(board)
            if tmp:
                print (tmp, "wins!") # Вывод: x/o победил!
                win = True # x/o одержал победу
                break # Цикл прерывается,  одержал победу
        if counter == 9: # Если все клетки заняты и никто не победил, то ничья
            print ("Draw!") # Вывод: Ничья
            break # Цикл прерывается (игра закончена, но никто не победил)
    draw_board(board) #"Перерисование" доски

main(board) #Вызов основной процедуры