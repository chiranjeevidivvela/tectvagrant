# TestVagrant Assignment

We want to build an intelligent system that can calculate the weekly subscription expenses of
essential items for a household. For the sake of this assignment, we will go with the weekly
newspaper subscription. Following table demonstrate prices of some of the prominent
newspapers on a daily basis, all prices in Indian rupees.
Please do not accept the below data from the command line/console, rather use a suitable data
structure to store below values (class/struct).
![image](https://user-images.githubusercontent.com/120237772/206831751-72f136df-855e-4f52-aa58-306fff94b3b2.png)


The input to the program should be the weekly budget/amount that the user has allocated to his
subscriptions. The output must be all possible combinations of the newspaper subscriptions for
the user budget.
![image](https://user-images.githubusercontent.com/120237772/206831764-d204a7e2-ced9-4d04-bacb-6021d4d4b241.png)


# AssignmentSolution

First we will be storing the cost of news paper of everday of the week in a 2dimentional array say "input_array"

Then,
Creating a dictionary "weeklyCost"
Here we are creating dictionary to store the sum of all the cost of particular newspaper

Now program will take the decided weekly budget as an input stored in "weeklySubscriptionBudget" as an integer

Names of the NewsPapers will be stored as a list to 
All possible combinations of the newspaper subscriptions for the user budget will be filtered by using if condition by comparing weeklySubscriptionBudget and weeklyCost 

Creating "solution" to store possible combinations
Then printing all the possible combination stored in "solution"
