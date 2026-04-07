keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']

# dictionary using zip and the dict constructor
user_dict = dict(zip(keys, values))
print(user_dict)