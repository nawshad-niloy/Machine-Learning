import pandas as pd

# df = pd.read_csv('industry.csv')
# print(df.to_string())

mydataset = {
    'cars' : ["BMW","Volvo","Ford"],
    'Ratings' : [7,5,6]
}

myvar = pd.DataFrame(mydataset) #creating a dataframe
print(myvar)

print(pd.__version__) #checking version

a = [1,"Niloy",2] #series
mybar = pd.Series(a)
print(mybar)

                    #labels

#cearting own index
mybar.index = ["x","y","z"]
print(mybar["y"])
print("\n")

#creating a series from dictionary
calories = {
    'day1' : 320, 'day2' : 400, 'day3' : 350
}
myseries = pd.Series(calories)
print(myseries)
print("\n")

