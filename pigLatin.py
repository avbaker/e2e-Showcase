def pig_it(text):
    output = ""
    words = text.split(" ")
    for i in range(len(words)):
        wd = words[i]
        if wd.isalnum():
            wd = wd[1:] + wd[0] +"ay"
            output = output+wd+" "
        else:
            #print(wd)
            output = output+wd+" "
    return output[:-1]