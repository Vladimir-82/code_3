ALFHABET = list('abcdefghijklmnopqrstuvwxyz')
NUMBERS = [str(i) for i in range(1, 27)]
def alphabet_position(text):
    my_dict = dict(zip(ALFHABET, NUMBERS))
    res = ''
    for i in text.lower():
        if i in my_dict.keys():
            res += my_dict[i] + " "
    return res.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))



