import pandas
data = pandas.read_csv("/Users/SIEMENS/OneDrive/Desktop/python/nato/nato.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
name = input("Enter your name: ")
var = True
while var:
    try:
        list = [dict[letter] for letter in name.upper()]
    except KeyError:
        print("Sorry only letters from the alphabet please!")
        name = input("Enter your name: ")
    else:
        for i in list:
            print (i)
        var = False
