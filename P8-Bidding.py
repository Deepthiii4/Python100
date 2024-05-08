name=input("What is your name ")
bid=input("What is your bid? : $")

dict={}
def create_Dict(name,bid):
    if name not in dict:
        dict[name]=bid
    else:
        print("Choose a different name")
    print(dict)
create_Dict(name,bid)
end=False
while end==False:
    more_bidders=input("Are there any other bidders? Type 'yes or 'no'")
    if more_bidders=="yes":
        name=input("What is your name ")
        bid=input("What is your bid? : $")
        create_Dict(name,bid)
    else:
        values=[]
        for value in dict:
            x=dict.get(value)
            values.append(x)
        max=max(values)
        winner_name=dict[max]
        print("The winner is "+winner_name+"with a bid of $"+max)
        end=True

