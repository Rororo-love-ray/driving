country = input ('whats your nation: ')
age = input ('whats your age: ')
age = int (age)
if country == 'Taiwan':
	if age >= 18:
		print ('you may drive')
	else:
		print ('you cannot drive')
if country == 'USA':
	if age >= 20:
		print ('you may drive')
	else:
		print ('you cannot drive')