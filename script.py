import random

def dict_cards():
    dicts = {}
    for i in range(1,53):
        dicts[i] = ''
    return dicts
dict_new = dict_cards()
poker_symbols = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']
poker_numbers = {'A':[1,14,27,40],'2':[2,15,28,41],'3':[3,16,29,42],'4':[4,17,30,43],'5':[5,18,31,44],'6':[6,19,32,45],'7':[7,20,33,46],'8':[8,21,34,47],'9':[9,22,35,48],'10':[10,23,36,49],'J':[11,24,37,50],'Q':[12,25,38,51],'K':[13,26,39,52]}
straight_translator = {0:'A',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'10',10:'J',11:'Q',12:'K',13:'A'}
hands_max = ['STRAIGHT','FLUSH','FULL HOUSE','STRAIGHT FLUSH','ROYAL FLUSH']
numbers_rank = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12,'♣':13,'♦':14,'♥':15,'♠':16}
hands_rank = {'HIGH CARD':0,'ONE PAIR':1,'TWO PAIR':2,'THREE OF A KIND':3,'STRAIGHT':4,'FLUSH':5,'FULL HOUSE':6,'FOUR OF A KIND':7,'STRAIGHT FLUSH':8,'ROYAL FLUSH':9}
def final_dic(dic):
    for i in range(len(poker_symbols)):
        dic[i+1] = poker_symbols[i]
    return dic
poker_cards = final_dic(dict_new)


class ProCards:  

  def __init__(self,name,money=100,money_p=100):
    self.name = name
    self.money = money
    self.money_p = money_p
    self.start_p = money_p
    self.round_on = False
    self.game_on = True
    self.winner = False
    self.bet = 0
    self.initial_bet = 0

  def __repr__(self):
    if self.money > 0:
        
        return '\n{} you have: ${} in cash!'.format(self.name,int(self.money))
    else:
        return '\n{} you have 0 money. No Cash, Double Looser.'.format(self.name)

  def heads_or_tails(self,option,money,percentage): 
    if money > self.money:
        print("You don't have enough money")
        return self.money
    elif money < 0:
        print("Your bet should be above 0")
        return self.money

    print("\nLet's play Heads or Tails!") 

    if option == "Heads":
        option = 1
    elif option == "Tails":
        option = 2
    else:
        print('\nEnter a correct option between "Heads" or "Tails"')
        return 
    
    percentage = 0.5 if percentage == '1' else 0.1

    value = random.randint(1,2)  
    result = 'Heads' if value == 1 else 'Tails'

    print('\nAnd the result is:\n{}'.format(result))

    if option == value:
        print("\nCongrats!! You just won on Heads or Tails.")
        self.money += money * percentage
        return self.money
    else:
        print("\nOh no! You just lost on Heads or Tails.")
        self.money -= money * percentage
        return self.money

  def cho_han(self,prediction,money,percentage):
    if money > self.money:
        print("You don't have enough money")
        return self.money
    elif money < 0:
        print("Your bet should be above 0")
        return self.money

    print("\nLet's play Cho-Han!") 

    percentage = 0.5 if percentage == '1' else 0.1

    if prediction == 'Odd' or prediction == 'Even':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        x = dice1 + dice2
        print('\nThe sum of the numbers is:\n{}'.format(x))
        value = 'Even' if x % 2 == 0 else 'Odd'
        if value == prediction:
            self.money += money * percentage
            print("\nCongrats!! You just won in Cho-Han.")
            return self.money
        else:
            self.money -= money * percentage
            print("\nOh no! You just lost in Cho-Han.")
            return self.money
    else:
        print('\nEnter a valid option between "Odd" or "Even"')
        return 
  
  def roulette(self,money,small_bet=None,big_bet=None,super_bet=None):
    if money > self.money:
        print("You don't have enough money")
        return self.money
    elif money < 0:
        print("Your bet should be above 0")
        return self.money

    print("\nLet's play Roulette!") 

    if super_bet != 'No':
        if money >= 10000:
            print("\nLet's play a super bet")
            number = random.randint(1,31)
            result = 'M' if number == 31 else number
            print('\nAnd the number is:\n{}!'.format(result))
            super_bet = 31
            if number == super_bet:
                self.money += 1000000000
                print('\n{}, You are offically a Millionare'.format(self.name))
                return self.money

            else:
                self.money -= 10000
                print('\n{}, You just lost 10 grand.'.format(self.name))
                return self.money
        else:
            print('\nYou need to have at least $10,000, to play a super bet')
        

    if big_bet != 'No':
        print("\nLet's play a big bet")
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))
        number3 = int(input('Third number: '))
        number4 = int(input('Fourth number: '))
        number = random.randint(1,31)
        print('1:{}\n2:{}\n3:{}\n4:{}'.format(number1,number2,number3,number4))
        print('\nAnd the number is:\n{}!'.format(number))
        if number1 == number or number2 == number or number3 == number or number4 == number:
            self.money += money * 10
            print('\nYou won a big bet')
            return self.money

        else:
            self.money -= money 
            print('\nYou just lost a big bet')
            return self.money

    if small_bet != 'No':
        print("\nLet's play a small bet")
        number = random.randint(1,31)
        print('\nAnd the number is:\n{}!'.format(number))
        if small_bet == 'Odd' or small_bet == 'Even':
            x = 'Even' if number % 2 == 0 else 'Odd'
            if x == small_bet:
                self.money += money * 0.5
                print('\nYou just won a small bet')
                return self.money
            else:
                self.money -= money * 0.5
                print('\nYou just lost a small bet')
                return self.money
        else:
            print('\nEnter a valid option between "Even" or "Odd"')
            return          

  def more_cards(self,lst,inputt=True):  
    if inputt:
        choice = input('Enter "1" to see the next card ')
        while choice != '1':
            choice = input('Enter "1" to see the next card ')
    card = random.randint(1,52)
    while card in lst:
        card = random.randint(1,52)
    lst.append(card)
    return card
  
  def turn(self,cards):
    turn = True
    h_status, no_key = self.status(cards)
    max_p = [1,3,5,6,7,9,10]
    while turn:
        choice = input('Enter 1 to bet\nEnter 2 to pass\nEnter 3 to leave\n')
        if choice == '1':
            print('Current amount of money: {}'.format(self.money_p))
            choice = input('How much money do you want to bet?: ')
            number = random.randint(1,10)
            if int(choice) > 0 and int(choice) <= self.money_p:
                self.money_p -= int(choice)
                self.bet += int(choice)   
                if hands_rank[h_status] >= 2:
                    turn = self.house_matches(choice)
                elif int(choice) > self.money_p // 2.4:
                    if hands_rank[h_status] >= 1:
                        if number in max_p:   
                            turn = self.house_matches(choice)
                        else:
                            turn = self.house_leaves()
                    else:
                        if number in max_p:   
                            turn = self.house_leaves()
                        else:
                            turn = self.house_matches(choice)                       
                else:   
                    if number in max_p:   
                        turn = self.house_matches(choice)
                    else:
                        turn = self.house_leaves()
            else:
                print('You dont have that amount of money. Try again.')
        elif choice == '2':
            if self.money_p > 5:
                number = random.randint(1,10)
                if hands_rank[h_status] >= 1:
                    if hands_rank[h_status] >= 3:
                        turn  = self.house_bet(self.money//3,self.money_p//1.6)
                    else:
                        if number in max_p:
                            turn = self.house_bet(5,self.money_p//3)
                        else:
                            turn = False
                            print('The House also passes!\n')
                else:
                    if number in max_p:
                        turn = False
                        print('The House also passes!\n')
                    else:
                        turn = self.house_bet(5,self.money_p//2.3)
            else:
                print('The House also passes!!')
                turn = False
        elif choice == '3':
            turn = False
            self.round_on = False
        else:
            print('Enter a valid option.')
   
  def house_bet(self,minn,maxx):
    amount = random.randint(minn,maxx)
    self.bet += amount 
    print('The House raises the bet to ${} more'.format(amount))
    decision = input('Enter "1" to match it and "2" to leave: ')
    if decision == '1':
        print('{} matches the bet!\n'.format(self.name))
        self.money_p -= amount
        self.bet += amount
        return False
    else:
        self.round_on = False
        return False
  
  def house_passes(self):
    print('The House also passes!\n')
    return False

  def house_leaves(self):
    print('The House decided to leave.\n')
    self.winner = True
    self.round_on = False
    self.money_p += self.bet
    return False

  def house_matches(self,choice):
    self.bet += int(choice)     
    print('The House matches the bet!\n')
    return False

  def end_of_level(self):
    if self.money_p >= 500:
        self.game_on = False 
        print('\n\n\n\n\n\nYou conquered the First Level of ProCards!!\n\nCongratulations, you are "La Neta"\nNow you will advance to the second level. Good Luck.\n')
        print('This your current amount of money: {}'.format(self.money_p))
        return True

  def counter(self,cards):
    poker_count = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0,'A':0}
    flush_count = {'♣':0,'♦':0,'♥':0,'♠':0}
    straight_count = {'A':[0,13],'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12}
    straight_lst = []
    for card in cards:
        symbol = poker_cards[card]
        number = symbol[:-1]
        flush = symbol[-1]
        for x in poker_count:
            if number == x:
                poker_count[x] += 1
        for y in flush_count:
            if flush == y:
                flush_count[y] += 1
        for z in straight_count:
            if number == z:
                if number == 'A':
                    if not straight_count[number] in straight_lst:
                        straight_lst.append(straight_count[number][0])
                        straight_lst.append(straight_count[number][1])
                else:
                    if not straight_count[number] in straight_lst:
                        straight_lst.append(straight_count[number])

       
    return poker_count, flush_count, straight_lst

  def straight_flush(self,cards):
    numbers = {'♣':[],'♦':[],'♥':[],'♠':[]}
    for card in cards:
        number = poker_cards[card]
        symbol = number[-1]
        numbers[symbol].append(card)
    
    lst_numbers = []
    for symbol in numbers:
        if len(numbers[symbol]) >= 5:
            for num in numbers[symbol]:
                lst_numbers.append(num)
    if len(lst_numbers) < 5:
        return False
    

    straight_lst = []
    straight_count = {'A':[0,13],'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12}
    for card in lst_numbers:
        symbol = poker_cards[card]
        number = symbol[:-1]
        for z in straight_count:
            if number == z:
                if number == 'A':
                    if not straight_count[number] in straight_lst:
                        straight_lst.append(straight_count[number][0])
                        straight_lst.append(straight_count[number][1])
                else:
                    if not straight_count[number] in straight_lst:
                        straight_lst.append(straight_count[number])

    
    return straight_lst

  def hand(self,cards,dict1,dict2,dict3):
    #ROYAL FLUSH 
    royal_f = [40,49,50,51,52]
    count_rf = '♠'
    count = 0
    for card in royal_f:
        if cards.count(card) > 0:
            count += 1
    if count == 5:
        return 'ROYAL FLUSH', count_rf
    #END ROYAL FLUSH TEST

    #STRAIGHT FLUSH
    count_sf = 0
    straight_numbers = False
    sf_key = False
    dict4 = self.straight_flush(cards)
    if dict4:
        for i in range(len(sorted(dict4))-1):
            start = dict4[i]
            if dict4[i+1] - 1 == start:
                count_sf+=1
                sf_key = dict4[i+1]
                if count_sf >= 4:
                    straight_numbers = True
            else:
                count_sf = 0    
        if straight_numbers:
            return 'STRAIGHT FLUSH', straight_translator[sf_key]
    #END STRAIGHT FLUSH TEST

    #FOUR OF A KIND
    for key,value in dict1.items():
        if value == 4:
            return 'FOUR OF A KIND', key
    #END FOUR OF KIND TEST
    
    #FULL HOUSE
    count3_fh = False
    count2_fh = False
    for key,value in dict1.items():
        if value == 3:
            count3_fh = key
        elif value == 2:
            count2_fh = key
    if count3_fh and count2_fh:
        return 'FULL HOUSE', count3_fh
    #END FULL HOUSE TEST

    #COLOR
    for key,value in dict2.items():
        if value >= 5:
            return 'FLUSH', key
    #END COLOR TEST

    #STRAIGHT
    count_st = 0
    straight = False
    st_key = False
    sort_dict = sorted(dict3)
    for i in range(len(sort_dict)-1):
        start = sort_dict[i]
        if sort_dict[i+1] - 1 == start:
            count_st+=1
            st_key = sort_dict[i+1]
            if count_st >= 4:
                straight = True
        else:
            count_st = 0
    if straight:
        return 'STRAIGHT' , straight_translator[st_key]
    #END STRAIGHT TEST

    #THREE OF A KIND
    three_key = False
    for key,value in dict1.items():
        if value == 3:
            three_key = key
    if three_key:
        return 'THREE OF A KIND', three_key
    #END THREE OF A KIND TEST

    #TWO PAIR
    count_tp = 0
    two_key = False
    for key,value in dict1.items():
        if value == 2:
            count_tp += 1
            two_key = key
    if count_tp >= 2:
        return 'TWO PAIR', two_key
    #END TWO PAIR TEST

    #PAIR
    for key,value in dict1.items():
        if value == 2:
            return 'ONE PAIR', key
    #END PAIR TEST 
    
    #HIGH CARD
    my_card1 = cards[0]
    my_card2 = cards[1]
    card1 = poker_cards[my_card1]
    number = card1[:-1]
    card2 = poker_cards[my_card2]
    number2 = card2[:-1]
    if numbers_rank[number] > numbers_rank[number2]:
        return 'HIGH CARD', number
    else:
        return 'HIGH CARD', number2
    #END HIGH CARD TEST

  def status(self,cards):
    p, f, s = self.counter(cards)
    status, key = self.hand(cards,p,f,s)
    return status, key

  def poker(self,poker_crush=True):
    if self.money_p > self.money:
        print("You don't have enough money")
        return self.money
    elif self.money_p < 0:
        print("Your bet should be above 0")
        return self.money
    

    while self.game_on and self.money_p >= 5:
        cards = []
        self.money_p -= 5
        self.initial_bet = 5 * 2
        self.bet = self.initial_bet
        self.round_on = True
        self.winner = False
        while self.round_on:
            house_cards = []
            card1 = self.more_cards(cards)
            print('Your first card:        {}\n'.format(poker_cards[card1]))
            card2 = self.more_cards(cards,False)
            print('Your second card:       {}\n'.format(poker_cards[card2]))
            house_card1 = self.more_cards(cards,False)
            house_cards.append(house_card1)
            house_card2 = self.more_cards(cards,False)
            house_cards.append(house_card2)

            table_card1 = self.more_cards(cards)
            print('Table first card:       {}\n'.format(poker_cards[table_card1]))
            house_cards.append(table_card1)
            table_card2 = self.more_cards(cards,False)
            print('Table second card:      {}\n'.format(poker_cards[table_card2]))
            house_cards.append(table_card2)
            table_card3 = self.more_cards(cards,False)
            print('Table third card:       {}\n'.format(poker_cards[table_card3]))  
            house_cards.append(table_card3)
            

            print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3]))
            self.turn(house_cards)           
   

            if self.round_on:
                table_card4 = self.more_cards(cards)
                print('Table fourth card:      {}\n'.format(poker_cards[table_card4]))
                house_cards.append(table_card4)
                 
                print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4]))
                self.turn(house_cards)

                if self.round_on:
                    table_card5 = self.more_cards(cards)
                    print('Table fifth card:       {}\n'.format(poker_cards[table_card5]))
                    house_cards.append(table_card5)

                    print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4],poker_cards[table_card5]))
                    self.turn(house_cards)
                    
                    if self.round_on:
                        print('The house first card:     {}\n'.format(poker_cards[house_card1]))
                        print('The house second card:    {}\n'.format(poker_cards[house_card2]))
                        self.round_on = False
                        my_cards = [card1,card2,table_card1,table_card2,table_card3,table_card4,table_card5]

                
                        my_hand, my_hc = self.status(my_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format(self.name,my_hand,my_hc))
                        house_hand, house_hc= self.status(house_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format('The House',house_hand,house_hc))
                        if hands_rank[my_hand] > hands_rank[house_hand]:
                            self.winner = True
                            self.money_p += self.bet
                            print('{} is higher than {}\n'.format(my_hand,house_hand))
                        elif hands_rank[my_hand] < hands_rank[house_hand]:
                            print('{} is higher than {}\n'.format(house_hand,my_hand))
                        elif hands_rank[my_hand] == hands_rank[house_hand]:
                            print('There has been a tie of hands\n')
                            if numbers_rank[my_hc] > numbers_rank[house_hc]:
                                self.winner = True
                                self.money_p += self.bet
                                print('{} of {} is higher than {} of {}\n'.format(my_hand,my_hc,house_hand,house_hc))
                            elif numbers_rank[my_hc] < numbers_rank[house_hc]:
                                print('{} of {} is higher than {} of {}\n'.format(house_hand,house_hc,my_hand,my_hc))
                            elif numbers_rank[my_hc] == numbers_rank[house_hc]:
                                print('There has been a tie of hands and its high card.\n')
                                my_hand2, my_hc2 = self.status([card1,card2])
                                house_hand2, house_hc2 = self.status([house_card1,house_card2])
                                if numbers_rank[my_hc2] > numbers_rank[house_hc2] and my_hand not in hands_max:
                                    self.winner = True
                                    self.money_p += self.bet
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format(self.name,my_hand2,my_hc2,'The House',house_hand2,house_hc2))
                                elif numbers_rank[my_hc2] < numbers_rank[house_hc2] and my_hand not in hands_max:
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format('The House',house_hand2,house_hc2,self.name,my_hand2,my_hc2))     
                                else:
                                    print('There has been a tie of hands and its high card and also the high cards of the players.\nIn these situations The House Wins.')

    
        print('\nRound finished. The winner of the round is: {}!!!!!'.format(self.name if self.winner else 'THE HOUSE'))
        print('The winner of the round takes: ${}\n'.format(self.bet))
        
        if self.end_of_level() and poker_crush:
            return self.money_p

        game_status = input('Enter "1" If you want to keep playing\nEnter "2" If you want to leave the game\n')
        enter = True
        while enter:
            if game_status == '1':
                self.game_on = True 
                enter = False
            elif game_status == '2':
                self.game_on = False
                enter = False
            else: 
                print('Invalid option, try again.')




    print('\n\nThanks {} for playing Poker in ProCards\nCurrent Poker Money: ${}'.format(self.name,self.money_p))
    total = self.money_p - self.start_p
    if total > 0:
        print('You won {} dollars. See you Next TIME!\n'.format(int(total)))
    else:
        total = total // -1
        print('You lost {} dollars. See you Next TIME!\n'.format(total))
        
  def play(self):
    start_m = self.money
    keep_going = True
    print('\nHi, Welcome to ProCards.')
    while self.money > 0 and keep_going:
        print(self)
        print('Which game would you want to play?\n We have this options: \n 1: "Heads or Tails"\n 2: "Cho-Han"\n 3: "Roulette"\n')
        choice = input("Choose your option here: ")

        if choice == 'Heads or Tails' or choice == '1':
            choice = input('Choose between "Heads" or "Tails": ')
            if choice == 'Heads' or choice == 'Tails':   
                choice_m = input('\nHow much money do you want to bet? ')
                choice_p = input('Enter "1" for a bet of 50% percent and "2" for a bet of 10%: ')
                self.money = self.heads_or_tails(choice,int(choice_m),choice_p)
        
        elif choice == 'Cho-Han' or choice == '2':
            choice = input('Choose between "Odd" or "Even": ')
            choice_m = input('\nHow much money do you want to bet? ')
            choice_p = input('Enter "1" for a bet of 50% percent and "2" for a bet of 10%: ')
            self.money = self.cho_han(choice,int(choice_m),choice_p)

        elif choice == 'Roulette' or choice == '3':
            choice1 = input('For Small Bet (Optional):\nChoose between "Odd" or "Even". If you dont want a small bet put "No": ')
            choice2 = input('For Big Bet (Optional):\nFor an all in put "Yes". If you dont want a big bet put "No": ')
            choice3 = input('For Super Bet (Optional):\nIf you like risks put "Yes". If you dont want a super bet put "No": ')
            choice_m = input('\nHow much money do you want to bet? ')
            self.money = self.roulette(int(choice_m),choice1,choice2,choice3)
        
        else:
            print('Enter a valid option')
        if self.money > 0:
            answer = input('Do you want to keep gambling?\n"Yes" or "No".\n')
            if answer == 'No':
                keep_going = False

    print('\nThank you for being here {}.\nYour total amount of money is ${}'.format(self.name,int(self.money)))
    total = self.money - start_m
    if total > 0:
        print('You won {} dollars. See you Next TIME!'.format(int(total)))
    else:
        new = total // -1
        print('You lost {} dollars. See you Next TIME!'.format(new))

class ProCards2(ProCards):
  def turn(self,cards):
    turn = True
    h_status, no_key = self.status(cards)
    cards2 = cards[2:]
    t_status, no_key = self.status(cards2)
    max_p = [1,3,5,6,7,9,10]
    number = random.randint(1,10)
    while turn:
        choice = input('Enter 1 to bet\nEnter 2 to pass\nEnter 3 to leave\n')
        if choice == '1':
            print('Current amount of money: {}'.format(self.money_p))
            choice = input('How much money do you want to bet?: ')
            if int(choice) >= (self.initial_bet//2) and int(choice) <= self.money_p:
                self.money_p -= int(choice)
                self.bet += int(choice)   
                if hands_rank[h_status] >= 2:
                    turn = self.house_matches(choice)

                elif hands_rank[t_status] >= 1 and hands_rank[h_status] < 1:
                    if int(choice) > self.money_p // 2:
                        turn = self.house_leaves()
                    else:
                        if number in max_p:
                            turn = self.house_leaves()
                        else:
                            turn = self.house_matches(choice)

                elif hands_rank[t_status] < 1 and hands_rank[h_status] >= 1:
                    turn = self.house_matches(choice)
                elif hands_rank[t_status] < 1 and hands_rank[h_status] < 1:
                    if int(choice) > self.money_p // 2:
                        if number in max_p:
                            turn = self.house_leaves()
                        else:
                            turn = self.house_matches(choice)
                    else: 
                        if number in max_p:
                            turn = self.house_matches(choice)
                        else:
                            turn = self.house_leaves()
                else:
                    turn = self.house_matches(choice)
            else:
                print('You have to bet over the initial bet: {}. Try again.'.format(self.initial_bet//2))
        elif choice == '2':
            if self.money_p > 7:
                if hands_rank[h_status] >= 1:
                    if hands_rank[t_status] >= 1:
                        if number in max_p:
                            turn = self.house_bet(1,self.money_p//2.7) 
                        else:
                            turn = False
                            print('The House also passes!\n')
                                 
                    else:
                        turn = self.house_bet(self.money_p//2,self.money_p//1.7)     
                else:
                    if hands_rank[t_status] >= 1:
                        turn = False
                        print('The House also passes!\n')
                    else:
                        if number in max_p: 
                            turn = False
                            print('The House also passes!\n')
                        else:
                            turn = self.house_bet(1,self.money_p//4)                  
            else:
                print('The House also passes!!')
                turn = False
        elif choice == '3':
            turn = False
            self.round_on = False
        else:
            print('Enter a valid option.')
  def end_of_level(self):
    if self.money_p >= 1000:
        self.game_on = False 
        print('\n\n\n\n\nYou conquered the Second Level of ProCards!!\nCongratulations, you are "Buenisimo en esto."\nNow you will advance to the third and final level. Good Luck, you will need it.\n')
        print('This your current amount of money: {}'.format(self.money_p))
        return self.money_p
  
class ProCards3(ProCards2):
  def poker(self):
    add = 0

    while self.game_on and self.money_p > 0:
        cards = []
        add += 100 
        self.round_on = True
        self.winner = False
        no_bet_money = False
        if self.money_p <= add:
            no_bet_money = True
        while self.round_on and no_bet_money == False:
            self.money_p -= add
            self.initial_bet = add * 2
            self.bet = self.initial_bet
            print(self.bet)
            print('The initial bet is {} each'.format(add)) 
            house_cards = []
            card1 = self.more_cards(cards)
            print('Your first card:        {}\n'.format(poker_cards[card1]))
            card2 = self.more_cards(cards,False)
            print('Your second card:       {}\n'.format(poker_cards[card2]))
            house_card1 = self.more_cards(cards,False)
            house_cards.append(house_card1)
            house_card2 = self.more_cards(cards,False)
            house_cards.append(house_card2)

            table_card1 = self.more_cards(cards)
            print('Table first card:       {}\n'.format(poker_cards[table_card1]))
            house_cards.append(table_card1)
            table_card2 = self.more_cards(cards,False)
            print('Table second card:      {}\n'.format(poker_cards[table_card2]))
            house_cards.append(table_card2)
            table_card3 = self.more_cards(cards,False)
            print('Table third card:       {}\n'.format(poker_cards[table_card3]))  
            house_cards.append(table_card3)
            

            print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3]))
            self.turn(house_cards)           
   

            if self.round_on:
                table_card4 = self.more_cards(cards)
                print('Table fourth card:      {}\n'.format(poker_cards[table_card4]))
                house_cards.append(table_card4)
                 
                print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4]))
                self.turn(house_cards)

                if self.round_on:
                    table_card5 = self.more_cards(cards)
                    print('Table fifth card:       {}\n'.format(poker_cards[table_card5]))
                    house_cards.append(table_card5)

                    print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4],poker_cards[table_card5]))
                    self.turn(house_cards)
                    
                    if self.round_on:
                        print('The house first card:     {}\n'.format(poker_cards[house_card1]))
                        print('The house second card:    {}\n'.format(poker_cards[house_card2]))
                        self.round_on = False
                        my_cards = [card1,card2,table_card1,table_card2,table_card3,table_card4,table_card5]

                
                        my_hand, my_hc = self.status(my_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format(self.name,my_hand,my_hc))
                        house_hand, house_hc= self.status(house_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format('The House',house_hand,house_hc))
                        if hands_rank[my_hand] > hands_rank[house_hand]:
                            self.winner = True
                            self.money_p += self.bet
                            print('{} is higher than {}\n'.format(my_hand,house_hand))
                        elif hands_rank[my_hand] < hands_rank[house_hand]:
                            print('{} is higher than {}\n'.format(house_hand,my_hand))
                        elif hands_rank[my_hand] == hands_rank[house_hand]:
                            print('There has been a tie of hands\n')
                            if numbers_rank[my_hc] > numbers_rank[house_hc]:
                                self.winner = True
                                self.money_p += self.bet
                                print('{} of {} is higher than {} of {}\n'.format(my_hand,my_hc,house_hand,house_hc))
                            elif numbers_rank[my_hc] < numbers_rank[house_hc]:
                                print('{} of {} is higher than {} of {}\n'.format(house_hand,house_hc,my_hand,my_hc))
                            elif numbers_rank[my_hc] == numbers_rank[house_hc]:
                                print('There has been a tie of hands and its high card.\n')
                                my_hand2, my_hc2 = self.status([card1,card2])
                                house_hand2, house_hc2 = self.status([house_card1,house_card2])
                                if numbers_rank[my_hc2] > numbers_rank[house_hc2] and my_hand not in hands_max:
                                    self.winner = True
                                    self.money_p += self.bet
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format(self.name,my_hand2,my_hc2,'The House',house_hand2,house_hc2))
                                elif numbers_rank[my_hc2] < numbers_rank[house_hc2] and my_hand not in hands_max:
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format('The House',house_hand2,house_hc2,self.name,my_hand2,my_hc2))     
                                else:
                                    print('There has been a tie of hands and its high card and also the high cards of the players.\nIn these situations The House Wins.')
        enter = True
        if no_bet_money:
            self.money_p *= -1
            enter = False
            print("You don't have enough money to bet, you've lost.")
        else:
            print('\nRound finished. The winner of the round is: {}!!!!!'.format(self.name if self.winner else 'THE HOUSE'))
            print('The winner of the round takes: ${}\n'.format(self.bet))

        
        
        while enter:
            game_status = input('Enter "1" If you want to keep playing\nEnter "2" If you want to leave the game\n')
            if game_status == '1':
                self.game_on = True 
                enter = False
            elif game_status == '2':
                self.game_on = False
                enter = False
            else: 
                print('Invalid option, try again.')
    

    if self.money_p > 0:
        print("\nIt's official: You just have finished Pro Cards!!!!")
        print('Go with the founders and you can cash your poker money with fake money or with favors.')
        print('We wish you had a great time.')   
        print('\n\nCongratulations {} for finishing all level of Poker in ProCards\nCurrent Poker Money: ${}'.format(self.name,self.money_p))
        print('You won {} dollars in the whole game. See you Next TIME!\nYou will always have a place in our hearts.\n{} is now in "PRO CARDS HALL OF FAME."'.format(int(self.money_p-100),self.name))
    else:
        total = self.start_p + (self.money_p // -1)
        print("\n\nYou almost did it. Keep on trying and never give up on what you want. Because if you do, what's left?")
        print("The money that you had left, now it's on the house")
        print('You lost {} dollars. See you Next TIME!\n'.format(total))

class ProCardsPro(ProCards):
  def __init__(self,name,money,money_p):
    super().__init__(name,money,money_p)
    self.passive = 0
    self.bluffer = 0
    self.bluff = False
    self.house_left = False
    self.house_patience = 0

  def house_leaves(self):
    print('The House decided to leave.\n')
    self.winner = True
    self.house_left = True
    self.round_on = False
    self.money_p += self.bet
    return False

  def turn(self,cards,last_turn):
    turn = True
    h_status, h_key = self.status(cards)
    cards2 = cards[2:]
    t_status, t_key = self.status(cards2)
    max_p = [1,3,5,6,7,9,10]
    number = random.randint(1,10)
    while turn:
        choice = input('Enter 1 to bet\nEnter 2 to pass\nEnter 3 to leave\n')
        if choice == '1':
            print('Current amount of money: {}'.format(self.money_p))
            choice = input('How much money do you want to bet?: ')
            if int(choice) >= (self.initial_bet//2) and int(choice) <= self.money_p:
                if int(choice) > self.money_p // 3:
                    self.bluff = 'Yes'
                else:
                    self.bluff = 'No'
                self.money_p -= int(choice)
                self.bet += int(choice)   

                if numbers_rank[h_key] > numbers_rank[t_key] and hands_rank[h_status] > hands_rank[t_status]:
                    turn = self.house_matches(choice)


                elif not (numbers_rank[h_key] > numbers_rank[t_key]) and hands_rank[h_status] > hands_rank[t_status]:
                    if hands_rank[h_status] > 2:
                        turn = self.house_matches(choice)
                    elif int(choice) > self.money_p // 3:            
                        if self.bluffer > self.passive:
                            turn = self.house_matches(choice)
                        else:
                            if number in max_p:
                                turn = self.house_leaves()
                            else:
                                turn = self.house_matches(choice)
                    else:
                        if self.passive > self.bluffer and last_turn:
                            if number in max_p:
                                turn = self.house_leaves()
                            else:
                                turn = self.house_matches(choice)
                        else:
                            turn = self.house_matches(choice)


                elif numbers_rank[h_key] > numbers_rank[t_key] and not (hands_rank[h_status] > hands_rank[t_status]):
                    if int(choice) > self.money_p // 3:
                        if self.bluffer > self.passive:
                            if number in max_p:
                                turn = self.house_matches(choice)
                            else:
                                turn = self.house_leaves()
                        else:
                            turn = self.house_leaves()
                    else:
                        if self.passive > self.bluffer and last_turn:
                            turn = self.house_leaves()
                        else:
                            if number in max_p:
                                turn = self.house_matches(choice)
                            else:
                                turn = self.house_leaves()
                
                else:
                    if self.house_patience > 2:
                        if number in max_p:
                            turn = self.house_matches(choice)
                            self.house_patience = 0
                        else:
                            turn = self.house_leaves()
                    elif int(choice) > self.money_p // 3.5:
                        turn = self.house_leaves()
                        self.house_patience += 1
                    else:
                        if not last_turn and int(choice) < self.money_p // 5.5 :
                            if number in max_p:
                                turn = self.house_matches(choice)
                            else:
                                turn = self.house_leaves()
                        else:
                            if self.bluffer > self.passive:
                                if number in max_p:
                                    turn = self.house_matches(choice)
                                else:
                                    turn = self.house_leaves()
                            else:
                                if number in max_p:
                                    turn = self.house_leaves()
                                else: 
                                    turn = self.house_matches(choice)
           
              
            else:
                print('You have to bet over the initial bet: {}. Try again.'.format(self.initial_bet//2))
        elif choice == '2':
            if self.money_p > 20:
                if numbers_rank[h_key] > numbers_rank[t_key] and hands_rank[h_status] > hands_rank[t_status]:
                    turn = self.house_bet(self.money_p//3.3,self.money_p//1.6)


                elif not (numbers_rank[h_key] > numbers_rank[t_key]) and hands_rank[h_status] > hands_rank[t_status]:
                    if hands_rank[h_status] > 2:
                        turn = self.house_bet(self.money_p//11,self.money_p//2.9)
                    elif self.bluffer > self.passive:
                        turn = self.house_bet(self.money_p//5,self.money_p//3.3)
                    else:
                        if number in max_p:
                            turn = self.house_passes()
                        else:
                            turn = self.house_bet(self.money_p//20,self.money_p//10)

                elif numbers_rank[h_key] > numbers_rank[t_key] and not (hands_rank[h_status] > hands_rank[t_status]):
                    if self.bluffer > self.passive:
                        if number in max_p:
                            turn = self.house_bet(self.money_p//9,self.money_p//2.5)
                        else:
                            turn = self.house_passes()
                    else:
                        if number in max_p:
                            turn = self.house_passes()
                        else:
                            turn = self.house_bet(self.money_p//20,self.money_p//11)
                
                else:
                    turn = self.house_passes()            
            else:
                print('The House also passes!!')
                turn = False
        elif choice == '3':
            turn = False
            self.round_on = False
        else:
            print('Enter a valid option.')
  
  def poker(self):
    
    self.start_p = self.money_p
    while self.game_on and self.money_p >= 5:
        cards = []
        self.money_p -= 10
        self.initial_bet = 10 * 2
        self.bet = self.initial_bet
        self.round_on = True
        self.winner = False
        self.house_left = False
        while self.round_on:
            house_cards = []
            card1 = self.more_cards(cards)
            print('Your first card:        {}\n'.format(poker_cards[card1]))
            card2 = self.more_cards(cards,False)
            print('Your second card:       {}\n'.format(poker_cards[card2]))
            house_card1 = self.more_cards(cards,False)
            house_cards.append(house_card1)
            house_card2 = self.more_cards(cards,False)
            house_cards.append(house_card2)

            table_card1 = self.more_cards(cards)
            print('Table first card:       {}\n'.format(poker_cards[table_card1]))
            house_cards.append(table_card1)
            table_card2 = self.more_cards(cards,False)
            print('Table second card:      {}\n'.format(poker_cards[table_card2]))
            house_cards.append(table_card2)
            table_card3 = self.more_cards(cards,False)
            print('Table third card:       {}\n'.format(poker_cards[table_card3]))  
            house_cards.append(table_card3)
            

            print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3]))
            self.turn(house_cards,False)           
   

            if self.round_on:
                table_card4 = self.more_cards(cards)
                print('Table fourth card:      {}\n'.format(poker_cards[table_card4]))
                house_cards.append(table_card4)
                 
                print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4]))
                self.turn(house_cards,False)

                if self.round_on:
                    table_card5 = self.more_cards(cards)
                    print('Table fifth card:       {}\n'.format(poker_cards[table_card5]))
                    house_cards.append(table_card5)

                    print('Your Cards: [{}, {}]\nThe Table Cards: [{}, {}, {}, {}, {}]\n'.format(poker_cards[card1],poker_cards[card2],poker_cards[table_card1],poker_cards[table_card2],poker_cards[table_card3],poker_cards[table_card4],poker_cards[table_card5]))
                    self.turn(house_cards,True)
                    
                    if self.round_on:
                        print('The house first card:     {}\n'.format(poker_cards[house_card1]))
                        print('The house second card:    {}\n'.format(poker_cards[house_card2]))
                        self.round_on = False
                        self.house_patience = 0
                        my_cards = [card1,card2,table_card1,table_card2,table_card3,table_card4,table_card5]

                
                        my_hand, my_hc = self.status(my_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format(self.name,my_hand,my_hc))
                        house_hand, house_hc= self.status(house_cards)
                        print('{} has a hand of: {} with {}!!!!!\n'.format('The House',house_hand,house_hc))
                        if hands_rank[my_hand] > hands_rank[house_hand]:
                            self.winner = True
                            self.money_p += self.bet
                            print('{} is higher than {}\n'.format(my_hand,house_hand))
                        elif hands_rank[my_hand] < hands_rank[house_hand]:
                            print('{} is higher than {}\n'.format(house_hand,my_hand))
                        elif hands_rank[my_hand] == hands_rank[house_hand]:
                            print('There has been a tie of hands\n')
                            if numbers_rank[my_hc] > numbers_rank[house_hc]:
                                self.winner = True
                                self.money_p += self.bet
                                print('{} of {} is higher than {} of {}\n'.format(my_hand,my_hc,house_hand,house_hc))
                            elif numbers_rank[my_hc] < numbers_rank[house_hc]:
                                print('{} of {} is higher than {} of {}\n'.format(house_hand,house_hc,my_hand,my_hc))
                            elif numbers_rank[my_hc] == numbers_rank[house_hc]:
                                print('There has been a tie of hands and its high card.\n')
                                my_hand2, my_hc2 = self.status([card1,card2])
                                house_hand2, house_hc2 = self.status([house_card1,house_card2])
                                if numbers_rank[my_hc2] > numbers_rank[house_hc2] and my_hand not in hands_max:
                                    self.winner = True
                                    self.money_p += self.bet
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format(self.name,my_hand2,my_hc2,'The House',house_hand2,house_hc2))
                                elif numbers_rank[my_hc2] < numbers_rank[house_hc2] and my_hand not in hands_max:
                                    print("{}'s {} of {} is higher than {}'s {} of {}\n".format('The House',house_hand2,house_hc2,self.name,my_hand2,my_hc2))     
                                else:
                                    print('There has been a tie of hands and its high card and also the high cards of the players.\nIn these situations The House Wins.')

    
        print('\nRound finished. The winner of the round is: {}!!!!!'.format(self.name if self.winner else 'THE HOUSE'))
        print('The winner of the round takes: ${}\n'.format(self.bet))
        
        if not self.winner and self.bluff == 'Yes' and not self.house_left:
            self.bluffer += 1
        
        if self.winner and self.bluff == 'No' and not self.house_left:
            self.passive += 1

        enter = True
        while enter:
            game_status = input('Enter "1" If you want to keep playing\nEnter "2" If you want to leave the game\n')
            if game_status == '1':
                self.game_on = True 
                enter = False
            elif game_status == '2':
                self.game_on = False
                enter = False
            else: 
                print('Invalid option, try again.')




    print('\n\nThanks {} for playing Poker in ProCards\nCurrent Poker Money: ${}'.format(self.name,self.money_p))
    total = self.money_p - self.start_p
    if total > 0:
        print('You won {} dollars. See you Next TIME!\n'.format(int(total)))
    else:
        total = total // -1
        print('You lost {} dollars. See you Next TIME!\n'.format(total))
     
    
name = input('Hello!\nWhat is your name? ')

print('\nWhich game would you want to play?\n')
choice = input('Enter "1" for a QUICK GAMBLE\nEnter "2" for a POKER GAME\nEnter "3" for a POKER CRUSH (New)\n')


if choice == '1':
    user = ProCards(name)
    user.play()
elif choice == '2':  
    level = input('Enter "1" for Easy\nEnter "2" for Medioum\nEnter "3" for Hard\n')
    if level == '1':
        user.poker(False)
    elif level == '2':
        user2 = ProCards2(name,200,200)
        user2.poker(False)
    elif level == '3':
        user3 = ProCardsPro(name,300,300)
        user3.poker()
    else: 
        print('Please enter a valid option. Try again.')
elif choice == '3':
    user = ProCards(name)
    money = user.poker()
    if money:
        print('\nHello! Welcome to the Second Level {}!!!\nYou are now officially a Silver Member of this game comunnity.'.format(name))
        name1 = name.title() + ' (silver member)'
        user2 = ProCards2(name1,money,money)
        money2 = user2.poker()

        if money2:
            print('\nHello! Welcome to the Third and Final Level {}!!!\nYou are now officially a Gold Member of this game comunnity.'.format(name))
            name2 = name.upper() + ' (GOLD Member)'
            user2 = ProCards3(name2,money2,money2)
            user2.poker()
else: 
        print('Please enter a valid option. Try again.')

