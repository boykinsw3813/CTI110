#m3Q2 A-N.txt
#William Boykins
#June 13, 2017


temp = float (input("what is the temperature of the water sample? "))

if temp <= 32:
    state= "solid"
    
elif temp <= 212:
    state = "liquid"
  
elif temp > 212:
    state = "gas"

print("The state of matter is" ,state)


