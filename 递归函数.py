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
        print(n)
        return n * factorial(n-1)  # 传递的参数是n,那么再次调用factorial(n-1)
res = factorial(11)
print(res)
