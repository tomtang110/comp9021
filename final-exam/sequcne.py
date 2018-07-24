
import sys
a=input('Please input a string of lowercase letters: ')
if not all(i.islower() for i in a):
    print('incorrect input')
    sys.exit()
longest_sequence = 0
current = 0
word_len = len(a)
current_start = 0

longest_sequence = 0
current = 0
word_len = len(a)
set1=[ord(i) for i in a]
current_start = 0
for i in range(current,word_len):
	last_sequence = 0
	for k in range(word_len-i):
		if ord(a[i])+k in set1[current:]:
			last_sequence += 1
		else:
			break
	if last_sequence > longest_sequence:
		longest_sequence = last_sequence
		current_start = current
	current += 1

print('The solution is: ',end='')
print(''.join(chr(ord(a[current_start])+i) for i in range(longest_sequence)))