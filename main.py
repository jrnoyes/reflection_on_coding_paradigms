#implement funtion that will flatten and sort array of integers in ascending order
def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
  return sorted(arr)

#How does this solution ensure data immutability?
    #because the variables are intigers which are immutable 

#Is this solution a pure function? Why or why not?

    #Yes because it's only updating data within itself and not impacting data outside the function 

#Is this solution a higher order function? Why or why not?

    #No because it is not aqccepting another function as an arguement 

#Would it have been easier to solve this problem using a different programming style?
    #No

#Why in particular is functional programming a helpful paradigm when solving this problem?
    #functional programming's main focus is "what to solve" and in this case we are looking to flatten and sort an array of integers 

#Object Oriented Prompt

#Podracer class defined with max+speed, condition, and price attributes
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

#define a repair() method that will update the condition to "repaired"
    def repair(self):
        self.condition = "repaired"

#define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max speed by 2
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):

    def boost(self):
        self.max_speed *= 2
    
    #define another class that inherits Podracer and call it SebulbasPod
    #class should have a special method called flame_jet that will update the condition of another podracer to "thrashed"

class SebulasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):

    def flame_jet(self, other):
        other.condition = "trashed"

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

#Encapsulation - I do not believe the solution has private variables so it does not use this pillar of OOP

#Abstraction - this solution only shows necessary information to get the result

#Inheritance - our solution does use inheritance because we have defined 2 classes that inherits all the methods and properties from the original base class

#Polymorphism - We did not use this pillar as we linked the classes together throughout the activity. If all classes wouldn't inherit "podracer" we would use this pillar. 


#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    #no - object oriented programing is a very efficient method to get the solution as we can reuse the objects within the calss over and over while also not impacting other code

#How in particular did Object Oriented Programming assist in the solving of this problem?
    # we were able to use the same attributres over and over while also utilizing different methods to get different results