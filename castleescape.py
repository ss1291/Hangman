print(''' ___                    /\
                  `---|  /%%\/\
                     ,`./,--.\%\
                    /%%%\|  |--.\
                   /,---.|[]|  |
                    |]_'||__| [|
                    ||]|[|]|[| |
               ._..-':\._ ''/`-'.._.
        ._._.  |  _.:"'|-'`|-..__.:|  ._._.
        '._,'_.''_    _|  _| .-. ``'._'._.'
         | |_  ,'.\  '-| '-| |_|   [] _| |
    _____|]|-'|,++:_   ||] |_     _  '-|[|
    ~  ,-|`|  |+++|-'  |  _|-'   '-'   |.|  ~  
      ~) |_|__||  |    ; '-:         __|_|`-.___ ~
    _  \-._..''`--:.__/-'   \__..--''    __...-,'__
     `-,-'    _.-'-.   `---''   _____..')..-~~'|\
       `-._.-'`-._'`)         ,'`_..-~~' ~_____;'
            `. ~~ `.`.________`.( ~~  ___)
              )    ~`.\ '  '    ,'  ~\
            ,'|  ~    ')__:__:_( ~   |)
             `-...______________....-''')
print("Welcome to Castle Escape!!")
print("Your Mission is to Escape the Castle")
choice1 = input("You have three doors, red, yellow and blue.\n").lower()
if choice1 == "red":
 choice2 = input("You have found the escape door. You Win!!!").lower()
 if choice2 == "yellow":
    choice3 = input("You have water door, you drowned. Game Over!!").lower()
    if choice3 == "blue":
 
     print()
else:    
 print("You have choosen fire door. Game Over!!")
