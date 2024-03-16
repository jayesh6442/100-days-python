import random
symbol_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
password = ""
number_alphabet = int(input("Enter number of alphabet: "))
number_number = int(input("Enter number of number: "))
number_symbol = int(input("Enter number of Symbol: "))

for _ in range(0, number_alphabet+1):
    password += random.choice(alphabet_list)

for _ in range(0, number_number+1):
    password += random.choice(number_list)

for _ in range(0, number_symbol+1):
    password += random.choice(symbol_list)


list_pass = list(password)


random.shuffle(list_pass)
print(list_pass)
final_pass = ''
for i in list_pass:
    final_pass+=i
print(final_pass)