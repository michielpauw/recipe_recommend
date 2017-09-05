def del_characters(str1):
    delims = ["&", "#", '&', '\n', '\t']
    for delim in delims:
        print(delim)
        for i in range(1):
            try:
                s = str1.index(delim)
                print(s)
                str1 = str1[0:s] + str1[s+1:]
            except ValueError:
                pass
    return str1


new_string = "h&e man,# hoe\n is &het met jou?"

print(del_characters(new_string))
