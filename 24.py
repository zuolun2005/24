# 24点游戏
# 2020-3-11
# 导入所需模块
import random
import itertools
from baiduapi import BaiDuAPI

class Solve24:
    '''用于计算24点游戏，并且实现自动计算'''
    # 构造函数  初始化函数
    def __init__(self, numList=[4, 12, 3, 5]):
        #列表推导式
        if type(numList) == list and len(numList) == 4:
            self.numList = numList
            print('指定计算的数字',self.numList,'\n')
        else:
            self.numList = [random.randint(1,13) for _ in range(4)]
            print('随机计算的数字',self.numList,'\n')
        #print(numList)

        self.nlist = []
        [self.nlist.append(n) for n in list(itertools.permutations(self.numList)) if n not in self.nlist]

        # 运算符
        # [4] [4] [4] 4*4*4 == 64
        self.operate = ['+','-','*','/']
        self.operateList = list(itertools.product(self.operate, repeat=3))

    def Solve(self):
        '''计算24点游戏，拼凑4个数字和三个运算符'''

        # 第一种情况 （a+b)+(c+d)
        # 产生字符串  返回的是列表
        solveList0 = ['('+str(n[0])+m[0]+str(n[1])+')'+m[1]+'('+str(n[2])+
                      m[2]+str(n[3])+')' for n in self.nlist for m in self.operateList]
        # 第二种情况  ((a+b)+c)+d
        solveList1 = ['(' + '(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) for n in self.nlist for m in self.operateList]
        # 第三种情况  (a+(b+c))+d
        solveList2 = ['('  + str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + str(n[2]) + ')' + ')' + m[2] + str(n[3]) for n in self.nlist for m in self.operateList]
        # 第四种情况   a+((b+c)+d)
        solveList3 = [str(n[0]) + m[0] + '(' + '(' + str(n[1]) +  m[1] + str(n[2]) + ')' + m[2] + str(n[3]) + ')' for n in self.nlist for m in self.operateList]
        # 第五种情况   a+(b+(c+d))
        solveList4 = [str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + '(' + str(n[2]) + m[2] + str(n[3])  + ')' + ')' for n in self.nlist for m in self.operateList]
        # 汇总所有情况
        allSolves = [solveList0,solveList1,solveList2,solveList3,solveList4]

        # 遍历所有情况
        count = False #0
        for n in allSolves:
            for m in n:
                try:
                    if eval(m) ==24:
                        count = True
                        print(m + '=24')
                except:
                    pass
        if count == False:
            print('一首凉凉送给你')





if __name__ == '__main__':

    baiduapi = BaiDuAPI(r'C:\Users\Administrator\PycharmProjects\24\password.ini')
    zihu = baiduapi.picture2Number(r'C:\Users\Administrator\PycharmProjects\24\1234.png')

    solve24 = Solve24(zihu)
    solve24.Solve()


