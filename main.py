from config import *

from ga import *




if __name__ == '__main__':
    # 全局变量

    G = draw_pic()  # 画初始路径图
    path = get_path(G, start=49, end=60)  # 获取路径图的所有可行路径

    fitness_list, best = ga(path)
    print(best)

    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    fig = plt.figure()
    plt.plot(fitness_list)
    plt.title(u"适应度曲线")
    path_dic = {}
    for i in range(len(path)):
        path_dic[i] = path[i]
    print(path_dic)
    plt.show()



