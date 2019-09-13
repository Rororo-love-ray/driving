country = input ('whats your nation: ')
age = input ('whats your age: ')
age = int (age)
if country == 'Taiwan':
	if age >= 18:
		print ('you may drive')
	else:
		print ('you cannot drive')
elif country == 'USA':
	if age >= 16:
		print ('you may drive')
	else:
		print ('you cannot drive')
else:
	print ('you are not from Taiwan or USA')