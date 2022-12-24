#made by Divyansh Mohan Rao and Janhvi Guha 
#cities[str]: entered by user comma separated
#distance[int]:integer distance from city 0 to city 1....city N
#c: capacity of the electric car to travel in full tank
def electricCar(cities: list[str],distance: list[int],c: int) -> list[str]:
    #Initializing and additng the starting city in the output Traversed array
    traversed = [cities[0]]
    c = int(c)
    #if the distance from city 0 to city 1 is less than capacity
    if len(distance) >0 and c < distance[0]:
        return 'Fuel capacity low, cant complete journey'
    #Available capacity after subtracting the distance of city 0
    availCap = c - distance[0]
    j = 1
    #while we have not traversed all the cities Do
    while j < len(cities)-1:
        # calculate if we can travel to next city and come back if pump is broken
        if distance[j] * 2 <= availCap:
            #decrease capacity and increase pointer to next city
            availCap -= distance[j]
            j+=1
        else:
            #if we dont have capacity to go to next city and come back then refill on current city
            traversed.append(cities[j])
            #restore capacity
            availCap = c
            #if after refilling also the capacity is not enough to reach next city then return error msg
            if j != len(distance)-1 and availCap < distance[j+1] * 2:
                return "Cant travel to next city after city:" +cities[j]
    #add the last city to traversed list 
    traversed.append(cities[-1])
    #return result
    return traversed

cap = input('please enter capicity of car: ')
cityList = input("please Enter cities (Comma Separated): ")
cityList = cityList.split(",")
distanceList = []
for i in range(1,len(cityList)):
    distanceList.append(int(input("please enter distance from city " +cityList[i-1]+ " to city "+ cityList[i] + ": ")))

print("The miniumum number of stops to reach the destination is : " ,electricCar(cityList,distanceList,cap))