def test(text):
    wlist=text.split(' ')
    llist=list(map(len,wlist))
    return llist.index(max(llist))+1
 
z=test("random pythonnn so close be happy")
print(z)
