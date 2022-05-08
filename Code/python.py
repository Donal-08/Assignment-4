import pandas as pd
from numpy import random as RN
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

# Load Excel file
Data = pd.read_excel(r"C:\Users\user\Downloads\table.xlsx")
data = np.array(Data)

#Sample size
N = 9

#Theorotical probability
frequency = np.array(data[0])
Pr_red = frequency[1]/N
Pr_yellow = frequency[2]/N
Pr_blue = frequency[3]/N
Pr_not_blue = 1 - frequency[3]/N
Pr_red_or_blue = (frequency[1] + frequency[3])/N

#Generating Samples
x = RN.randint(0, high = 3, size=N)

#Finding the number of red,yellow,blue,not blue,red or blue
c_red = np.count_nonzero(x==0)
c_yellow = np.count_nonzero(x==1)
c_blue = np.count_nonzero(x==2)
c_not_blue = np.count_nonzero(x!=2)
c_red_or_blue = c_red + c_blue

#compute probabilities
pr_red = 1.0*c_red/N
pr_yellow = 1.0*c_yellow/N
pr_blue = 1.0*c_blue/N
pr_not_blue = 1.0*c_not_blue/N
pr_red_or_blue = pr_red + pr_blue

#theoretical probabilities
print('Theoritical probability')
print("Probability of getting red: ",Pr_red)
print("Probability of getting yellow: ",Pr_yellow)
print("Probability of getting blue: ",Pr_blue)
print("Probability of getting not blue: ",Pr_not_blue)
print("Probability of getting red or : ",Pr_red_or_blue)

#expermental probabilities
print("Expermental probability")
print("Probability of getting red: ",pr_red)
print("Probability of getting yellow: ",pr_yellow)
print("Probability of getting blue: ",pr_blue)
print("Probability of getting not blue: ",pr_not_blue)
print("Probability of getting red or blue: ",pr_red_or_blue)

#plotting pmf from the given data
X = np.array([4,3,2,1,0])
Y = np.array([Pr_red_or_blue,Pr_not_blue,Pr_blue,Pr_yellow,Pr_red])
fig1 = stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.grid('minor')
plt.show()












