stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
print("Updated list:", stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
print("Updated list:", stops)
#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print ("The index for Linlithgow is:", index)
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print("Updated list:", stops)
#6. Delete "Cumbernauld" from the list by index
del stops[2]
print("Updated list:", stops)
#7. Print the number of stops there are in the list
number_of_stops = len(stops)
print("The number of stops is:",number_of_stops)
#8. Sort the list alphabetically
stops.sort()
print(stops)
#9. Reverse the positions of the stops in the list
stops.sort(reverse= True)
print(stops)
# 10 Print out all the stops using a for loop
for all_stops in range(len(stops)):
    print(stops[all_stops])