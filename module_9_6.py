import itertools
def all_variants(text):
    for size in range(len(text)):
        for i_elem in range(len(text)-size):
            yield text[i_elem:i_elem+size+1]

a = all_variants("abc")
for i in a:
    print(i)