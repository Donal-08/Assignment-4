import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Excel file
Data = pd.read_excel(r"C:\Users\user\Downloads\table.xlsx")

# Read File
colours = Data["Color"]
freq = Data["No. of Discs"]
list = dict((x, y) for x, y in zip(colours, freq))


# Find probability
def prob(key, dict):
    return "{:.3f}".format(dict[key] / dict["Total"])


def find_prob(key, dict):
    print("Probability of Discs being", key, "is", prob(key, dict))


def find_not_prob(key, dict):
    print("Probability of Discs being not", key, "is", 1 - float(prob(key, dict)))

def find_prob_of_either_A_or_B(key1, dict1, key2, dict2):
    print("Probability of Discs being either", key1, "or", key2, "is", float(prob(key1, dict1))+float(prob(key2, dict2)))
  

# Find required probability
find_prob('Red', list)
find_prob('Yellow', list)
find_prob('Blue', list)
find_not_prob('Blue', list)
find_prob_of_either_A_or_B('Red', list, 'Blue', list)

