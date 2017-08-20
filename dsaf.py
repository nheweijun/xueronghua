# coding=utf-8
__author__ = "4N"


# mm = [[1,2],[3,4]]

#
# # m = map(lambda x:[x[1] if x[1] >2 else 1][0], mm)
#
#
# d = range(20)
# print [x+2 for x in d if x>10]


# import requests
#
# url = "http://pythonscraping.com/pages/cookies/welcome.php"
# params = {"username":"4N","password":"password"}
# r = requests.post(url=url,data= params)
# print r.cookies.get_dict()\
#
# def n(nt):
#     try:
#         for t in nt:
#             for e in n(t):
#                 yield e
#     except TypeError:
#         yield nt


m = [[1,2,[1,2]],3]

def ns(nt):
    for i in nt:
        if isinstance(i,list):
            for k in ns(i):
                yield k
        else:
            yield i


from itertools import permutations




mk = ns(m)
print list(mk)