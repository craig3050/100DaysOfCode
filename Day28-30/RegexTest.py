import re

hundred = 'Awesome, I am doing the 100 days of code'
two_hundred = 'Awesome, I am doing the 200 days of code'

m = re.search(f'.*(#\d+DaysOfCode).*', hundred)
m.groups()[0]