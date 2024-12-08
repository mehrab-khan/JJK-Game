import random
import time

hero = 'Gojo'
villain = 'Sukuna'
hero_live = 100
villain_live = 100
villain_domain_attempt =  False
def hero_Attack():
    global villain_live
    global hero_live
    hollow_purple = 40
    red = 10
    blue = 7
    kick_and_punch = 5
    if hero_live < 40:
        user_power_choice = int(input('1.Reversal Red\n2.Blue\n3.Kick & Punch\n4.Hollow Purple\n5.Heal ( 15 )\nEnter : '))
    else:
        user_power_choice = int(input('1.Reversal Red\n2.Blue\n3.Kick & Punch\nEnter : '))
    print('------- Gojo Attacking -------')
    time.sleep(1)
    if user_power_choice == 1:
         villain_live = villain_live - red
         print('Sukuna Live Is ',villain_live)


    elif user_power_choice == 2:
        villain_live = villain_live - blue
        print('Sukuna Live Is ', villain_live)
    elif user_power_choice == 3:
        villain_live = villain_live - kick_and_punch
        print('Sukuna Live Is ', villain_live)
    elif user_power_choice == 4:
        if hero_live < 40:
            villain_live = villain_live - hollow_purple
        else:
            print("Try Another Choice")
    elif user_power_choice == 5:
        if hero_live < 40:
            hero_live = hero_live + 20
        else:
            print("Try Another Choice")
    else:
        print("Please enter any actions....")



def villain_Attack():
    global hero_live
    global villain_live
    global villain_domain_attempt
    if villain_live < 50 and villain_domain_attempt == False:
        print('------- Sukuna Starting His Domain --------')
        villain_domain_attempt = True
        time.sleep(1)
        print('Reyoki Tenkai')
        for i in range(6):
            time.sleep(0.5)
            print('Gojo health decreasing -5')
            hero_live = hero_live - 5

        print("Gojo Live : ",hero_live)

    else:
        print('---------Sukuna Attacking & Healing ( 2+ )---------')
        villain_live = villain_live + 2
        attacks = [10,20,5,15]
        attack_power = random.choice(attacks)
        hero_live = hero_live - attack_power

        print("Gojo Live : ",hero_live)



user_init_choice = int(input("Choose Options : \n1.Play\n2.Exit\nEnter : "))
time.sleep(1)
print('------Starting------')
while True:
    if hero_live > 0 and villain_live > 0:
        if user_init_choice == 1:
            time.sleep(1)

            print(f'\nHero (Gojo) live is {hero_live}\nVillain (Sukuna) live is {villain_live}')
            hero_Attack()
            time.sleep(1)
            villain_Attack()
    else:
        if villain_live <= 0 :
            print("GAME OVER Gojo Win")
            break
        elif hero_live <= 0:
            print("GAME OVER Sukuna Win")
            break

