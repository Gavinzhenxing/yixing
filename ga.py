import random
from config import *
import itertools as it
import numpy as np

# 全局变量
K = 5 # 数据流数量
gene_num = 100 # 迭代次数
cross_prob = 1 # 交叉概率
mutate_prob = 1 # 变异概率
band_size = 25 # 所有链路带宽均为250
individual_num = 100 # 种群规模
r = [1, 1, 1, 1, 1] # 计算适应度值参数：带宽
band_min = 1 # 带宽需求最小的流所在位置
w = [0.6, 0.8, 1, 1, 1.2] # 计算适应度时参数：权重
random.seed(100)






def ga(path):

    def calculate_fitness(aim_route):
        '''
        # 计算适应度值函数
        :param aim_route: 需要计算的路径 1维数组
        :return:
        '''
        fitness = 0
        for i in range(K):  # len(num_sort[0])：数据流流数量，对每条流计算fitness
            fitness += r[i] * w[i] * route_delay[aim_route[i]]
            # fitness = random.random()
            # 取倒数
        fitness = 1 / fitness
        return fitness

    def judge_load(judge_path):
        # 初始化链路负载字典
        links_load = {}  # 链路负载
        for i in range(len(path)):
            for j in range(len(path[i]) - 1):
                links_load_key = int('%s' % path[i][j] + '%s' % path[i][j + 1])
                links_load[links_load_key] = 0

        # 计算judge_path链路负载
        t = 0  # 计数器，用于选择 r[]
        for i in judge_path:
            for j in range(len(path[i]) - 1):
                links_load_key = int('%s' % path[i][j] + '%s' % path[i][j + 1])
                links_load[links_load_key] += r[t]
            t += 1
        # 判断是否符合带宽
        if max(links_load.values()) > band_size:
            return False
        else:
            return True

    def find_point_not(path, judge_path):
        '''
        找到交叉点和变异点的位置(不包含首位链路)
        :param path: 路径
        :param judge_path: 需要判断的路径
        :return:
        '''
        # 找到链路负载最重的，# 将各路径转换为链路list(不含首尾)
        links_1d = []  # 1维
        links_2d = []  # 2维
        for i in judge_path:
            links = []
            for j in range(1, len(path[i]) - 2):
                links.append(int('%s' % path[i][j] + '%s' % path[i][j + 1]))
                links_1d.append(int('%s' % path[i][j] + '%s' % path[i][j + 1]))
            links_2d.append(links)
        # 找到出现次数最多的路径元素
        max_links = max(links_1d, key=links_1d.count)
        # 找到出现“负载最大的路径”的最小流量点
        include_max_list = {}
        for i in range(len(links_2d)):
            if max_links in links_2d[i]:
                include_max_list[i] = r[i]
        point = min(include_max_list, key=lambda x: include_max_list[x])
        return point

    def cross(individual_list):
        print(individual_list)
        print('cross')
        '''
        交叉
        :param individual_list: 输入种群
        :return:
        '''
        cross_genes = []
        for i in range(0, individual_num - 1, 2):
            # 交叉概率
            genes1 = individual_list[i]
            genes2 = individual_list[i + 1]
            if random.random() < cross_prob:
                genes1_fitness = calculate_fitness(genes1)
                genes2_fitness = calculate_fitness(genes2)
                if genes1_fitness == genes2_fitness:
                    cross_genes.append(genes1)
                    cross_genes.append(genes2)
                    continue
                elif genes1_fitness < genes2_fitness:
                    # 获得交叉点
                    point = find_point_not(path, judge_path=genes1)
                elif genes2_fitness < genes1_fitness:
                    # 获得交叉点
                    point = find_point_not(path, judge_path=genes2)

                new_genes1 = []
                new_genes2 = []
                for i in range(0, point):
                    new_genes1.append(genes1[i])
                    new_genes2.append(genes2[i])
                for i in range(point, K):
                    new_genes1.append(genes2[i])
                    new_genes2.append(genes1[i])
                cross_genes.append(new_genes1)
                cross_genes.append(new_genes2)
            else:
                cross_genes.append(genes1)
                cross_genes.append(genes2)
        return cross_genes

    def mutate(cross_genes):
        print('mutate')
        '''
        变异
        :param cross_genes: 输入种群
        :return:
        '''
        mutate_genes = []
        tt =[]
        for individual in cross_genes:
            if random.random() < mutate_prob:
                point = find_point_not(path, judge_path=individual)
                tt = individual
                tt[point] = random.randint(0, len(path)-1)  # len(cross_genes[0])-1) ==4; path == 7
                # individual[point] = random.randint(0, len(path)-1)  # len(cross_genes[0])-1) ==4; path == 7
                mutate_genes.append(tt)
            else:
                mutate_genes.append(individual)

        for i in range(len(cross_genes)):
            if random.random() < mutate_prob:
                point = find_point_not(path, judge_path=cross_genes[i])
                tt = []
                tt = cross_genes[i]
                tt[point] = random.randint(0, len(path)-1)  # len(cross_genes[0])-1) ==4; path == 7
                mutate_genes.append(tt)
            else:
                mutate_genes.append(cross_genes[i])






        return mutate_genes

    def select(individual_list=[], mutate_genes=[]):
        print('select')
        print("individual_list长度：%s"%len(individual_list))
        print("individual_list:%s"%individual_list)
        '''
        选择
        :param mutate_genes:
        :return:
        '''
        # 120选60
        print("mutate_genes:%s"%mutate_genes)
        # 将交叉变异后的基因进行判断，符合的才能进入迭代
        legal_genes = []
        for i in mutate_genes:
            if (i in num_sort):
                legal_genes.append(i)
            else:
                pass
        # 组合数组
        new_genes = []
        new_genes += individual_list
        print("individual_list%s"%len(individual_list))
        new_genes += legal_genes
        print("legal_genes%s："%len(legal_genes))
        print("new_genes:%s"%new_genes)
        print("new_genes数量：%s个"%len(new_genes))
        # 计算新组成的120条染色体中，每一条染色体的fitness
        all_fitness = []
        for i in new_genes:
            all_fitness.append(calculate_fitness(i))

        # 方法1：排序并选择最大的60个适应度值
        all_fitness_array = np.array(all_fitness)
        all_fitness_sort_order = np.argsort(-all_fitness_array)
        result_genes = []
        for i in range(individual_num):
            result_genes.append(new_genes[all_fitness_sort_order[i]])
        # result_genes = [new_genes[i] for i in all_fitness_sort_order]

        # # 方法2：根据概率公式无放回抽取
        # max_fitness = max(all_fitness)
        # min_fitness = min(all_fitness)
        # # 计算概率,生成概率数组
        # new_genes_prob = []
        # for i in new_genes:
        #     individual_prob = (calculate_fitness(i) - min_fitness) / (max_fitness - min_fitness)
        #     new_genes_prob.append(individual_prob)
        #
        # # 将概率归一化,所有概率和为1
        # new_genes_prob_normal = [i / sum(new_genes_prob) for i in new_genes_prob]
        #
        # # 根据概率无放回的 选择下一代
        # print(new_genes_prob_normal)
        # result_genes_order = np.random.choice([i for i in range(len(new_genes))], size=individual_num, replace=False, p=new_genes_prob_normal)
        # result_genes = [new_genes[i] for i in result_genes_order]  # 下一代实际基因
        print("result_genes:%s"%result_genes)


        # 60里选best
        result_fitness = [calculate_fitness(i) for i in result_genes]  # 生成子代种群的所有适应度值
        result_fitness_array = np.array(result_fitness)
        # 排序后的所有元素的和
        result_fitness_sort = np.argsort(-result_fitness_array)  # 返回从大到小的序号
        best = result_genes[result_fitness_sort[0]]
        # for i in range(len(result_genes)):
        #     temp_best_order = result_fitness_sort[i]  # 临时最佳元素序号
        #     best = result_genes[temp_best_order]
        #     # # 判断这个最佳是否在所有可能情况之内
        #     # if temp_best in num_sort:
        #     #     best = temp_best
        #     #     break
        #     # if i == len(result_genes) - 1:
        #     #     print("本次生成的子代中没有符合条件的best")
        return result_genes, best

    def next_genes(individual_list):
        '''
        迭代
        :param individual_list: 输入种群
        :return:
        '''
        cross_genes = cross(individual_list)
        mutate_genes = mutate(cross_genes)
        result_genes, best = select(individual_list=individual_list, mutate_genes=mutate_genes)
        return result_genes, best


    route_delay = get_delay(path)  # 获取所有路径的时延
    # 排列组合 生成所有可能情况
    num_sort = []
    for i in it.product([i for i in range(len(path))], repeat=K):
        num_sort.append(list(i))  # 5条路 4种选择，排列下来1024种组合
    # 根据带宽限制，剔除不符合要求的分配方式
    all_sort = []
    for i in num_sort:
        if judge_load(i):
            all_sort.append(i)
        else:
            pass
    num_sort = all_sort

    # 初始化种群
    individual_order = random.sample(range(len(num_sort)), individual_num)  # 生成individual_num=60个初始种群序号的list
    # individual_list = [num_sort[i] for i in individual_order]  # 取出对应list的路径值
    individual_list = []
    for i in individual_order:
        individual_list.append(num_sort[i])
    best = individual_list[0]  # 初始best值,每迭代一次保存一个best值，访问best[-1]永远是最新的best

    print(individual_list)

    # 迭代
    best_list = []
    for i in range(gene_num):
        print("第%d次迭代"%i)
        result_genes, best = next_genes(individual_list=individual_list)  # 保存上一代生成的种群和best值
        best_list.append(best)
        individual_list = result_genes
    fitness_list = []
    for i in best_list:
        fitness_list.append(calculate_fitness(i))

    print("-------------")
    print(len(num_sort))
    return fitness_list,best_list[-1]
    # 解决中文显示问题




    #