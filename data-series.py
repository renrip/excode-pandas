import numpy as np
import pandas as pd

# taken from https://www.w3resource.com/python-exercises/pandas/index-data-series.php

#ex-1 Write a Pandas program to create and display a one-dimensional array-like object
# containing an array of data using Pandas module.
print("\n---ex-1---")
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

#ex-2 Write a Pandas program to convert a Panda module Series to Python list and it’s type.
print("\n---ex-2---")
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

#ex-3 Write a Pandas program to add, subtract, multiple and divide two Pandas Series
print("\n---ex-3---")
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print("Add two Series:")
ds = ds1 + ds2
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)

#ex-4 Write a Pandas program to compare the elements of the two Pandas Series.
print("\n---ex-4---")
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)

#ex-5 Write a Pandas program to convert a dictionary to a Pandas series
print("\n---ex-5---")
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)

#ex-6 Write a Pandas program to convert a NumPy array to a Pandas series.
print("\n---ex-6---")
np_array = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)

#ex-7 Write a Pandas program to change the data type of given a column or a Series.
print("\n---ex-7---")
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

#ex-8 Write a Pandas program to convert the first column of a DataFrame as a Series
print("\n---ex-8--- FIXED")
#.ix is depricated. Look into implementing using .iloc and .loc
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
#s1 = df.ix[:,0] #Original code raised exception because ix method is depricated
s1 = df.loc[:,"col1"] #Works
#s1 = df.iloc[:, 0] #Also works
print("\n1st column as a Series:")
print(s1)
print(type(s1))

#ex-9 Write a Pandas program to convert a given Series to an array
print("\n---ex-9---")
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array")
a = s1.values
print(a)
print(type(a))

#ex-10 Write a Pandas program to convert Series of lists to one Series
print("\n---ex-10---")
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
#s = s.apply(pd.Series).stack().reset_index(drop=True) #Original line give warning
# The following two lines perform the intended action
s = s.explode() #line1
s = s.reset_index(drop=True) #line2
print("One Series")
print(s)

#ex-11 Write a Pandas program to sort a given Series
print("\n---ex-11---")
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)

#ex-12 Write a Pandas program to add some data to an existing Series
print("\n---ex-12---")
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
print("\nData Series after adding some data:")
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)

#ex-13 Write a Pandas program to create a subset of a given series based on value and condition
print("\n---ex-13---")
s = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
print("Original Data Series:")
print(s)
print("\nSubset of the above Data Series:")
n = 6
new_s = s[s < n]
print(new_s)

#ex-14 Write a Pandas program to change the order of index of a given series
print("\n---ex-14---")
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)

#ex-15 Write a Pandas program to create the mean and standard deviation of the data of a given Series
print("\n---ex-15---")
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:")
print(s)
print("Mean of the said Data Series:")
print(s.mean())
print("Standard deviation of the said Data Series:")
print(s.std())

#ex-16 Write a Pandas program to get the items of a given series not present in another given series
print("\n---ex-16---")
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print("\nItems of sr1 not present in sr2:")
result = sr1[~sr1.isin(sr2)]
print(result)

#ex-17 Write a Pandas program to get the items which are not common of two given series
print("\n---ex-17---")
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print("\nItems of a given series not present in another given series:")
sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]
print(result)

#ex-18 Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series
print("\n---ex-18---")
num_state = np.random.RandomState(100) #interesting, always returns the same result given a seed
num_series = pd.Series(num_state.normal(10, 4, 20)) #this too
print("Original Series:")
print(num_series)
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])
print("\nMinimum, 25th percentile, median, 75th, and maximum of a given series:")
print(result)

#ex-19 Write a Pandas program to calculate the frequency counts of each unique value of a given series
print("\n---ex-19---")
num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print("Original Series:")
print(num_series)
print("Frequency of each unique value of the said series.")
result = num_series.value_counts()
print(result)

#ex-20 Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series
print("\n---ex-20--- FIXED")
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
#result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other' #pandas sqwaks on this
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = -999 # Uses a legal value that also stands out
print(num_series)

#ex-21 Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series
print("\n---ex-21---")
num_series = pd.Series(np.random.randint(1, 10, 9))
print("Original Series:")
print(num_series)
result = np.where(num_series % 5==0)
print("Positions of numbers that are multiples of 5:")
print(result)

#ex-22 Write a Pandas program to extract items at given positions of a given series
print("\n---ex-22---")
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
print("Original Series:")
print(num_series)
result = num_series.take(element_pos)
print("\nExtract items at given positions of the said series:")
print(result)

#ex-23 Write a Pandas program to get the positions of items of a given series in another given series
print("\n---ex-23---")
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
print("Original Series:")
print(series1)
print(series2)
result = [pd.Index(series1).get_loc(i) for i in series2]
print("Positions of items of series2 in series1:")
print(result)

#ex-24 Write a Pandas program convert the first and last character of each word to upper case in each word of a given series
print("\n---ex-24---")
series1 = pd.Series(['php', 'python', 'java', 'c#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print("\nFirst and last character of each word to upper case:")
print(result)

#ex-25 Write a Pandas program to calculate the number of characters in each word in a given series
print("\n---ex-25---")
series1 = pd.Series(['Php', 'Python', 'Java', 'C#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: len(x))
print("\nNumber of characters in each word in the said series:")
print(result)

#ex-26 Write a Pandas program to compute difference of differences between consecutive numbers of a given series
print("\n---ex-26---")
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])
print("Original Series:")
print(series1)
print("\nDifference of differences between consecutive numbers of the said series:")
print(series1.diff().tolist())
print(series1.diff().diff().tolist())

#ex-27 Write a Pandas program to convert a series of date strings to a timeseries
print("\n---ex-27--- FIXED")
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:")
print(date_series)
print("\nSeries of date strings to a timeseries:")
print(pd.to_datetime(date_series, format="mixed")) #added format="mixed" to get this code working

#ex-28 Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings
print("\n---ex-28--- FIXED")
from dateutil.parser import parse
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:")
print(date_series)
date_series = date_series.map(lambda x: parse(x))
print("Day of month:")
print(date_series.dt.day.tolist())
print("Day of year:")
print(date_series.dt.dayofyear.tolist())
print("Week number:")
# print(date_series.dt.weekofyear.tolist()) #function deprecated
print(date_series.dt.isocalendar().loc[:, "week"].tolist()) #working line
print("Day of week:")
# print(date_series.dt.weekday_name.tolist()) #function deprecated?
print(date_series.dt.day_name().tolist()) #working line

#ex-29 Write a Pandas program to convert year-month string to dates adding a specified day of the month
print("\n---ex-29---")
from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:")
print(date_series)
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)

#ex-30 Write a Pandas program to filter words from a given series that contain atleast two vowels
print("\n---ex-30---")
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print("Original Series:")
print(color_series)
print("\nFiltered words:")
result =color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(color_series[result])

#ex-31
"""
Write a Pandas program to compute the Euclidean distance between two given series.
Euclidean distance
From Wikipedia,
In mathematics, the Euclidean distance or Euclidean metric is the "ordinary" straight-line distance between two points
in Euclidean space. With this distance, Euclidean space becomes a metric space. The associated norm is called the
Euclidean norm.
"""
print("\n---ex-31---")
x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original series:")
print(x)
print(y)
print("\nEuclidean distance between two said series:")
print(np.linalg.norm(x-y))

#ex-32 Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series
print("\n---ex-32---")
nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original series:")
print(nums)
print("np.diff(nums):")
print(np.diff(nums))
print("np.sign(np.diff(nums)):")
print(np.sign(np.diff(nums)))
temp_list = np.diff(np.sign(np.diff(nums)))
print(f"temp_list:")
print(temp_list)
result_list = np.where(temp_list == -2)[0] + 1
print("\nPositions of the values surrounded by smaller values on both sides:")
print(result_list)

#ex-33 Write a Pandas program to replace missing white spaces in a given string with the least frequent character
print("\n---ex-33---")
str1 = 'abc def abcdef icd'
print("Original series:")
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)

#ex-34
"""
Write a Pandas program to compute the autocorrelations of a given numeric series.

From Wikipedia: Autocorrelation, also known as serial correlation, is the correlation of a signal with a delayed copy
of itself as a function of delay. Informally, it is the similarity between observations as a function of the time lag
between them
"""
print("\n---ex-34---")
num_series = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))
print("Original series:")
print(num_series)
autocorrelations = [num_series.autocorr(i).round(2) for i in range(11)]
print("\nAutocorrelations of the said series:")
print(autocorrelations[1:])

#ex-35 Write a Pandas program to create a TimeSeries to display all the Sundays of given year
print("\n---ex-35---")
result = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2019:")
print(result)

#ex-36 Write a Pandas program to convert given series into a dataframe with its index as another column on the dataframe
print("\n---ex-36--- ??")
char_list = list('ABCDEFGHIJKLMNOP')
num_arra = np.arange(8)
num_dict = dict(zip(char_list, num_arra))
num_ser = pd.Series(num_dict)
df = num_ser.to_frame().reset_index()
print(df.head())

#ex-37 Write a Pandas program to stack two given series vertically and horizontally
print("\n---ex-37--- COMPLETED / FIXED")
series1 = pd.Series(range(10))
series2 = pd.Series(list('pqrstuvwxy'))
print("Original Series:")
print("series1")
print(series1)
print("series2")
print(series2)
# series1.append(series2)
series1._append(series2)
# print("series2 - AGAIN")
# print(series2)
print("vertical stacking:")
vert_stack = series1._append(series2)
vert_stack = vert_stack.reset_index(drop=True)
print(vert_stack)
df = pd.concat([series1, series2], axis=1)
print("\nhorizontal stacking:")
print(df)

#ex-38 Write a Pandas program to check the equality of two given series
print("\n---ex-38---")
nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:")
print(nums1)
print(nums2)
print("Check 2 series are equal or not?")
print(nums1 == nums2)

#ex-39 Write a Pandas program to find the index of the first occurrence of the smallest and largest value of a given series
print("\n---ex-39---")
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("Original Series:")
print(nums)
print("Index of the first occurrence of the smallest and largest value of the said series:")
print(nums.idxmin())
print(nums.idxmax())

#ex-40 Write a Pandas program to check inequality over the index axis of a given dataframe and a given series
print("\n---ex-40---")
df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None])
print("Original DataFrame:")
print(df_data)
print("\nOriginal Series:")
print(sr_data)
print("\nCheck for inequality of the said series & dataframe:")
print(df_data.ne(sr_data, axis = 0))

