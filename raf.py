from coinbase.wallet.client import Client


#initializing API key & secret from coinbase
api_key = '#######'
api_secret = '########'
client = Client(api_key, api_secret)

#creating an object for APIObject
account = "0x998dd1230AAb93e7B7f01878db960E615Ae15A79"

#This is turning the balance amount(BTC = #.####) to an integer
amount = float(account.balance.amount)

#Ratio threshold
thresh = 7299

#for buy triggers
pricelow1 = 2240
pricelow2 = 2375


#for sell triggers
mySellPrice = 8000

#Gets my account balance
#balance = account.balance

#Gets the current buy price for Bitcoin
buyPrice = client.get_buy_price().amount

#Gets the current sell price for Bitcoin
sellPrice = client.get_sell_price().amount
#Sell Price for Litecoin
sellPriceL = client.get_sell_price(currency_pair='LTC-USD').amount

#Gets the current price for Bitcoin
spotPrice = client.get_spot_price().amount

#Gets primary account which is Bitcoin wallet
#wallet = client.get_primary_account()

#Tests that can be deleted whenever
#print("Current buy price", buyPrice)
#print("Current sell price", sellPrice)
#print("Current spot price", spotPrice)
#print("My account balance:",account.balance)


ratio = float(buyPrice)/float(sellPrice) - 1
print("Calculated Ratio is ",ratio)


ths = float(thresh)
bp = float(buyPrice)
print("start loop>>")
buys = 0
sells = 0
while bp < ths:
    print("loop:This is the buy price", buyPrice)
   print("loop:This is the spot price", spotPrice)
   print("loop:This is my buy price low range ", pricelow1)
    print("loop:This is my buy price high range ", pricelow2)
    print("loop:My sell price ", mySellPrice)
    buyPrice = client.get_buy_price().amount
    buyPrice = input("buy price test input: ")
    bp = float(buyPrice)
    if (bp >= pricelow1) and (bp <= pricelow2):
        print("buying now this price:",bp)
      account.buy(amount='.000704225', currency='BTC')
        buys += 1
        if buys > 2:
            exit()
    sellPrice = client.get_sell_price().amount
    print("Sell price: ",sellPrice)
    sellPrice = input("Sell price input: ")
    print("Current sell price", sellPrice)
    if float(sellPrice) >= mySellPrice:
       print("selling now at ",sellPrice)
        account.sell(amount='.000704225', currency='BTC')
        sells += 1
        if sells > 2:
           exit()
    else:
        print("run loop again")



print(sellPriceL)
