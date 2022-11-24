def siema(**kwargs):
    if 'end' in kwargs.keys():
        pom=kwargs['end']
    else:
        pom='\n'
    for k in kwargs:
        print(k, kwargs[k],end=pom)
siema(one=1,two=2,end=" _ ")
