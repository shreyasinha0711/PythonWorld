# sets don't hold order and don't contain duplicate elements
art_friends = {"Roy", "Jeff", "Jen"}
science_friends = {"Jen", "Charly"}

art_not_science = art_friends.difference(science_friends)
science_not_art = science_friends.difference(art_friends)
print(art_not_science)
print(science_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

inter_section = art_friends.intersection(science_friends)
union_section = art_friends.union(science_friends)
print(inter_section)
print(union_section)

art_friends.add("Rof")
print(art_friends)
print(science_friends)
art_friends.add("Rof")
print(art_friends)
