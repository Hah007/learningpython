# def story():
#     print('从前有座山，\n')
#     print('山上有座庙，\n')
#     print('庙里有个老和尚，\n')
#     print('一天老和尚对小和尚讲故事：\n')
#     story()
#     print('小和尚听了，找了块豆腐撞死了')
#     # 非尾递归，下一个函数结束以后此函数还有后续，所以必须保存本身的环境以供处理返回值。

# story()

# 阶乘计算
def factorial(n):
    if n == 1:
        return 1
    else:
        # 5*4! = 5*4*3! = 5*4*3*2! 
        # print(n)
        return n * factorial(n-1)  # 传递的参数是n,那么再次调用factorial(n-1)
# res = factorial(11)
# print(res)
def fac2(n=1):
    fac_value = 1
    while True:
        fac_value *= n
        yield fac_value
        n += 1

import time

def fb1(max):
    n,a,b=0,0,1
    while n<max:
        # print(b)
        a,b=b,a+b
        n=n+1
    else:
        print(a)
def fb2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

def main():

    maxnum=10000
    # res = factorial(maxnum)
    t1=time.time()
    b1=fb1(maxnum)
    t2=time.time()
    # print(res)
    print('fb1用时：%.2f' %(100000*(t2-t1))+'ms')
    
    print('*'*20)
    t3=time.time()
    b2=fb2(maxnum)
    t4=time.time()
    print(b2)
    print('fb2用时：%.2f' %(100000*(t4-t3))+'ms')
    # for i in b:
    #     print(i)
    

    




if __name__ == '__main__':
    main()
   

