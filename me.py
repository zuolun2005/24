import random
import itertools

class Solve24:
    def __init__(self,numlist=[4,12,3,5]):
        if type(numlist) ==list and len(numlist) == 4:
            self.numlist = numlist
        else:
            self.numlist = [random.randint(1,13) for _ in range(4)]

        self.nlist = []
        [self.nlist.append(n) for n in list(itertools.permutations(self.numlist)) if n not in self.nlist]

        self.operate = ['+','-','*','/']
        self.operatelist = list(itertools.product(self.operate, repeat=3))

    def solve(self):

        # 第一种情况 （a+b)+(c+d)
        # 产生字符串  返回的是列表
        solvelist0 = ['(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] +'(' + str(n[2]) + m[2] +str(n[3]) + ')' for n in self.nlist for m in self.operatelist]
        # 第二种情况  ((a+b)+c)+d
        solvelist1 = ['(' + '(' + str(n[0]) + m[0] + str(n[1]) + ')' + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) for n in self.nlist for m in self.operatelist]
        # 第三种情况  (a+(b+c))+d
        solvelist2 = ['('  + str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + str(n[2]) + ')'+ ')'  + m[2] + str(n[3]) for n in self.nlist for m in self.operatelist]
        # 第四种情况   a+((b+c)+d)
        solvelist3 = [str(n[0]) + m[0] + '(' + '(' + str(n[1]) + m[1] + str(n[2]) + ')' + m[2] + str(n[3]) + ')'   for n in self.nlist for m in self.operatelist]
        # 第五种情况   a+(b+(c+d))
        solvelist4 = [str(n[0]) + m[0] + '(' + str(n[1]) + m[1] + '(' + str(n[2]) + m[2] + str(n[3]) + ')' + ')'  for n in self.nlist for m in self.operatelist]
        # 汇总所有情况
        allSolves = [solvelist0,solvelist1,solvelist2,solvelist3,solvelist4]
        # 遍历所有可能
        count = False
        for n in allSolves:
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
