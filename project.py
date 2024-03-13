footballer_list = ["Cristiano Ronaldo", "Lionel Messi", "Diego Maradona", "Franz Beckenbauer" , "Pele", "Zinedine Zidane"]

new_footballer = input("What footballer would you like to add to the list?")

def rank_footballer(new_footballer, footballer_list):

    for i in range(len(footballer_list)):

        rank = input("Do you like A)" + new_footballer + " more or B)" + footballer_list[i] + " more? A/B")

        if rank == "A":
            footballer_list.insert(i, new_footballer)
            return footballer_list

        elif rank =="B":
           continue

    footballer_list.append(new_footballer)
    return footballer_list

print("Your new ranking of footballers is", rank_footballer(new_footballer, footballer_list))

list = [1,2,3,4]
list = list[0:1]
