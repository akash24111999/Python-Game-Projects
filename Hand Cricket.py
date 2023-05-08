# Hand Cricket

zero = """ 
  .oooo.   
 d8P'`Y8b  
888    888 
888    888 
888    888 
`88b  d88' 
 `Y8bd8P'  
 """

one = """
  .o  
o888  
 888  
 888  
 888  
 888  
o888o 
"""

two = """
  .oooo.   
.dP""Y88b  
      ]8P' 
    .d8P'  
  .dP'     
.oP     .o 
8888888888 
"""

three = """
  .oooo.   
.dP""Y88b  
      ]8P' 
    <88b.  
     `88b. 
o.   .88P  
`8bd88P' 
"""

four = """
      .o   
    .d88   
  .d'888   
.d'  888   
88ooo888oo 
     888   
    o888o 
"""

five = """
  oooooooo 
 ///
d88888b.   
    `Y88b  
      ]88  
o.   .88P  
`8bd88P'   
"""

six = """
   .ooo   
  .88'     
 d88'      
d888P"Ybo. 
Y88[   ]88 
`Y88   88P 
 `88bod8' 
"""
images_hc = [zero,one,two,three,four,five,six]

import random


#For Toss:
def toss():
        #Taking enteries from the user for the toss:
        toss_hc = input("For the toss, ask the user to choose between even or odd: ")
        if (toss_hc not in ["even","odd"]):
            print("Inavalid entry, Again select even or odd.")
            toss()
        user_toss = int(input("Enter the number from 0 to 6 for the toss: "))
        if (user_toss<0) or (user_toss>6):
            print("Invalid entry. Please enter the number between 0 to 6")
            toss()
        else:
            print(images_hc[user_toss])
    
        #Robot entries:
        robot_toss = random.randint(0,6)
        print(f"The Robot chooses {robot_toss}")
        print(images_hc[robot_toss])
    
        #Addition of user_toss digit and robot_toss digit:
        sum_toss = user_toss + robot_toss   
    
        #To determine who won the toss:
        if toss_hc.lower() == "even":
            if(sum_toss % 2 == 0):
                print("You win the toss..!!")
                user_bat_bowl = input("What do you want to choose, bat or ball?: ")
                if user_bat_bowl.lower() == "bat":
                    print("You will be batting in the first inning, and the robot will be bowling.")
                    user_first_batting()
                elif user_bat_bowl.lower() == "ball":
                    print("Robot will be batting in the first inning, and you will be bowling.")
                    user_second_batting()
                else:
                    print("Invalid entry..!!")
                    toss() 
                    
            else:
                print("Robot wins the toss..!!")
                robot_bat_bowl = random.choice(["bat","ball"])
                if robot_bat_bowl == "bat":
                    print("Robot will be batting in the first inning, and you will be bowling.")
                    user_second_batting()
                elif robot_bat_bowl == "ball":
                    print("Robot will be bowling in the first inning, and you will be batting.")
                    user_first_batting()
        
        
        
        elif toss_hc.lower() == "odd":
            if(sum_toss % 2 != 0):
                print("You win the toss..!!")
                user_bat_bowl = input("What do you want to choose, bat or ball?")
                if user_bat_bowl.lower() == "bat":
                    print("You will be batting in the first inning, and the robot will be bowling.")
                    user_first_batting()
                elif user_bat_bowl.lower() == "ball":
                    print("Robot will be batting in the first inning, and you will be bowling.")
                    user_second_batting()
                else:
                    print("Invalid entry..!!")
                    toss() 
                    
            else:
                print("Robot wins the toss..!!")
                robot_bat_bowl = random.choice(["bat","ball"])
                if robot_bat_bowl == "bat":
                    print("Robot will be batting in the first inning, and you will be bowling.")
                    user_second_batting()
                elif robot_bat_bowl == "ball":
                    print("Robot will be bowling in the first inning, and you will be batting.")
                    user_first_batting()

#For user batting in first inning:
def user_first_batting():
        print("""
 _   _                          ____            _     _     _                 
| | | |  ___    ___   _ __     | __ )    __ _  | |_  | |_  (_)  _ __     __ _ 
| | | | / __|  / _ \ |  __|    |  _ \   / _  | | __| | __| | | |  _ \   / _  |
| |_| | \__ \ |  __/ | |       | |_) | | (_| | | |_  | |_  | | | | | | | (_| |
 \___/  |___/  \___| |_|       |____/   \__,_|  \__|  \__| |_| |_| |_|  \__  |
                                                                        |___/ """)
        
    
        #Initializing the user's runs to zero:
        runs_user = 0
        
        #Applying condition:
        while (True):
            robot_move = random.randint(0,6)
            user_move = int(input("Enter the runs from 0 to 6: "))
            if (user_move<0) or (user_move>6):
                print("Invalid entry. Please enter the number between 0 to 6")
                toss()
               
            print(images_hc[user_move])
            print(f"The Robot balls {robot_move}")
            print(images_hc[robot_move])
            
            
        
            if (user_move == robot_move):
                print("""
  ___    _   _   _____ 
 / _ \  | | | | |_   _|
| | | | | | | |   | |  
| |_| | | |_| |   | |  
 \___/   \___/    |_|  
                     """)
                
                break
            else:
                runs_user = runs_user + user_move
                print(f"User made {runs_user} runs")
                print("~~~~~~~~~~~~First inning comes to an end~~~~~~~~~~~~")

        
        print(f"Robot requires {runs_user+1} runs to win..!!")
        
        print("""
 ____            _               _             ____            _     _     _                 
|  _ \    ___   | |__     ___   | |_          | __ )    __ _  | |_  | |_  (_)  _ __     __ _ 
| |_) |  / _ \  |  _ \   / _ \  | __|         |  _ \   / _  | | __| | __| | | |  _ \   / _  |
|  _ <  | (_) | | |_) | | (_) | | |_          | |_) | | (_| | | |_  | |_  | | | | | | | (_| |
|_| \_\  \___/  |_ __/   \___/   \__|         |____/   \__ _|  \__|  \__| |_| |_| |_|  \__, |
                                                                                       |___/""")
        
        #Initializing the robot's runs to zero:
        runs_robot = 0
        
        #Appluing loop condition:
        while (True):
            robot_move = random.randint(0,6)
            user_move = int(input("Enter the balls from 0 to 6: "))
            if (user_move > 6) and (user_move < 0):
                print("Invalid move..!!")
                toss()
                
            print(images_hc[user_move])
            print(f"The Robot hits {robot_move}")
            print(images_hc[robot_move])

            runs_robot = runs_robot + robot_move
            
            if runs_robot > runs_user:
                print(f"Robot made {runs_robot} runs")
                print("""
 ____            _               _                  _                   _     _                                                 
|  _ \    ___   | |__     ___   | |_    __      __ (_)  _ __    ___    | |_  | |__     ___      __ _    __ _   _ __ ___     ___ 
| |_) |  / _ \  |  _ \   / _ \  | __|   \ \ /\ / / | | |  _ \  / __|   | __| |  _ \   / _ \    / _  |  / _  | |  _   _ \   / _ \
|  _ <  | (_) | | |_) | | (_) | | |_     \ V  V /  | | | | | | \__ \   | |_  | | | | |  __/   | (_| | | (_| | | | | | | | |  __/
|_| \_\  \___/  |_ __/   \___/   \__|     \_/\_/   |_| |_| |_| |___/    \__| |_| |_|  \___|    \__, |  \__,_| |_| |_| |_|  \___|
                                                                                               |___/                            """)
                
                print("""
 ____           _     _                     _                  _                              _       _     _                    
| __ )    ___  | |_  | |_    ___   _ __    | |  _   _    ___  | | __    _ __     ___  __  __ | |_    | |_  (_)  _ __ ___     ___ 
|  _ \   / _ \ | __| | __|  / _ \ |  __|   | | | | | |  / __| | |/ /   |  _ \   / _ \ \ \/ / | __|   | __| | | |  _   _ \   / _ \
| |_) | |  __/ | |_  | |_  |  __/ | |      | | | |_| | | (__  |   <    | | | | |  __/  >  <  | |_    | |_  | | | | | | | | |  __/
|____/   \___|  \__|  \__|  \___| |_|      |_|  \__,_|  \___| |_|\_\   |_| |_|  \___| /_/\_\  \__|    \__| |_| |_| |_| |_|  \___|""")
                
                
                play_again()
                break


            
                
            if (user_move == robot_move):
                print(f"Robot made {runs_robot} runs")
                print("""
  ___    _   _   _____ 
 / _ \  | | | | |_   _|
| | | | | | | |   | |  
| |_| | | |_| |   | |  
 \___/   \___/    |_|  
                      """)


                if (runs_robot < runs_user):
                    print ("""
__   __                               _             _     _                                                 
\ \ / /   ___    _   _    __      __ (_)  _ __     | |_  | |__     ___      __ _    __ _   _ __ ___     ___ 
 \ V /   / _ \  | | | |   \ \ /\ / / | | |  _ \    | __| |  _ \   / _ \    / _  |  / _  | |  _   _ \   / _ \
  | |   | (_) | | |_| |    \ V  V /  | | | | | |   | |_  | | | | |  __/   | (_| | | (_| | | | | | | | |  __/
  |_|    \___/   \__,_|     \_/\_/   |_| |_| |_|    \__| |_| |_|  \___|    \__, |  \__,_| |_| |_| |_|  \___|
                                                                           |___/                            """)
                    
                    print(f"Congratulations..!! You won the game by {runs_user-runs_robot} runs")
                    
                else:
                    print("""
 _____   _                                    _            _         _                         _                           
|_   _| | |__     ___     _ __ ___     __ _  | |_    ___  | |__     (_)  ___      __ _      __| |  _ __    __ _  __      __
  | |   |  _ \   / _ \   |  _   _ \   / _  | | __|  / __| |  _ \    | | / __|    / _  |    / _  | |  __|  / _  | \ \ /\ / /
  | |   | | | | |  __/   | | | | | | | (_| | | |_  | (__  | | | |   | | \__ \   | (_| |   | (_| | | |    | (_| |  \ V  V / 
  |_|   |_| |_|  \___|   |_| |_| |_|  \__,_|  \__|  \___| |_| |_|   |_| |___/    \__,_|    \__,_| |_|     \__,_|   \_/\_/  
                                                                                                                           """)
                play_again()
                break
                    
#For user batting in second inning:
def user_second_batting():
        print("""
 ____            _               _          ____            _     _     _                 
|  _ \    ___   | |__     ___   | |_       | __ )    __ _  | |_  | |_  (_)  _ __     __ _ 
| |_) |  / _ \  |  _ \   / _ \  | __|      |  _ \   / _  | | __| | __| | | |  _ \   / _  |
|  _ <  | (_) | | |_) | | (_) | | |_       | |_) | | (_| | | |_  | |_  | | | | | | | (_| |
|_| \_\  \___/  |_ __/   \___/   \__|      |____/   \__ _|  \__|  \__| |_| |_| |_|  \__, |
                                                                                    |___/ """)
    

        #Initializing the robot's runs to zero:
        runs_robot = 0

        #Applying condition:
        while (True):
            robot_move = random.randint(0,6)
            user_move = int(input("Enter the balls from 0 to 6: "))
            if (user_move<0) or (user_move>6):
                print("Invalid entry. Please enter the number between 0 to 6")
                toss()
            

            print(images_hc[user_move])
            print(f"The Robot chooses {robot_move}")
            print(images_hc[robot_move])
                    
            if (robot_move == user_move):
                print("""
  ___    _   _   _____ 
 / _ \  | | | | |_   _|
| | | | | | | |   | |  
| |_| | | |_| |   | |  
 \___/   \___/    |_|  
                     """)
            
                break
            else:
                runs_robot = runs_robot + robot_move
                print(f"Robot made {runs_robot} runs")
                print("~~~~~~~~~~~~First inning comes to an end~~~~~~~~~~~~")

                



        print(f"User requires {runs_robot+1} runs to win..!!")
        
        print("""
 _   _                            ____            _     _     _                 
| | | |  ___    ___   _ __       | __ )    __ _  | |_  | |_  (_)  _ __     __ _ 
| | | | / __|  / _ \ |  __|      |  _ \   / _  | | __| | __| | | |  _ \   / _  |
| |_| | \__ \ |  __/ | |         | |_) | | (_| | | |_  | |_  | | | | | | | (_| |
 \___/  |___/  \___| |_|         |____/   \__,_|  \__|  \__| |_| |_| |_|  \__, |
                                                                          |___/ """)
        
        #Initializing the user's runs to zero:
        runs_user = 0
        
        #Appluing loop condition:
        while (True):
            robot_move = random.randint(0,6)
            user_move = int(input("Enter the runs from 0 to 6: "))
            if (user_move > 6) and (user_move < 0):
                print("Invalid move..!!")
                toss()
                
            print(images_hc[user_move])
            print(f"The Robot balls {robot_move}")
            print(images_hc[robot_move])
            
            runs_user = runs_user + user_move
            
            if (runs_user > runs_robot):
                print(f"User made {runs_user} runs")
                print("""
__   __                               _             _     _                                                 
\ \ / /   ___    _   _    __      __ (_)  _ __     | |_  | |__     ___      __ _    __ _   _ __ ___     ___ 
 \ V /   / _ \  | | | |   \ \ /\ / / | | |  _ \    | __| |  _ \   / _ \    / _  |  / _  | |  _ ` _ \   / _ \
  | |   | (_) | | |_| |    \ V  V /  | | | | | |   | |_  | | | | |  __/   | (_| | | (_| | | | | | | | |  __/
  |_|    \___/   \__,_|     \_/\_/   |_| |_| |_|    \__| |_| |_|  \___|    \__, |  \__,_| |_| |_| |_|  \___|
                                                                           |___/                            """)
                
                play_again()
                break
                
            if (user_move == robot_move):
                print(f"User made {runs_user} runs")
                print("""
  ___    _   _   _____ 
 / _ \  | | | | |_   _|
| | | | | | | |   | |  
| |_| | | |_| |   | |  
 \___/   \___/    |_|  
                      """)
                
                    
                if (runs_user < runs_robot):
                    print(f"You lose the game by {runs_robot-runs_user} runs")

                    print ("""
__   __                    _                          _     _                                                 
\ \ / /   ___    _   _    | |   ___    ___    ___    | |_  | |__     ___      __ _    __ _   _ __ ___     ___ 
 \ V /   / _ \  | | | |   | |  / _ \  / __|  / _ \   | __| |  _ \   / _ \    / _  |  / _  | |  _ ` _ \   / _ \
  | |   | (_) | | |_| |   | | | (_) | \__ \ |  __/   | |_  | | | | |  __/   | (_| | | (_| | | | | | | | |  __/
  |_|    \___/   \__,_|   |_|  \___/  |___/  \___|    \__| |_| |_|  \___|    \__, |  \__,_| |_| |_| |_|  \___|
                                                                             |___/                            """)
                    print("""
 ____           _     _                     _                  _                              _       _     _                    
| __ )    ___  | |_  | |_    ___   _ __    | |  _   _    ___  | | __    _ __     ___  __  __ | |_    | |_  (_)  _ __ ___     ___ 
|  _ \   / _ \ | __| | __|  / _ \ |  __|   | | | | | |  / __| | |/ /   |  _ \   / _ \ \ \/ / | __|   | __| | | |  _ ` _ \   / _ \
| |_) | |  __/ | |_  | |_  |  __/ | |      | | | |_| | | (__  |   <    | | | | |  __/  >  <  | |_    | |_  | | | | | | | | |  __/
|____/   \___|  \__|  \__|  \___| |_|      |_|  \__,_|  \___| |_|\_\   |_| |_|  \___| /_/\_\  \__|    \__| |_| |_| |_| |_|  \___|""")
                    
                    
                    
                else:
                    print("""
 _____   _                                    _            _         _                         _                           
|_   _| | |__     ___     _ __ ___     __ _  | |_    ___  | |__     (_)  ___      __ _      __| |  _ __    __ _  __      __
  | |   |  _ \   / _ \   |  _   _ \   / _  | | __|  / __| |  _ \    | | / __|    / _  |    / _  | |  __|  / _  | \ \ /\ / /
  | |   | | | | |  __/   | | | | | | | (_| | | |_  | (__  | | | |   | | \__ \   | (_| |   | (_| | | |    | (_| |  \ V  V / 
  |_|   |_| |_|  \___|   |_| |_| |_|  \__,_|  \__|  \___| |_| |_|   |_| |___/    \__,_|    \__,_| |_|     \__,_|   \_/\_/  
                                                                                                                           """)
                
                play_again()
                break
    

#To play again:
def play_again():
    playagain = input("Do you want to play again? Type yes if you want to play again, otherwise type no if you don't want to play again: ")
    
    if playagain.lower() == "yes":
        hand_cricket()
    elif playagain.lower() == "no":
        print("Thank you for playing the game.")
        exit()
    else:
        print("Invalid entry..!!")
        play_again()

def hand_cricket():
    print("""
 _   _                       _           ____          _          _             _   
| | | |   __ _   _ __     __| |         / ___|  _ __  (_)   ___  | | __   ___  | |_ 
| |_| |  / _  | |  _ \   / _  |        | |     |  __| | |  / __| | |/ /  / _ \ | __|
|  _  | | (_| | | | | | | (_| |        | |___  | |    | | | (__  |   <  |  __/ | |_ 
|_| |_|  \__,_| |_| |_|  \__,_|         \____| |_|    |_|  \___| |_|\_\  \___|  \__|

------------------------------- Play Virtual Cricket -------------------------------""")
    
    toss()
   

hand_cricket()
