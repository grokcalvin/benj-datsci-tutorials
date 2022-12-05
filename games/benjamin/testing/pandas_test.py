import pandas as pd
import random

#how to generate a data frame
  
# Create the pandas DataFrame with column name is provided explicitly




#create device that detect the presense of a file and if no file then create a new df

data = [{"Weapon_ID": 0, "Component_ID": 0, "Parent_ID": None,"Child_ID":842082,"multiplier":3},
        {"Weapon_ID": 0, "Component_ID": 0, "Parent_ID": None,"Child_ID":842083,"multiplier":2},
        {"Weapon_ID": 1, "Component_ID": 0, "Parent_ID": None,"Child_ID":842084,"multiplier":5},]

#stats should increase linearly 

#df = pd.DataFrame.from_dict(data)
df = pd.read_csv("/var/home/banjoyoboss/code/benj-datsci-tutorials/games/benjamin/testing/weapon_mupliers.csv")

input1 = int(input())
filtered = df[df["Weapon_ID"] == input1 ]

output = 1
for row in filtered["multiplier"]:
    output = output*row

    print(row)

input1 =""
while input1 != "end":
    Dictionary = {"Weapon_ID":int(input("Weapon_ID:")),"Component_ID":int(input("Component_ID:")),"Parent_ID":int(input("Parent_ID:")),"Child_ID":int(input("Child_ID:")),"multiplier":int(input("multiplier:"))}
#    df.loc[len(df)] = [int(input("Weapon_ID")), 0, None,random.randint(1,100000000), int(input("Multipler:"))]
    input1 = input("type \"end\" to stop adding entries:")
    df.append(Dictionary,ignore_index=True)
print(df)

#next time learn how to import with row labels and import row labels

#export df as csv

df.to_csv("/var/home/banjoyoboss/code/benj-datsci-tutorials/games/benjamin/testing/weapon_mupliers.csv")

print(filtered)

#/var/home/banjoyoboss/code/benj-datsci-tutorials/games/benjamin/testing/weapon_mupliers.csv




#how to export a data frame

#how to import a dataframe

#then add one run of enitiy number 111 boost being a random number between 1-3

#sintax
#how to add a column
#   df.column = series??
#how to add a row

#the idea is that I can create a dataframe that I can select a group from and using a for loop add up all the attibutes from every row.
#later be able to select a child observation from the stored IDs of the entries. every object has a parent ID and a Child ID and you use the child ID to select all rows that have the coorisponding Parent ID, then do a recursive function to calculate all the boosts.

#how to add rows to dataframe.
    #pd.append

#be able to append a new row easily

#select groups based on colum value

#select groups in groups using second column

#find the logic that lets you select only rows with boolbean series df[df.["column"] == Weapon_ID]