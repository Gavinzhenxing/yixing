import matplotlib.pyplot as plt

from config import *

from ga import *




if __name__ == '__main__':
    # 全局变量

    G = draw_pic()  # 画初始路径图
    path = get_path(G, start=42, end=49)  # 获取路径图的所有可行路径

    fitness_list, fitness_list_average, best = ga(path)
    print("best",best)

    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    fig = plt.figure()

    # 操作数据
    # paint_list_ = []
    # for i in range(len(fitness_list)):
    #     if i <= len(fitness_list)/3:
    #         paint_list_.append(fitness_list[i]+random.uniform(-0.01, 0.01))
    #     elif i < (2*len(fitness_list))/3 and i > len(fitness_list)/3:
    #         paint_list_.append(fitness_list[i] + random.uniform(-0.005, 0.005))
    #     elif i >= (2*len(fitness_list))/3 and i < (4*len(fitness_list))/5:
    #         paint_list_.append(fitness_list[i] + random.uniform(-0.002, 0.002))
    #     else:
    #         paint_list_.append(fitness_list[i] + random.uniform(-0.0001, 0.0001))
    #
    # plt.plot(paint_list_)
    plt.plot(fitness_list, color='blue')
    plt.plot(fitness_list_average, color='red')


    plt.title(u"适应度曲线")
    path_dic = {}
    for i in range(len(path)):
        path_dic[i] = path[i]
    print("所有链路",path_dic)
    plt.show()
    print(fitness_list)
    print(fitness_list_average)



