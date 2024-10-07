# Organise a guest list into seprate groups based on age
guests = [
    ("LiLy", 56),
    ("Adam", 22),
    ("Danil", 35),
    ("Dave", 45),
    ("Grace", 24),
    ("Helen", 38)
]

young_group = []
old_group = []

for guest in guests:
    name, age = guest 
    if age < 30:
        young_group.append((name, age))  
    else:
        old_group.append((name, age)) 

print("Young group:", young_group)
print("Old group:", old_group)