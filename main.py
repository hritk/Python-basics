print('welcome to the game')
msg="gameover"
next="you win"
ques1 = input("where to go left or right \n")
if ques1 == 'right':
  print(msg)
else:
  ques2 =input("swim or what \n")  
  if ques2 == 'swim':
    print(msg)
  else:
    a =input("which door you want red blue or yellow \n")  
    if a == "yellow" :
      print(next)
    elif a == "blue" :
      print(msg)
    else:
      print(msg)   
