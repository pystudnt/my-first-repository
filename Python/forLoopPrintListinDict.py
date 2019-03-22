neighbors = ['s1', 's2', 's3']
facts = {'neighbors': ['s1', 's2', 's3'], 'hostname': 'cisco', 'os': '7.0.2'}
for key in facts:
	if key == 'neighbors':
		print facts.get('neighbors')
