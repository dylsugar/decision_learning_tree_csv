Instructions:

Language: Python3

1. type python3 decisiontree.py "csv file" or python3 decisiontree.py restaurant.csv
2. This should automatically output the tree and information gain/ attributes


Output:
Information Gain: [0.0, 0.0, 0.02, 0.2, 0.54, 0.2, 0.0, 0.02, 0.0, 0.21]
Highest Information Gain: Pat with 0.54
---------------------------------------------
Information Gain: [0.11, 0.0, 0.11, 0.25, 0.25, 0.11, 0.25, 0.25, 0.25]
Highest Information Gain: Hun with 0.25
---------------------------------------------
Information Gain: [0.0, 0.0, 0.31, 0.31, 0.0, 0.31, 0.5, 0.0]
Highest Information Gain: Type with 0.5
---------------------------------------------
Information Gain: [-0.08, -0.08, 0.92, -0.08, -0.08, -0.08, 0.92]
Highest Information Gain: Fri with 0.92
---------------------------------------------
The Tree:


------Node---->   Patrons
Pat Some      Pat None      Pat Full

Yes               No               No

------Node---->   Hungry
Hun Yes      Hun No

Yes               No

------Node---->   Type
Type Thai      Type French      Type Burger      Type Italian

Yes               Yes               Yes               No

------Node---->   Fri/Sat
Fri Yes      Fri No

Yes               No
