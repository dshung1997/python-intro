import re

str = "3, 5, 7, 23    ,   24  , 32423,12"
w = list(map(lambda x: int(x), re.split(r"\s*,\s*", str)))
print(w)


list_a = [1, 2, 3, 4, 5]

# filter object <filter at 0x4e45890>
filter_obj = filter(lambda x: x % 2 == 0, list_a)

even_num = list(filter_obj)  # Converts the filer obj to a list

print(even_num)  # Output: [2, 4]
