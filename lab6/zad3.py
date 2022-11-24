def siema(*args):
    print(args)
    if len(args) == 0:
        None
    else:
        print("najwiekszy argument to: ",max(args))
        print("najmniejszy argument to: ",min(args))

siema(1,2,3,4,5)
