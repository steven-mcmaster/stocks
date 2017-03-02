class Stock:
    def __init__(self, ticker, cost, name):
        self.ticker = ticker
        self.cost = int(cost)
        self.name = name

    def __str__(self):
        return self.ticker + " " + self.name + " " + str(self.cost)


with open('file', 'r') as file:
    for line in file:
        try:
            s1 = Stock(*line.split(" ", 2))
            stock_dict[s1.ticker] = s1
        except:
            pass

user_data = input("Enter stuff: ")
stock_dict = {}
while(len(user_data)):
    try:
        s1 = Stock(*user_data.split(" ", 2))
        stock_dict[s1.ticker] = s1
    except:
        print("You are dumb")

    user_data = input("Enter stuff: ")

for x in stock_dict:
    print(stock_dict.get(x))

print()
print(*stock_dict.values(), sep="\n")
