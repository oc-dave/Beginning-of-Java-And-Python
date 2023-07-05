from subprocess import call

print("""
============================================================================================    
                                      NOKIA
============================================================================================

                                     IPHONE XS MAX """)


def phone_book():
    return """
    =====================================
                 Phone Book
    =====================================
            1. Search
            2. Service Nos. 1
            3. Add name
            4. Erase
            5. Edit
            6. Assign tone
            7. Send b’card  
            8. Options 
            9. Speed dials
            10. Voice tags
            """


def options():
    return """
    ================================
                options
    ================================
            1. Type of view
            2. Memory status
    """


def Messages():
    return """
        ======================================
                        Messages
        ======================================
            1. Write messages
            2. Inbox
            3. Outbox
            4. Picture messages
            5. Templates
            6. Smileys
            7. Message settings
             8. Info service
            9. Voice mailbox number
            10.Service command editor
            """


def Message_settings():
    return """"
    ===============================
            Message Settings
    ===============================
            1. Set 12
            2. Common 13
            """


def set():
    return """
    =================================
                Set
    =================================
            1. Message centre number
            2. Messages sent as       
            3. Message validity
            """


def Common():
    return """
    =============================
            Common
    =============================
    1. Delivery reports
    2. Reply via same centre
    3 . Character support
    """


def chat():
    return """chat"""


def Call_register():
    return """
    ================================
            Call register
    ================================
            1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs 
            7. Call cost settings
            8. Prepaid credit"""


def Show_call_duration():
    return """
    =================================
            Show call duration
    =================================
            1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers"""


def Show_call_costs():
    return """
    ===============================
            Show call cost
    ===============================
            1. Last call cost
            2. All calls’ cost
            3. Clear counters 
            """


def Call_cost_settings():
    return """
    ===========================================
            Call  cost setting
    ===========================================
                1. Call cost limit
                2. Show costs in
                """


def Tones():
    return """
    ==================================
                Tones       
    ==================================
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                """


def Settings():
    return """
    ============================
            Settings
    ============================
            1. Call settings
            2. Phone settings
            3. Security settings
            4. Restore factory settings
            """


def Call_settings():
    return """
    =====================================
                 Call Setting
    ======================================
                1. Automatic redial
                2. Speed dialling
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Automatic answer 1
                """


def Phone_settings():
    return """    1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                 5. Lights2
                6. Confirm SIM service actions
                """


def Security_settings():
    return """
    =====================================
             Security setting
    =====================================

                1. PIN code request
                2. Call barring service
                3. Fixed dialling
                4. Closed user group
                5. Phone security
                6. Change access codes"""


def Call_divert():
    return """
    ==================================
            Call divert
    =================================
             call divert 
             """


def Games():
    return """
    =================================
                Game
    =================================
                1. Snake Game
                2. puzzle
                3. Sudo
                 """


def Calculator():
    return """
    ========================
            Calculator
    ========================
        Calculator"""


def Reminders():
    return """
    =========================
            Reminder
    =========================
            Reminder
            """


def Clock():
    return """
    =================================
                 Clock
    =================================
                1. Alarm clock  
                2. Clock settings 
                3. Date setting
                4. Stopwatch 
                5. Countdown timer   
                6. Auto update of date and time
                """


def Profiles():
    return """
    ============================
            Profiles
    ============================
            Profiles"""


def SIM_services():
    return """
    ========================
        Sim services
    ========================
    Sim services"""


def menu(user):
    print(f"""  
                ===================================================                
                                      MENU
                ===================================================                
                            (1) Phone book 
                            (2) Messages     
                            (3) Chat         
                            (4) call register
                            (5) Tones       
                            (6) Settings    
                            (7) Call_divert   
                            (8)Games 
                            (9) Calculator 
                            (10) Reminder    
                            (11) Clock        
                            (12) Profile
                            (13) SIM services """)


counter = 0

while True:
    user = int(input("enter 1 for main menu : "))
    if user == 1:
        print(menu(user))

    user_entry = int(input("enter menu number : "))
    if user_entry == 1:
        print(phone_book())
        user_entry = int(input("Enter 8 for option or 0 to go back:"))
    if user_entry == 0:
        print(phone_book())
    elif user_entry == 8:
        print(options())
        user_entry = int(input("Enter 0 to go back:"))
    if user_entry == 0:
        print(menu(user))


    elif user_entry == 2:
        print(Messages())
        user_entry = int(input("Enter 7 for message setting or 0 to go back: "))
        if user_entry == 0:
            print(menu(user))
        elif user_entry == 7:
            print(Message_settings())
        user_entry = int(input("Enter 1 for set or 2 for common,enter 0 to go back: "))
        if user_entry == 0:
            print(Message_settings())
        elif user_entry == 1:
            print(set())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Message_settings())
                user_entry = int(input("Enter 0 go back: "))
                if user_entry == 0:
                    print(Messages())
        elif user_entry == 2:
            print(Common())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Message_settings())
                user_entry = int(input("Enter 0 go back: "))
                if user_entry == 0:
                    print(Messages())


    elif user_entry == 3:
        print(chat())
        user_entry = int(input("Enter 0 to go back: "))
        if user_entry == 0:
            print(menu(user))



    elif user_entry == 4:
        print(Call_register())
        user_entry = int(input('Enter number 5 for Show_call_duration or 7 or Call_cost_settings or 0 to go back:'))
        if user_entry == 0:
            print(menu(user))
        elif user_entry == 5:
            print(Show_call_duration())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Call_register())
        elif user_entry == 6:
            print(Show_call_costs())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Call_register())
        elif user_entry == 7:
            print(Call_cost_settings())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Call_register())

    elif user_entry == 5:
        print(Tones())
        user = int(input("enter 0 to go back: "))
        if user_entry == 0:
            print(menu(user))


    elif user_entry == 6:
        print(Settings())
        user_entry = int(input("Enter 0 to go back: "))
        if user_entry == 1:
            print(Call_settings())
            user_entry = int(input("Enter 0 to go back: "))
            print(Settings())
        elif user_entry == 0:
            print(Settings())
            user_entry = int(input("Enter 0 to go back: "))
        if user_entry == 2:
            print(Phone_settings())
        elif user_entry == 3:
            print(Security_settings())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Settings())
        elif user_entry == 4:
            print("Restore factory settings")
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(Settings())



    elif user_entry == 7:
        print(Call_divert())
        user_entry = int(input("Enter 0 to go back: "))
        if user_entry == 0:
            print(menu(user))

    elif user_entry == 8:
        print(Games())
        user_entry = int(input("Enter 0 to go back: "))
        if user_entry == 0:
            print(menu(user))

        elif user_entry == 9:
            print(Calculator())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(menu(user))

        elif user_entry == 10:
            print(Reminders())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(menu(user))

        elif user_entry == 11:
            print(Clock())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(menu(user))

        elif user_entry == 12:
            print(Profiles())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(menu(user))

        elif user_entry == 13:
            print(SIM_services())
            user_entry = int(input("Enter 0 to go back: "))
            if user_entry == 0:
                print(menu(user))
    counter += 1
