#new_list = filter(lambda num: num % 2 ==0,numbers)
#print(list(new_list))

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)