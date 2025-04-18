import pygame
import time
import sys
import os

questions = ["1. Which organ of the human body is primarily responsible for pumping blood?",
             "2. In which direction does the sun rise?",
             "3. Which of these is not a web browser?",
             "4. If someone says they are eating 'idli', which part of India are they most likely from?",
             "5. Which of the following is used to measure temperature?",
             "6. What does the 'C' in CPU stand for?",
             "7. Who among these was not a President of India?",
             "8. Which Indian city is also known as the 'Pink City'?",
             "9. If a car is moving at 60 km/h, how far will it travel in 30 minutes?",
             "10. Which gas is most commonly used in fire extinguishers?",
             "11. Which of these is a famous Indian classical dance form from Kerala?",
             "12. The 'S' in ISRO stands for what?",
             "13. Which of these is a unit used to measure electric current?",
             "14. Which river is known as the longest river in India?",]
answers = [["brain","liver","heart","lungs"],
           ["east","west","north","south"],
           ["chrome","firefox","instagram","safari"],
           ["punjab","rajasthan","tamilnadu","gujarat"],
           ["barometer","thermometer","speedometer","altimeter"],
           ["central","control","compute","core"],
           ["dr.APJ Abdul Kalam","Pratibha Patil","atal bihari vajpayee","ram nath kovind"],
           ["jodhpur","jaipur","udaipur","bikaner"],
           ["15","20","25","30"],
           ["oxygen","carbondioxide","nitrogen","hydrogen"],
           ["kathak","odissi","bharatnatyam","kathakali"],
           ["science","space","satallite","service"],
           ["volt","ohm","ampere","watt"],
           ["yamuna","brahmaputra","ganga","godavari"],]
paise = ["1000",      
         "2000",
         "5000",
         "10000",
         "20000",
         "50000",
         "100000",
         "320000",
         "640000",
         "1250000",
         "2500000",
         "5000000",
         "10000000",
         "70000000"]

pygame.mixer.init()

startsound = pygame.mixer.Sound("music/among-us-role-reveal-sound.mp3")
confirmsound = pygame.mixer.Sound("music/trollface-smile.mp3")
gamestart = pygame.mixer.Sound("music/kbc-question.mp3")
angryamitabh = pygame.mixer.Sound("music/angry-amitabh.mp3")
intense = pygame.mixer.Sound("music/quiz-show-thinking_by_waderman_preview.mp3")
moreintense =  pygame.mixer.Sound("music/serious music_preview.mp3")
sadmeow =  pygame.mixer.Sound("music/sad-meow-song.mp3")
money = pygame.mixer.Sound("music/money-soundfx.mp3")
bgmusic = pygame.mixer.Sound("music/tension-showmatch.mp3")
tensionrise =  pygame.mixer.Sound("music/8-tension-rising.mp3")
tension =  pygame.mixer.Sound("music/64-000-500-000-questions-mp3cut.mp3")
bhikhari = pygame.mixer.Sound("music/bhikhari.wav")
croreseven =  pygame.mixer.Sound("music/sevenscore.wav")
fullintro =  pygame.mixer.Sound("music/KBC INTRO WITH MUSIC.wav")
dance =  pygame.mixer.Sound("music/5x30.mp3")
idlidosa = pygame.mixer.Sound("music/idlidosa.wav")
technologia = pygame.mixer.Sound("music/technologia.mp3")

def typing(text,delay):
    for i in text:
        time.sleep(delay)
        sys.stdout.write(i)
        sys.stdout.flush()
print("\n\nWelcome to Kaun Banega Crorepati!")
time.sleep(2)
startsound.play()
while True:
    print("\n\n")
    typing("\nDo you really want to play KBC? : ",0.05)
    play = input("")
    if play != "yes":
        print("\nEnter a Valid Answer (yes/no) : ")
    else:
        confirmsound.play()
        typing("\nAre you sure that you're smart enough to play KBC? : ",0.03)
        play2 = input("")
        if play2 == "no":
             print("\nAagya na line pe! Bhag yaha se...")
        elif play2 != "yes":
            print("\nEnter a Valid Answer (yes/no)")
        else:
            fullintro.play()
            typing("\n\nFine then! LET'S PLAY KAUN BANEGA CROREPATI",0.05)
            break   
def play():
    amount = 0
    typing("\nToh yeh raha pehela prashn 1000 Rupyo ke liye aapki screen par!",0.05)
    fullintro.stop()
    gamestart.play()
    print("\n")
    typing(questions[0],0.05)
    print("\n")
    tension.play()
    for i in answers[0]:
        print(i)
    answer1 = input("\nType the answer : ")
    if answer1 == "heart":
        amount = int(paise[0])
        tension.stop()
        money.play()
        typing("\nArey Kya baat hai sir!",0.05)
        print(f"\nApp ke account me total {amount} rupey aa chuke hai!")
        typing("\nToh ab aate hai hum humare agle prasn ki aurr...Joki hai 2000 Rupyo ke liye",0.02)
        gamestart.play()
        print("\n")
        typing(questions[1],0.02)
        print("\n")
        tension.play()
        for i in answers[1]:
            print(i)
        print("\n")
        answer2 = input("\nType the answer : ")
        if answer2 == "east":
            amount = int(paise[1])
            tension.stop()
            money.play()
            time.sleep(1)
            typing("\nPrashn number 3... Yeh raha..",0.05)
            gamestart.play()
            print("\n")
            typing(questions[2],0.02)
            print("\n")
            tension.play()
            for i in answers[2]:
                print(i)
            answer3 = input("\nType the answer : ")
            if answer3 == "instagram":
                amount = int(paise[2])
                tension.stop()
                money.play()
                time.sleep(1)
                typing("\nPrashn number 4... Yeh raha..",0.05)
                idlidosa.play()
                print("\n")
                typing(questions[3],0.02)
                print("\n")
                for i in answers[3]:
                    print(i)
                answer4 = input("\nType the answer : ")
                if answer4 == "tamilnadu":
                    amount = int(paise[3])
                    idlidosa.stop()
                    money.play()
                    time.sleep(1)
                    typing("\nPrashn number 5... Yeh raha..",0.05)
                    gamestart.play()
                    print("\n")
                    typing(questions[4],0.02)
                    print("\n")
                    tension.play()
                    for i in answers[4]:
                        print(i)
                    answer5 = input("\nType the answer : ")
                    if answer5 == "thermometer":
                        amount = int(paise[4])
                        tension.stop()
                        money.play()
                        time.sleep(1)
                        typing("\nPrashn number 6... Yeh raha..",0.05)
                        gamestart.play()
                        print("\n")
                        typing(questions[5],0.02)
                        print("\n")
                        tension.play()
                        for i in answers[5]:
                            print(i)
                        answer6 = input("\nType the answer : ")
                        if answer6 == "central":
                            amount = int(paise[5])
                            tension.stop()
                            money.play()
                            time.sleep(1)
                            typing("\nPrashn number 7... Yeh raha..",0.05)
                            gamestart.play()
                            print("\n")
                            typing(questions[6],0.02)
                            print("\n")
                            tension.play()
                            for i in answers[6]:
                                print(i)
                            answer7 = input("\nType the answer : ")
                            if answer7 == "atal bihari vajpayee":
                                amount = int(paise[6])
                                tension.stop()
                                money.play()
                                time.sleep(1)
                                typing("\nPrashn number 8... Yeh raha..",0.05)
                                gamestart.play()
                                print("\n")
                                typing(questions[7],0.02)
                                print("\n")
                                tension.play()
                                for i in answers[7]:
                                    print(i)
                                answer8 = input("\nType the answer : ")
                                if answer8 == "jaipur":
                                    amount = int(paise[7])
                                    tension.stop()
                                    money.play()
                                    time.sleep(1)
                                    typing("\nPrashn number 9... Yeh raha..",0.05)
                                    gamestart.play()
                                    print("\n")
                                    typing(questions[8],0.02)
                                    print("\n")
                                    tension.play()
                                    for i in answers[8]:
                                        print(i)
                                    answer9 = input("\nType the answer : ")
                                    if answer9 == "30":
                                        amount = int(paise[8])
                                        tension.stop()
                                        money.play()
                                        time.sleep(1)
                                        typing("\nPrashn number 10... Yeh raha..",0.05)
                                        gamestart.play()
                                        print("\n")
                                        typing(questions[9],0.02)
                                        print("\n")
                                        tension.play()
                                        for i in answers[9]:
                                            print(i)
                                        answer10 = input("\nType the answer : ")
                                        if answer10 == "carbondioxide":
                                            amount = int(paise[9])
                                            tension.stop()
                                            money.play()
                                            time.sleep(1)
                                            typing("\nPrashn number 11... Yeh raha..",0.05)
                                            gamestart.play()
                                            print("\n")
                                            typing(questions[10],0.02)
                                            print("\n")
                                            tension.play()
                                            for i in answers[10]:
                                                print(i)
                                            answer11 = input("\nType the answer : ")
                                            if answer11 == "kathakali":
                                                amount = int(paise[10])
                                                tension.stop()
                                                money.play()
                                                time.sleep(1)
                                                typing("\nPrashn number 12... Yeh raha..",0.05)
                                                gamestart.play()
                                                print("\n")
                                                typing(questions[11],0.02)
                                                print("\n")
                                                technologia.play()
                                                for i in answers[11]:
                                                    print(i)
                                                answer12 = input("\nType the answer : ")
                                                if answer12 == "space":
                                                    amount = int(paise[11])
                                                    technologia.stop()
                                                    money.play()
                                                    time.sleep(1)
                                                    typing("\nPrashn number 13... Yeh raha..",0.05)
                                                    gamestart.play()
                                                    print("\n")
                                                    typing(questions[12],0.02)
                                                    print("\n")
                                                    tension.play()
                                                    for i in answers[12]:
                                                        print(i)
                                                    answer13 = input("\nType the answer : ")
                                                    if answer13 == "ampere":
                                                        amount = int(paise[12])
                                                        tension.stop()
                                                        money.play()
                                                        time.sleep(1)
                                                        typing("\nPrashn number 14... Yeh raha..",0.05)
                                                        gamestart.play()
                                                        print("\n")
                                                        typing(questions[13],0.02)
                                                        print("\n")
                                                        tension.play()
                                                        for i in answers[13]:
                                                            print(i)
                                                        answer14 = input("\nType the answer : ")
                                                        if answer14 == "ganga":
                                                            amount = int(paise[13])
                                                            tension.stop()
                                                            croreseven.play()
                                                            time.sleep(2)
                                                            dance.play()
                                                            frame1 = """
                                                                        o
                                                                        /|\\
                                                                        / \\
                                                                        """

                                                            frame2 = """
                                                                        o
                                                                        \\|/
                                                                        / \\
                                                                        """

                                                            def clear():
                                                                os.system('cls' if os.name == 'nt' else 'clear')

                                                            def dance_dot_person(repeats=10, delay=0.3):
                                                                for _ in range(repeats):
                                                                    clear()
                                                                    print(frame1)
                                                                    time.sleep(delay)

                                                                    clear()
                                                                    print(frame2)
                                                                    time.sleep(delay)

                                                            dance_dot_person()
                                                            print("Thanks For Playing!")
                                                            quit()
                                                        else:
                                                            tension.stop()
                                                            angryamitabh.play()
                                                            print(f"Toh aap lekha jaate hai '10000000' Rupye ")
                                                            typing("Gawar Itna bhi nahi aata!??!",0.03)
                                                            time.sleep(5)
                                                            quit()
                                                    else:
                                                        tension.stop()
                                                        angryamitabh.play()
                                                        print(f"Toh aap lekha jaate hai '5000000' Rupye ")
                                                        typing("Gawar Itna bhi nahi aata!??!",0.03)
                                                        time.sleep(5)
                                                        quit()
                                                else:
                                                    tension.stop()
                                                    angryamitabh.play()
                                                    print(f"Toh aap lekha jaate hai '320000' Rupye ")
                                                    typing("Gawar Itna bhi nahi aata!??!",0.03)
                                                    time.sleep(5)
                                                    quit()
                                            else:
                                                tension.stop()
                                                angryamitabh.play()
                                                print(f"Toh aap lekha jaate hai '320000' Rupye ")
                                                typing("Gawar Itna bhi nahi aata!??!",0.03)
                                                time.sleep(5)
                                                quit()
                                        else:
                                            tension.stop()
                                            angryamitabh.play()
                                            print(f"Toh aap lekha jaate hai '320000' Rupye ")
                                            typing("Gawar Itna bhi nahi aata!??!",0.03)
                                            time.sleep(5)
                                            quit()
                                    else:
                                        tension.stop()
                                        angryamitabh.play()
                                        print(f"Toh aap lekha jaate hai '320000' Rupye ")
                                        typing("Gawar Itna bhi nahi aata!??!",0.03)
                                        time.sleep(5)
                                        quit()                                                                                                 
                                else:
                                    tension.stop()
                                    angryamitabh.play()
                                    print(f"Toh aap lekha jaate hai '10000' Rupye ")
                                    typing("Gawar Itna bhi nahi aata!??!",0.03)
                                    time.sleep(5)
                                    quit()                        
                            else:
                                tension.stop()
                                angryamitabh.play()
                                print(f"Toh aap lekha jaate hai '10000' Rupye ")
                                typing("Gawar Itna bhi nahi aata!??!",0.03)
                                time.sleep(5)
                                quit()                                 
                        else:
                            tension.stop()
                            angryamitabh.play()
                            print(f"Toh aap lekha jaate hai '10000' Rupye ")
                            typing("Gawar Itna bhi nahi aata!??!",0.03)
                            time.sleep(5)
                            quit()                                  
                    else:
                        tension.stop()
                        angryamitabh.play()
                        print(f"Toh aap lekha jaate hai '10000' Rupye ")
                        typing("Gawar Itna bhi nahi aata!??!",0.03)
                        time.sleep(5)
                        quit()
                else:
                    tension.stop()
                    bhikhari.play()
                    print(f"Toh aap lekha jaate hai '0' Rupye ")
                    typing("Gawar Itna bhi nahi aata!??!",0.03)
                    time.sleep(20)
                    quit()
            else:
                tension.stop()
                bhikhari.play()
                print(f"Toh aap lekha jaate hai '0' Rupye ")
                typing("Gawar Itna bhi nahi aata!??!",0.03)
                time.sleep(20)
                quit()

        else:
            tension.stop()
            bhikhari.play()
            print(f"Toh aap lekha jaate hai '0' Rupye ")
            typing("Gawar Itna bhi nahi aata!??!",0.03)
            time.sleep(20)
            quit()
            
    else:
        tension.stop()
        bhikhari.play()
        print(f"Toh aap lekha jaate hai '0' Rupye ")
        typing("Gawar Itna bhi nahi aata!??!",0.03)
        time.sleep(20)
        quit()
def game():
    while True:
        typing("\nType 'start' to START the Game or 'quit' to exit : ",0.02)
        choice = input("")
        if choice == "start":
            play()
        elif choice == 'quit':
            quit()
        else:
            print("Please enter a valid answer.")        
game()
    
 