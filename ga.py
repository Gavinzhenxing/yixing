import random
from config import *
import itertools as it
import numpy as np

# 全局变量
K = 20 # 数据流数量
gene_num = 31 # 迭代次数
cross_prob = 0.6 # 交叉概率    # 0.6~0.9
mutate_prob = 0.1 # 变异概率   # 0.001~0.01
band_size = 25 # 所有链路带宽均为250
individual_num = 60 # 种群规模
r = [0.8, 0.4, 0.6, 1.2, 0.9, 1.3, 0.7, 1.2, 0.8, 1, 1, 1, 1, 1, 1,1.5, 1.5, 1.5, 1.5, 1.5] # 计算适应度值参数：带宽
band_min = 1 # 带宽需求最小的流所在位置
w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1,0.8, 0.8, 0.8, 0.8, 0.8] # 计算适应度时参数：权重
random.seed(202)






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
        print("cross前",individual_list)
        print('cross')
        '''
        交叉
        :param individual_list: 输入种群
        :return: 交叉后的种群
        '''
        cross_genes = []
        for i in range(0, len(individual_list) - 1, 2):
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
                if judge_load(new_genes1) and judge_load(new_genes2):
                    cross_genes.append(new_genes1)
                    cross_genes.append(new_genes2)
                else:
                    cross_genes.append(genes1)
                    cross_genes.append(genes2)
            else:
                cross_genes.append(genes1)
                cross_genes.append(genes2)
        return cross_genes

    def mutate(cross_genes):
        print('mutate')
        '''
        变异
        :param cross_genes: 输入种群
        :return: 变异后的种群
        '''
        mutate_genes = []
        for individual in cross_genes:
            if random.random() < mutate_prob:
                point = find_point_not(path, judge_path=individual)
                individual[point] = random.randint(0, len(path) - 1)
                if judge_load(individual):
                    mutate_genes.append(individual)
                else:
                    mutate_genes.append(individual.copy())
            else:
                mutate_genes.append(individual.copy())
        return mutate_genes

    def select(individual_list=[], mutate_genes=[]):
        print('select')
        print("individual_list长度：%s" % len(individual_list))
        print("individual_list:%s" % individual_list)

        '''
        选择
        :param mutate_genes:
        :return:
        '''
        # 组合数组
        new_genes = []
        new_genes += individual_list
        new_genes += mutate_genes
        print("individual_list%s" % len(individual_list))
        print("mutate_genes%s：" % len(mutate_genes))
        print("new_genes:%s" % new_genes)
        print("new_genes数量：%s个" % len(new_genes))

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

        print("result_genes:%s" % result_genes)

        # 60里选best
        result_fitness = [calculate_fitness(i) for i in result_genes]  # 生成子代种群的所有适应度值
        result_fitness_array = np.array(result_fitness)
        # 排序后的所有元素的和
        result_fitness_sort = np.argsort(result_fitness_array)  # 返回从大到小的序号
        best = result_fitness_array[result_fitness_sort[-1]]
        average = np.mean(result_fitness_array)

        return result_genes, best, average

    def next_genes(individual_list):
        '''
        迭代
        :param individual_list: 输入种群
        :return:
        '''
        cross_genes = cross(individual_list)
        mutate_genes = mutate(cross_genes)
        result_genes, best, average = select(individual_list=individual_list, mutate_genes=mutate_genes)
        return result_genes, best, average


    route_delay = get_delay(path)  # 获取所有路径的时延

    # 初始化种群
    individual_list = []
    while len(individual_list) < individual_num:
        num = []
        for j in range(K):
            # 随机选择一个元素
            node = random.randint(0, len(path) - 1)
            num.append(node)
        if num not in individual_list and judge_load(num):
            # 如果该元素符合要求并且不在individual_list中，则将其添加到individual_list中
            individual_list.append(num)
    print(individual_list)


    # 迭代
    best_list = []
    average_list = []
    for i in range(gene_num):
        print("第%d次迭代"%i)
        result_genes, best, average = next_genes(individual_list=individual_list)  # 保存上一代生成的种群和best值
        best_list.append(best)
        average_list.append(average)
        individual_list = result_genes
    fitness_list = []
    fitness_list_average = []
    for i in best_list:
        fitness_list.append(i)
    for i in average_list:
        fitness_list_average.append(i)

    print("-------------")
    return fitness_list,fitness_list_average,best_list[-1]
