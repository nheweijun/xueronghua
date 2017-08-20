# coding=utf-8
__author__ = "4N"

def move(str, n):
    str1 = str[0:n]
    str2 = str[n:]
    return str2+str1

def reverse(say):
    """
    reverse a sentence
    :param say: a sentence
    :return: a reversed sentence
    """
    words = say.split(' ')
    words.reverse()
    newsay = ''
    for word in words:
        newsay += ' ' + word
    newsay.strip()
    return newsay

def determin(str1,str2):
    det = True
    for str in str1:
        if str not in str2:
            det = False
    return det


# def possible(str):

# def possible(str):
#     chars = [i for i in str]
#     colist=[]
#     def combine(chars):
#         if len(chars) == 1:
#             return chars[0]
#         else:
#             for achar in chars:
#                 chars.remove(achar)
#                 colist.append(achar + combine(chars))
#     combine(chars)
#     return colist

# print possible('abc')



def fact(instance):
    """
    扁平化列表
    :param instance:
    :return:
    """
    res = []
    def each(ins):
        if not isinstance(ins, list):
            res.append(ins)
        else:
            for item in ins:
                fact(item)
    each(instance)
    return res

def compose(str):
    """

    :return:
    """
    res = []
    words = list(str)
    astr = ''
    def do_compose(words):
        if len(words) == 1:
            self.nstr += words[0]
            res.append(nstr)
        else:
            for word in words:
                nstr +=word
                mm = words
                mm.remove(word)
                do_compose(mm,nstr)

    do_compose(words,astr)
    return res

m = compose("abc")
print m
