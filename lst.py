lst=list()
dct=dict()
tpl=tuple()
lst=[1,2,3,4,5]
lst.append('yrrt')
print lst.count(1)
dict1={'a':'56','b':'67','c':'78'}
tpl = (1,3,4,5,6,7)
tpl1=(34,56)
tpl=(tpl,tpl1)
tpl1=tpl
lst[1]='changed'
dict1['a']='changed'
print "ths list is",lst
print "the dictionary is:",dict1
print "the tuple is ",tpl,tpl1
print "the tuple1 is ",tpl1
