import random
print("this is tic tac toe,")
squares = ["top left" , "top middle" , "top right", "middle left", "middle"," middle right"," bottom left", "bottom middle", "bottom right"]
usedSquares = ['']
usermoveArray = [""]
win = 0
while win == 0:
  print("Pick a square," + str(squares))
  usermove = input(" ")
  if(usermove not in squares):
    print("please enter a square listed, " + str(squares))
    usermove = input("")
  computerChoice = random.choice(squares)
  print("the computer chose " + str(computerChoice))  
  usermoveArray.append(usermove)
 
  if usermove == "top left":
    squares.remove(usermove)
  if usermove == "top right":
    squares.remove(usermove)
  if usermove == "top middle":
    squares.remove(usermove)
  if usermove == "middle left":
    squares.remove(usermove)
  if usermove == "middle right":
    squares.remove(usermove)
  if usermove == "middle":
    squares.remove(usermove)
  if usermove == "bottom middle":
    squares.remove(usermove)
  if usermove == "bottom left":
    squares.remove(usermove)
  if usermove == "bottom right":
    squares.remove(usermove)

  if("top left" in usermoveArray and "top middle" in usermoveArray and "top right" in usermoveArray):
    print("you win!! u had all top")
    win = 1
  if("middle right" in usermoveArray and "middle" in usermoveArray and "middle left" in usermoveArray):
    print("you win!! u had all middle")
    win = 1
  if("bottom left" in usermoveArray and "bottom middle" in usermoveArray and "bottom right" in usermoveArray):
    print("you win!! u had all bottom squares")
    win = 1
  if("top left " in usermoveArray and "middle left" in usermoveArray and "bottom left"):
    print("you win!! u had all left squares")
    win = 1
  if("top right"in usermoveArray and "middle right" in usermoveArray and "bottom right"in usermoveArray):
    print("you win!! u had all right squares")
    win = 1
  if("top middle" in usermoveArray and "middle" in usermoveArray and "botton middle" in usermoveArray):
    print("you win!! u had all right squares")
    win = 1
  if("top left" in usermoveArray and "middle" in usermoveArray and "bottom right" in usermoveArray):
    print("you win!! u had diganal from top left to bottom right")
    win = 1
  if("top right" in usermoveArray and "middle" in usermoveArray and "bottom left" in usermoveArray):
    print("you win!! u had diganal from top right to bottom left")
    win = 1
  
  usedSquares.append(computerChoice)
  usedSquares.append(usermoveArray)
  print("you can't choose, " + str(usedSquares))
