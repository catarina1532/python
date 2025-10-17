acceptable_coins = ['25', '10', '5'] #list of coin values that the machine accepts
total_inserted = 0 #how much the user has inserted so far

#star a loop until the user still owes money (less than 50)
while total_inserted < 50:
    print('Amount Due:', 50 - total_inserted) #show how much is still due
    coin_provided = input('Insert Coin: ').strip() #prompt user for a coin
    if coin_provided in acceptable_coins: #only accept valid coins
        total_inserted += int(coin_provided) #converts the string to an integer and adds it to the running total
#if coin is not valid, do nothing
#when total_inserted reaches 50 or more, the while condition becomes false and the loop stops
if total_inserted >= 50:
    change_owed = total_inserted - 50
    print('Change Owed:', change_owed) #show the change owed
