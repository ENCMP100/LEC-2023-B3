## Lists, Tuples, Sets, and Dictionaries
#
# Sets and Dictionaries: See Lecture 19 code files
#

## Creating empty instances
emptyList = []
emptySet = set()
emptyDict1 = dict()
emptyDict2 = {}

## Creating instances with values
list1 = [1,2,3,2,5]
list2 = ["Apple", "Orange", "Banana", "Orange"]

set1 = set([1,2,3,2,5]) # duplicate values are ignored
set2 = set(["Apple", "Orange", "Banana", "Orange"])

dict_contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }
dict_citizenships = { "Fred": "Canadian", "Mary": "American" }

person = {"Name": "Sarah", "Age": 25, "Phone": "232323"}
tuple1 = (3,5,7)

## Adding values
list1.append(100)
list2.append("Pineapple")
list2.append("Pineapple")
list2.append("Pineapple")


set1.add(100)
set1.add(100) #Adding existing value has no effect. 

set2.add("Pineapple")
set2.add("Pineapple")
set2.add("Pineapple")

dict_contacts["Rose"] = 3434


