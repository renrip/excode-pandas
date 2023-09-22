import numpy as np
import pandas as pd

#ex-01
"""
Write a Pandas program to create a dataframe from a dictionary and display it.
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
"""
print("\n---ex-01---")
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

#ex-02
"""
Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
Sample Python dictionary data and list labels: (in the code)
"""
print("\n---ex-02---")
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

# #ex-03
# print("\n---ex-03---")
#
# #ex-04
# print("\n---ex-04---")
#
# #ex-05
# print("\n---ex-05---")
#
# #ex-06
# print("\n---ex-06---")
#
# #ex-07
# print("\n---ex-07---")
#
# #ex-08
# print("\n---ex-08---")
#
# #ex-09
# print("\n---ex-09---")
#
# #ex-10
# print("\n---ex-10---")
#
# #ex-11
# print("\n---ex-11---")
#
# #ex-12
# print("\n---ex-12---")
#
# #ex-13
# print("\n---ex-13---")
#
# #ex-14
# print("\n---ex-14---")
#
# #ex-15
# print("\n---ex-15---")
#
# #ex-16
# print("\n---ex-16---")
#
# #ex-17
# print("\n---ex-17---")
#
# #ex-18
# print("\n---ex-18---")
#
# #ex-19
# print("\n---ex-19---")
#
# #ex-20
# print("\n---ex-20---")
#
# #ex-21
# print("\n---ex-21---")
#
# #ex-22
# print("\n---ex-22---")
#
# #ex-23
# print("\n---ex-23---")
#
# #ex-24
# print("\n---ex-24---")
#
# #ex-25
# print("\n---ex-25---")
#
# #ex-26
# print("\n---ex-26---")
#
# #ex-27
# print("\n---ex-27---")
#
# #ex-28
# print("\n---ex-28---")
#
# #ex-29
# print("\n---ex-29---")
#
# #ex-30
# print("\n---ex-30---")
#
# #ex-31
# print("\n---ex-31---")
#
# #ex-32
# print("\n---ex-32---")
#
# #ex-33
# print("\n---ex-33---")
#
# #ex-34
# print("\n---ex-34---")
#
# #ex-35
# print("\n---ex-35---")
#
# #ex-36
# print("\n---ex-36---")
#
# #ex-37
# print("\n---ex-37---")
#
# #ex-38
# print("\n---ex-38---")
#
# #ex-39
# print("\n---ex-39---")
#
# #ex-40
# print("\n---ex-40---")
#
# #ex-41
# print("\n---ex-41---")
#
# #ex-42
# print("\n---ex-42---")
#
# #ex-43
# print("\n---ex-43---")
#
# #ex-44
# print("\n---ex-44---")
#
# #ex-45
# print("\n---ex-45---")
#
# #ex-46
# print("\n---ex-46---")
#
# #ex-47
# print("\n---ex-47---")
#
# #ex-48
# print("\n---ex-48---")
#
# #ex-49
# print("\n---ex-49---")
#
# #ex-50
# print("\n---ex-50---")
#
# #ex-51
# print("\n---ex-51---")
#
# #ex-52
# print("\n---ex-52---")
#
# #ex-53
# print("\n---ex-53---")
#
# #ex-54
# print("\n---ex-54---")
#
# #ex-55
# print("\n---ex-55---")
#
# #ex-56
# print("\n---ex-56---")
#
# #ex-57
# print("\n---ex-57---")
#
# #ex-58
# print("\n---ex-58---")
#
# #ex-59
# print("\n---ex-59---")
#
# #ex-60
# print("\n---ex-60---")
#
# #ex-61
# print("\n---ex-61---")
#
# #ex-62
# print("\n---ex-62---")
#
# #ex-63
# print("\n---ex-63---")
#
# #ex-64
# print("\n---ex-64---")
#
# #ex-65
# print("\n---ex-65---")
#
# #ex-66
# print("\n---ex-66---")
#
# #ex-67
# print("\n---ex-67---")
#
# #ex-68
# print("\n---ex-68---")
#
# #ex-69
# print("\n---ex-69---")
#
# #ex-70
# print("\n---ex-70---")
#
# #ex-71
# print("\n---ex-71---")
#
# #ex-72
# print("\n---ex-72---")
#
# #ex-73
# print("\n---ex-73---")
#
# #ex-74
# print("\n---ex-74---")
#
# #ex-75
# print("\n---ex-75---")
#
# #ex-76
# print("\n---ex-76---")
#
# #ex-77
# print("\n---ex-77---")
#
# #ex-78
# print("\n---ex-78---")
#
# #ex-79
# print("\n---ex-79---")
#
# #ex-80
# print("\n---ex-80---")
#
# #ex-81
# print("\n---ex-81---")

