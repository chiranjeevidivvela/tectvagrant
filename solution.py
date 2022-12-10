input_array=[[3,3,3,3,3,5,6],[2.5, 2.5 ,2.5, 2.5, 2.5, 4, 4],[4,4,4,4,4,4,10],[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],[2, 2, 2, 2, 2, 4 ,4
]]
#first we will be storing the cost of news paper of everday of the week in a 2d array
weeklyCost={} 
#Here we are creating dictionary to store the sum of all the cost of particular newspaper
weeklyCost["TOI"]=sum(input_array[0])
weeklyCost["Hindu"]=sum(input_array[1])
weeklyCost["ET"]=sum(input_array[2])
weeklyCost["BM"]=sum(input_array[3])
weeklyCost["HT"]=sum(input_array[4])
print("Enter allocated weekly budget by the user for newspaper subscription:")
weeklySubscriptionBudget=int(input())
newspaperList=["TOI","Hindu","ET","BM","HT"]
print("All possible combinations of the newspaper subscriptions for the user budget are :")
solution=[]
for i in range(len(newspaperList)):
    for j in range(i+1,len(newspaperList)):
        if weeklyCost[newspaperList[i]]+weeklyCost[newspaperList[j]]<weeklySubscriptionBudget:
#All possible combinations of the newspaper subscriptions for the user budget will be filtered here
            tmp=[]
            tmp.append(newspaperList[i])
            tmp.append(newspaperList[j])
            solution.append(tmp)
print(solution)
#All possible combinations of the newspaper subscriptions for the user budget will be printed
