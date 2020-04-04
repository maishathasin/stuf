
s='insert 0 5 insert 1 10 insert 0 6 print remove 6 append 9 append 1 sort print pop reverse print'
y=(s.split())



i=[]
def commands(str_):
    if str_==[]:
        return[]
    elif str_[0]=='insert':
        i.insert(int (str_[1]), (int (str_[2]))) 
        return i + commands(str_[3:])
    elif str_[0]=='print':
        print(i)
        return i + commands(str_[1:])
    elif str_[0]=='append':
        i.append(int(str_[1]))
        return i + commands(str_[2:])
    elif str_[0]=='remove':
         i.remove(int(str_[1]))
         return i + commands(str_[2:])
    elif str_[0]=='sort':
         i.sort()
         return i + commands(str_[1:])
    elif str_[0]=='pop':
         i.pop() 
         return i + commands(str_[1:])
    elif str_[0]=='reverse':
        i.reverse()
        return i + commands(str_[1:])

print(commands (y))

        
        

