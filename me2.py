#24点游戏
#导入所需模块
import random
import itertools
#建立类
class Solve24:
#初始化函数
    def __init__(self, numlist=[4,12,3,5]):
    # 判断输入数值
        if type(numlist) == list and len(numlist) == 4:
            self.numlist = numlist
            print('指定计算的数字', self.numlist, '\n')
        else:
            self.numlist = [random.randint(1,13) for _ in range(4)]
            print('指定计算的数字', self.numlist, '\n')

        #产生数字
        self.nlist = []
        [self.nlist.append(n) for n in list(itertools.permutations(self.numlist)) if n not in self.nlist]
        #产生运算符号
        self.operate = ['+', '-', '*', '/']
        self.operatelist = list(itertools.product(self.operate, repeat=3))

#计算函数
    def solve(self):

        # 第一种(a+b)+(c+d)
        solvelist0 = ['(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] +'(' + str(n[2]) + m[2] +str(n[3]) + ')' for n in self.nlist for m in self.operatelist]
        # 第二种((a+b)+c)+d
        solvelist1 = ['(' + '(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) for n in self.nlist for m in self.operatelist]
        # 第三种(a+(b+c))+d
        solvelist2 = ['('  + str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + str(n[2]) + ')'+ ')'  + m[2] + str(n[3]) for n in self.nlist for m in self.operatelist]
        # 第四种a+((b+c)+d)
        solvelist3 = [str(n[0]) + m[0] + '(' + '(' + str(n[1]) + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) + ')'   for n in self.nlist for m in self.operatelist]
        # 第五种a+(b+(c+d))
        solvelist4 = [str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + '(' + str(n[2]) + m[2] + str(n[3]) + ')' + ')' for n in self.nlist for m in self.operatelist]
        #汇总所有情况
        allsolves = [solvelist0, solvelist1, solvelist2, solvelist3, solvelist4]
        count = False
        for n in allsolves:
            for m in n:
                try:
                    if eval(m) == 24:
                        count = True
                        print(m + '=24')
                except:
                    pass
        if count == False:
            print('没有符合要求的结果')

if __name__ == '__main__':
    solve24 = Solve24()
    solve24.solve()