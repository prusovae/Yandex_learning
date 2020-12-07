source_str = 'AABBCCCAC'
print(source_str)
uniq_el = ''
result_str = ''

for letter in source_str:
    if letter not in uniq_el:
        uniq_el += letter
print(uniq_el)
for uniq_letter in uniq_el:
    k=0
    for letter in source_str:
        k += 1 if letter == uniq_letter else 0
    result_str+=uniq_letter+str(k)
print(result_str)

