"""
Create a program that combines two dictionaries. 
If you locate the same keys during combining, you can sum the values of these similar keys.
 Create a new dictionary.
"""

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}

d2 = {'key1': 200, 'key2': 100, 'key4':300}


new_dict = Counter(d1) + Counter(d2)
print(new_dict)