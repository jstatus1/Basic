def count_smileys(arr):
    counter = 0
    for i in arr:
        if i[0] == ':' or i[0] == ';':
        	if len(i) == 2 and (i[1] == ')' or i[1] == 'D'):
        		counter += 1

        	if len(i) == 3 and (i[1] == '-' or i[1] == '~') and (i[2] == ')' or i[2] == 'D'):
        		counter += 1
    return counter

print(count_smileys([':!)']))
    
    