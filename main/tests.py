from django.test import TestCase



class User():
	my_field = 'dd'

u = User()
u.my_field = "hello"

print(u.my_field)