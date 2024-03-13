Name = input('Enter name:')
Name_length = len(Name)
if Name_length < 3:
    print('Name must be at least 3 characters.')
elif Name_length > 50:
    print('Name can only be a maximum of 50 characters')
else:
    print("Name looks good!")