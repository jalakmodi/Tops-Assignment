# dic={}
# for i in range (1,6):
#     fn=input("Enter Your Name : ")
#     Ag=int(input("Enter Your Agg : "))
#     dic[fn] = Ag
# print(dic)
# def election():
#     pass

# dict={'jalak': 35, 'sunny': 28, 'dipa': 38, 'nilita': 29, 'janvi': 5}
# dic={}


dict = {}
dic={}
while True:

    fn=input("Enter Your Name : ")
    if fn=="exit":
        break
    ag=int(input("Enter Your Agg : "))
    #dict[fn] = ag
    if ag>18:
        dict[fn]=ag
    else:
        dic[fn]=ag
    print(dict)
    print(dic)