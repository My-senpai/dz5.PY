# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def drawBoard(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def takeInput(playerToken):
   valid = False
   while not valid:
      playerAnswer = input("Куда поставим " + playerToken+"? ")
      try:
         playerAnswer = int(playerAnswer)
      except:
         print("Некорректный ввод. Это не число")
         continue
      if playerAnswer >= 1 and playerAnswer <= 9:
         if(str(board[playerAnswer - 1]) not in "XO"):
            board[playerAnswer - 1] = playerToken
            valid = True
         else:
            print("Клетка занята")
      else:
        print("Некорректный ввод")

def checkWin(board):
   winCoord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in winCoord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def Game(board):
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
           takeInput("X")
        else:
           takeInput("O")
        counter += 1
        if counter > 4:
           win = checkWin(board)
           if win:
              print(win, "выиграл")
              win = True
              break
        if counter == 9:
            print("Ничья")
            break
    drawBoard(board)
Game(board)

input("Для выхода надо нажать на Enter")














