input_string = input("Podaj lancuch znakow: ")

char_list = []
char_list[:0] = input_string

a_count = 0
non_f_even_index_count = 0
for c in char_list:
    i = char_list.index(c)
    if c in {'m', 'k'}:
        print("Lancuch nie powinien zawierac m lub k")
        break
    if c == 'a':
        a_count = a_count + 1
    if c != 'f' and (i % 2 == 0):
        non_f_even_index_count = non_f_even_index_count + 1
    if c == 'o':
        char_list[i] = 'x'
    if c not in {'m', 'a'}:
        char_list[i] = 'w'

print("a count = " + str(a_count))
print("even index not f = " + str(non_f_even_index_count))
for c in char_list:
    print(c, end="")
