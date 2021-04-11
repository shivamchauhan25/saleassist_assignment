#Using inbuilt function
def len_string(str):
    return len(str)


#Manual
def len_string_manual(str):
    count=0
    for i in str:
        count+=1
    return count

def string_gen(n,char):
    return n*char
