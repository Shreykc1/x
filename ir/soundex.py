dic = {
    0: ['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y'],
    1: ['b', 'f', 'p', 'v'],
    2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
    3: ['d', 't'],
    4: ['l'],
    5: ['n', 'm'],
    6: ['r']
}

def get_soundex(word):
    word = word.lower().replace(" ", "")
    if not word:
        return "0000"

    final = word[0]

    for i in word[1:]:
        for key, values in dic.items():
            if i in values:
                final += str(key)
                break

    print("Step 1 (Converted to numbers):", final)


    temp = final[0]
    for i in range(1, len(final)):
        if final[i] != final[i - 1]:  #
            temp += final[i]
    final = temp
    print("Step 2 (After removing consecutive duplicates):", final)


    final = final[0] + final[1:].replace('0', '')
    print("Step 3 (After removing zeros):", final)

    final = final.ljust(4, '0')[:4]

    return final


word = "hello world"
soundex_code = get_soundex(word)
print("Final Soundex code:", soundex_code)
