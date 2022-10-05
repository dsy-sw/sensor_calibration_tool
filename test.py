import config.config as config

con = config.name_match
a = 'gnss'
b = a.split(' ')
if b in con:
    print(b)