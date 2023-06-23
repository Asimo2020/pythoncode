for i in range(5):
 import random
 data_list = [ "meow","moo" ,"bark","quack" ,"buzz","tweet"]
 random_elements = random.choice(data_list)

 print(random_elements)

 user_guess=input ("Guess this sound is *** animal  ")

 if (random_elements == "meow" and user_guess=="cat") or (random_elements== "moo" and user_guess=="caw") or (random_elements == "bark" and user_guess=="dog") or (random_elements == "quack" and user_guess=="duck") or (random_elements == "buzz" and user_guess=="bee") or (random_elements == "tweet" and user_guess=="chiken"):
         print("that's correct")
 else:    
     print("that's wrong ")

print("well done")