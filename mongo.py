# coding = utf-8
__author__ = "4N"

import pymongo


class Mongo():

    def __init__(self):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.db = self.connection.N4
        self.liuyan_history = self.db.xueronghua

    def show(self):
        liuyanbang = '@4N Email: nheweijun@sina.com'
        xinliuyanbang = []
        try:
            for item in self.liuyan_history.find().sort("time", pymongo.DESCENDING).limit(20):
                xinliuyanbang.append(item["content"] + "    " + item["time"])
            xinliuyanbang.reverse()
            for x in xinliuyanbang:
                liuyanbang = liuyanbang + '\n' + str(x)
        except Exception:
            pass
        return liuyanbang

    def insert(self, xinliuyan):
        self.liuyan_history.insert(xinliuyan)

    def show_all(self):
        liuyanbang = '@4N Email: nheweijun@sina.com'
        xinliuyanbang = []
        try:
            for item in self.liuyan_history.find().sort("time", pymongo.DESCENDING):
                xinliuyanbang.append(item["content"] + "\t" + item["time"])
            xinliuyanbang.reverse()
            for x in xinliuyanbang:
                liuyanbang = liuyanbang + '\n' + str(x)
        except Exception:
            pass
        return liuyanbang
#
if __name__ == '__main__':
    M = Mongo()
    print M.show()
    # xinliuyanbang=[]
    # liuyanbang = '@4N Email: nheweijun@sina.com'
    # for item in M.liuyan_history.find().sort("time", pymongo.DESCENDING).limit(10):
    #     xinliuyanbang.append(item["content"] + "\t" + item["time"])
    #
    # ddddd = len(xinliuyanbang)
    # for i in range(len(xinliuyanbang) - 1, -1, -1):
    #     liuyanbang = liuyanbang + '\n' + str(xinliuyanbang[i])
    # # M.remove()
    # print M.show_all()