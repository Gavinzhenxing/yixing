import networkx as nx
import matplotlib.pyplot as plt

def draw_pic():
    '''
    画无向图
    :return:
    '''
    # 设置位置
    pos = {1: [0, 10],
           2: [5, 10],
           3: [10, 10],
           4: [15, 10],
           5: [0, 5],
           6: [5, 5],
           7: [10, 5],
           8: [15, 5],
           9: [0, 0],
           10: [5, 0],
           11: [10, 0],
           12: [15, 0],
           }
    # 创建无向图
    G = nx.Graph()

    # 添加结点：多少边多少个结点
    nodes = []
    for i in range(12):
        nodes.append(i + 1)
    G.add_nodes_from(nodes)

    G.add_edge(37, 38, band=25, time=10)
    G.add_edge(37, 43, band=25, time=13.5)

    G.add_edge(38, 37, band=25, time=10)
    G.add_edge(38, 39, band=25, time=10)
    G.add_edge(38, 44, band=25, time=13.5)

    G.add_edge(39, 38, band=25, time=10)
    G.add_edge(39, 40, band=25, time=10)
    G.add_edge(39, 45, band=25, time=13.5)

    G.add_edge(40, 39, band=25, time=10)
    G.add_edge(40, 41, band=25, time=10)
    G.add_edge(40, 46, band=25, time=13.5)

    G.add_edge(41, 40, band=25, time=10)
    G.add_edge(41, 42, band=25, time=10)
    G.add_edge(41, 47, band=25, time=13.5)

    G.add_edge(42, 41, band=25, time=10)
    G.add_edge(42, 48, band=25, time=13.5)

    #
    G.add_edge(43, 37, band=25, time=13.5)
    G.add_edge(43, 44, band=25, time=14)
    G.add_edge(43, 49, band=25, time=13.5)

    G.add_edge(44, 38, band=25, time=13.5)
    G.add_edge(44, 43, band=25, time=14)
    G.add_edge(44, 45, band=25, time=14)
    G.add_edge(44, 50, band=25, time=13.5)

    G.add_edge(45, 39, band=25, time=13.5)
    G.add_edge(45, 44, band=25, time=14)
    G.add_edge(45, 46, band=25, time=14)
    G.add_edge(45, 51, band=25, time=13.5)

    G.add_edge(46, 40, band=25, time=13.5)
    G.add_edge(46, 45, band=25, time=14)
    G.add_edge(46, 47, band=25, time=14)
    G.add_edge(46, 52, band=25, time=13.5)

    G.add_edge(47, 41, band=25, time=13.5)
    G.add_edge(47, 46, band=25, time=14)
    G.add_edge(47, 48, band=25, time=14)
    G.add_edge(47, 53, band=25, time=13.5)

    G.add_edge(48, 42, band=25, time=13.5)
    G.add_edge(48, 47, band=25, time=14)
    G.add_edge(48, 54, band=25, time=13.5)

    #
    G.add_edge(49, 43, band=25, time=13.5)
    G.add_edge(49, 50, band=25, time=14)

    G.add_edge(50, 44, band=25, time=13.5)
    G.add_edge(50, 49, band=25, time=14)
    G.add_edge(50, 51, band=25, time=14)

    G.add_edge(51, 45, band=25, time=13.5)
    G.add_edge(51, 50, band=25, time=14)
    G.add_edge(51, 52, band=25, time=14)

    G.add_edge(52, 46, band=25, time=13.5)
    G.add_edge(52, 51, band=25, time=14)
    G.add_edge(52, 53, band=25, time=14)

    G.add_edge(53, 47, band=25, time=13.5)
    G.add_edge(53, 52, band=25, time=14)
    G.add_edge(53, 54, band=25, time=14)

    G.add_edge(54, 48, band=25, time=13.5)
    G.add_edge(54, 53, band=25, time=14)

    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimSun']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title("初始路径图")

    nx.draw(G, with_labels=True, node_color='y', pos=pos)
    # 格式化输出时延 t=xx
    edgeTime = nx.get_edge_attributes(G, 'time')
    edgeLabel = {}  # 边的标签
    for i in edgeTime.keys():  # 整理边的标签，用于绘图显示
        edgeLabel[i] = f't={edgeTime[i]:}'  # 边的容量
    nx.draw_networkx_edge_labels(G, pos, edgeLabel, font_color='navy')

    # 格式化输出带宽 b=xx
    edgeBand = nx.get_edge_attributes(G, 'band')
    for i in edgeBand.keys():  # 整理边的标签，用于绘图显示
        edgeLabel[i] += ',b=' + str(edgeBand[i])

    nx.draw_networkx_edge_labels(G, pos, edgeLabel, font_color='navy')
    plt.show()

    return G

# def draw_final_pic():
#     import networkx as nx
#     import matplotlib.pyplot as plt
#     # 设置位置
#     pos = {1: [0, 10],
#            2: [5, 10],
#            3: [10, 10],
#            4: [15, 10],
#            5: [0, 5],
#            6: [5, 5],
#            7: [10, 5],
#            8: [15, 5],
#            9: [0, 0],
#            10: [5, 0],
#            11: [10, 0],
#            12: [15, 0],
#            }
#     # 创建无向图
#     G = nx.Graph()
#
#     # 添加结点：多少边多少个结点
#     nodes = []
#     color_list = []
#     for i in range(12):
#         nodes.append(i + 1)
#         color_list.append('y')
#     G.add_nodes_from(nodes)
#
#     G.add_edge(1, 2, band=250, time=40)  # 添加边的属性 "band=250,  time"
#     G.add_edge(1, 5, band=250, time=50)
#
#     G.add_edge(2, 1, band=250, time=40)
#     G.add_edge(2, 3, band=250, time=40)
#     G.add_edge(2, 6, band=250, time=50)
#
#     G.add_edge(3, 2, band=250, time=40)
#     G.add_edge(3, 4, band=250, time=40)
#     G.add_edge(3, 7, band=250, time=50)
#
#     G.add_edge(4, 3, band=250, time=40)
#     G.add_edge(4, 8, band=250, time=50)
#
#     G.add_edge(5, 1, band=250, time=50)
#     G.add_edge(5, 6, band=250, time=30)
#     G.add_edge(5, 9, band=250, time=50)
#
#     G.add_edge(6, 2, band=250, time=50)
#     G.add_edge(6, 5, band=250, time=30)
#     G.add_edge(6, 7, band=250, time=30)
#     G.add_edge(6, 10, band=250, time=50)
#
#     G.add_edge(7, 3, band=250, time=50)
#     G.add_edge(7, 6, band=250, time=30)
#     G.add_edge(7, 8, band=250, time=30)
#     G.add_edge(7, 11, band=250, time=50)
#
#     G.add_edge(8, 4, band=250, time=50)
#     G.add_edge(8, 7, band=250, time=30)
#     G.add_edge(8, 12, band=250, time=50)
#
#     G.add_edge(9, 5, band=250, time=50)
#     G.add_edge(9, 10, band=250, time=30)
#
#     G.add_edge(10, 6, band=250, time=50)
#     G.add_edge(10, 9, band=250, time=30)
#     G.add_edge(10, 11, band=250, time=30)
#
#     G.add_edge(11, 7, band=250, time=50)
#     G.add_edge(11, 10, band=250, time=30)
#     G.add_edge(11, 12, band=250, time=30)
#
#     G.add_edge(12, 8, band=250, time=50)
#     G.add_edge(12, 11, band=250, time=30)
#
#     for i in pp:
#         color_list[i - 1] = 'r'
#     nx.draw(G, with_labels=True, node_color=color_list, pos=pos)
#     G.add_edge(12, 8, band=250, time=50)
#
#     plt.show()

def draw_pic():
    import networkx as nx
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 14))
    # 设置位置
    pos = {1: [0, 0],
           2: [5, 0],
           3: [10, 0],
           4: [15, 0],
           5: [20, 0],
           6: [25, 0],

           7: [0, 5],
           8: [5, 5],
           9: [10, 5],
           10: [15, 5],
           11: [20, 5],
           12: [25, 5],

           13: [0, 10],
           14: [5, 10],
           15: [10, 10],
           16: [15, 10],
           17: [20, 10],
           18: [25, 10],

           19: [0, 15],
           20: [5, 15],
           21: [10, 15],
           22: [15, 15],
           23: [20, 15],
           24: [25, 15],

           25: [0, 20],
           26: [5, 20],
           27: [10, 20],
           28: [15, 20],
           29: [20, 20],
           30: [25, 20],

           31: [0, 25],
           32: [5, 25],
           33: [10, 25],
           34: [15, 25],
           35: [20, 25],
           36: [25, 25],

           37: [0, 30],
           38: [5, 30],
           39: [10, 30],
           40: [15, 30],
           41: [20, 30],
           42: [25, 30],

           43: [0, 35],
           44: [5, 35],
           45: [10, 35],
           46: [15, 35],
           47: [20, 35],
           48: [25, 35],

           49: [0, 40],
           50: [5, 40],
           51: [10, 40],
           52: [15, 40],
           53: [20, 40],
           54: [25, 40],

           55: [0, 45],
           56: [5, 45],
           57: [10, 45],
           58: [15, 45],
           59: [20, 45],
           60: [25, 45],

           61: [0, 50],
           62: [5, 50],
           63: [10, 50],
           64: [15, 50],
           65: [20, 50],
           66: [25, 50],
           }
    # 创建无向图
    G = nx.Graph()

    # 添加结点：多少边多少个结点
    nodes = []
    for i in range(66):
        nodes.append(i + 1)
    G.add_nodes_from(nodes)

    #

    G.add_edge(37, 38, band=25, time=10)
    G.add_edge(37, 43, band=25, time=13.5)

    G.add_edge(38, 37, band=25, time=10)
    G.add_edge(38, 39, band=25, time=10)
    G.add_edge(38, 44, band=25, time=13.5)

    G.add_edge(39, 38, band=25, time=10)
    G.add_edge(39, 40, band=25, time=10)
    G.add_edge(39, 45, band=25, time=13.5)

    G.add_edge(40, 39, band=25, time=10)
    G.add_edge(40, 41, band=25, time=10)
    G.add_edge(40, 46, band=25, time=13.5)

    G.add_edge(41, 40, band=25, time=10)
    G.add_edge(41, 42, band=25, time=10)
    G.add_edge(41, 47, band=25, time=13.5)

    G.add_edge(42, 41, band=25, time=10)
    G.add_edge(42, 48, band=25, time=13.5)

    #
    G.add_edge(43, 37, band=25, time=13.5)
    G.add_edge(43, 44, band=25, time=14)
    G.add_edge(43, 49, band=25, time=13.5)

    G.add_edge(44, 38, band=25, time=13.5)
    G.add_edge(44, 43, band=25, time=14)
    G.add_edge(44, 45, band=25, time=14)
    G.add_edge(44, 50, band=25, time=13.5)

    G.add_edge(45, 39, band=25, time=13.5)
    G.add_edge(45, 44, band=25, time=14)
    G.add_edge(45, 46, band=25, time=14)
    G.add_edge(45, 51, band=25, time=13.5)

    G.add_edge(46, 40, band=25, time=13.5)
    G.add_edge(46, 45, band=25, time=14)
    G.add_edge(46, 47, band=25, time=14)
    G.add_edge(46, 52, band=25, time=13.5)

    G.add_edge(47, 41, band=25, time=13.5)
    G.add_edge(47, 46, band=25, time=14)
    G.add_edge(47, 48, band=25, time=14)
    G.add_edge(47, 53, band=25, time=13.5)

    G.add_edge(48, 42, band=25, time=13.5)
    G.add_edge(48, 47, band=25, time=14)
    G.add_edge(48, 54, band=25, time=13.5)

    #
    G.add_edge(49, 43, band=25, time=13.5)
    G.add_edge(49, 50, band=25, time=14)

    G.add_edge(50, 44, band=25, time=13.5)
    G.add_edge(50, 49, band=25, time=14)
    G.add_edge(50, 51, band=25, time=14)

    G.add_edge(51, 45, band=25, time=13.5)
    G.add_edge(51, 50, band=25, time=14)
    G.add_edge(51, 52, band=25, time=14)

    G.add_edge(52, 46, band=25, time=13.5)
    G.add_edge(52, 51, band=25, time=14)
    G.add_edge(52, 53, band=25, time=14)

    G.add_edge(53, 47, band=25, time=13.5)
    G.add_edge(53, 52, band=25, time=14)
    G.add_edge(53, 54, band=25, time=14)

    G.add_edge(54, 48, band=25, time=13.5)
    G.add_edge(54, 53, band=25, time=14)

    # 这两行代码解决 plt 中文显示的问题
    # plt.rcParams['font.sans-serif'] = ['SimSun']
    # plt.rcParams['axes.unicode_minus'] = False


    nx.draw(G, with_labels=True, node_color='y', pos=pos)
    # 格式化输出时延 t=xx
    edgeTime = nx.get_edge_attributes(G, 'time')
    edgeLabel = {}  # 边的标签
    for i in edgeTime.keys():  # 整理边的标签，用于绘图显示
        edgeLabel[i] = f't={edgeTime[i]:}'  # 边的容量
    nx.draw_networkx_edge_labels(G, pos, edgeLabel, font_color='navy')

    # 格式化输出带宽 b=xx
    # edgeBand = nx.get_edge_attributes(G, 'band')
    # for i in edgeBand.keys():  # 整理边的标签，用于绘图显示
    #     edgeLabel[i] += ',b=' + str(edgeBand[i])

    nx.draw_networkx_edge_labels(G, pos, edgeLabel, font_color='navy')

    plt.savefig("1_bali_dongjing.jpg", dpi=300, bbox_inches='tight')
    plt.show()

    return G

def select_path(path):
    '''
    选择所有最短路径
    :param path: 输入路径
    :return:
    '''
    cols = []
    select_path = []
    for i in range(len(path)):
        cols.append(len(path[i]))
    for i in range(len(cols)):
        if cols[i] == min(cols):
            select_path.append(path[i])
    return select_path

def get_path(G,start=1, end=12):
    '''
    获取路径
    :param G: 无向图
    :param start: 起始节点
    :param end: 终止节点
    :return:
    '''
    G_dic = {}
    for i in list(G.nodes):
        G_dic[i] = list(G[i])

    # 将图保存成字典
    # {1: [2, 5],
    #  2: [1, 3, 6],
    #  3: [2, 4, 7],
    #  4: [3, 8],
    #  5: [1, 6, 9],
    #  6: [2, 5, 7, 10],
    #  7: [3, 6, 8, 11],
    #  8: [4, 7, 12],
    #  9: [5],
    #  10: [6],
    #  11: [7],
    #  12: [8]}

    def findAllPath(graph, start, end, path=[]):
        # path.append(start)
        path = path + [start]
        if start == end:
            return path

        for node in graph[start]:
            if node not in path:
                newpaths = findAllPath(graph, node, end, path)
                for newpath in newpaths:
                    if newpath == end:
                        path.append(newpath)
                        paths.append(path)
        return paths

    # 输入：
    paths = []  # 存储所有路径
    path = findAllPath(G_dic, start=start, end=end)
    # [[1, 2, 3, 4, 8, 7, 6], [1, 2, 3, 7, 6], [1, 2, 6], [1, 5, 6]]

    path = select_path(path)  # 选择所有最短路径
    return path

def get_delay(path):
    '''
    获取时延
    :param path: 路径信息
    :return:
    '''
    # 结点与结点之间的时延,实
    base_delay = {'12': 9,
                  '23': 9,
                  '34': 9,
                  '45': 9,
                  '56': 9,

                  '21': 9,
                  '32': 9,
                  '43': 9,
                  '54': 9,
                  '65': 9,

                  '78': 11,
                  '89': 11,
                  '910': 11,
                  '1011': 11,
                  '1112': 11,

                  '87': 11,
                  '98': 11,
                  '109': 11,
                  '1110': 11,
                  '1211': 11,

                  '1314': 14,
                  '1415': 14,
                  '1516': 14,
                  '1617': 14,
                  '1718': 14,

                  '1413': 14,
                  '1514': 14,
                  '1615': 14,
                  '1716': 14,
                  '1817': 14,

                  '1920': 11,
                  '2021': 11,
                  '2122': 11,
                  '2223': 11,
                  '2324': 11,

                  '2019': 11,
                  '2120': 11,
                  '2221': 11,
                  '2322': 11,
                  '2423': 11,

                  '2526': 9,
                  '2627': 9,
                  '2728': 9,
                  '2829': 9,
                  '2930': 9,

                  '2625': 9,
                  '2726': 9,
                  '2827': 9,
                  '2928': 9,
                  '3029': 9,

                  '3738': 10,
                  '3839': 10,
                  '3940': 10,
                  '4041': 10,
                  '4142': 10,

                  '3837': 10,
                  '3938': 10,
                  '4039': 10,
                  '4140': 10,
                  '4241': 10,

                  '4344': 14,
                  '4445': 14,
                  '4546': 14,
                  '4647': 14,
                  '4748': 14,

                  '4443': 14,
                  '4544': 14,
                  '4645': 14,
                  '4746': 14,
                  '4847': 14,

                  '4950': 14,
                  '5051': 14,
                  '5152': 14,
                  '5253': 14,
                  '5354': 14,

                  '5049': 14,
                  '5150': 14,
                  '5251': 14,
                  '5352': 14,
                  '5453': 14,

                  '5556': 10,
                  '5657': 10,
                  '5758': 10,
                  '5859': 10,
                  '5960': 10,

                  '5655': 10,
                  '5756': 10,
                  '5857': 10,
                  '5958': 10,
                  '6059': 10,

                  '17':13.5,
                  '713': 13.5,
                  '1319': 13.5,
                  '1925': 13.5,
                  '2531': 13.5,
                  '3137': 13.5,
                  '3743': 13.5,
                  '4349': 13.5,
                  '4955': 13.5,
                  '5561': 13.5,
                  '611': 13.5,

                  '71': 13.5,
                  '137': 13.5,
                  '1913': 13.5,
                  '2519': 13.5,
                  '3125': 13.5,
                  '3731': 13.5,
                  '4337': 13.5,
                  '4943': 13.5,
                  '5549': 13.5,
                  '6155': 13.5,
                  '161': 13.5,

                  '28': 13.5,
                  '814': 13.5,
                  '1420': 13.5,
                  '2026': 13.5,
                  '2632': 13.5,
                  '3238': 13.5,
                  '3844': 13.5,
                  '4450': 13.5,
                  '5056': 13.5,
                  '5662': 13.5,
                  '622': 13.5,

                  '82': 13.5,
                  '148': 13.5,
                  '2014': 13.5,
                  '2620': 13.5,
                  '3226': 13.5,
                  '3832': 13.5,
                  '4438': 13.5,
                  '5044': 13.5,
                  '5650': 13.5,
                  '6256': 13.5,
                  '262': 13.5,

                  '39': 13.5,
                  '915': 13.5,
                  '1521': 13.5,
                  '2127': 13.5,
                  '2733': 13.5,
                  '3339': 13.5,
                  '3945': 13.5,
                  '4551': 13.5,
                  '5157': 13.5,
                  '5763': 13.5,
                  '633': 13.5,

                  '93': 13.5,
                  '159': 13.5,
                  '2115': 13.5,
                  '2721': 13.5,
                  '3327': 13.5,
                  '3933': 13.5,
                  '4539': 13.5,
                  '5145': 13.5,
                  '5751': 13.5,
                  '6357': 13.5,
                  '363': 13.5,

                  '410': 13.5,
                  '1016': 13.5,
                  '1622': 13.5,
                  '2228': 13.5,
                  '2834': 13.5,
                  '3440': 13.5,
                  '4046': 13.5,
                  '4652': 13.5,
                  '5258': 13.5,
                  '5864': 13.5,
                  '644': 13.5,

                  '104': 13.5,
                  '1610': 13.5,
                  '2216': 13.5,
                  '2822': 13.5,
                  '3428': 13.5,
                  '4034': 13.5,
                  '4640': 13.5,
                  '5246': 13.5,
                  '5852': 13.5,
                  '6458': 13.5,
                  '464': 13.5,

                  '511': 13.5,
                  '1117': 13.5,
                  '1723': 13.5,
                  '2329': 13.5,
                  '2935': 13.5,
                  '3541': 13.5,
                  '4147': 13.5,
                  '4753': 13.5,
                  '5359': 13.5,
                  '5965': 13.5,
                  '655': 13.5,

                  '115': 13.5,
                  '1711': 13.5,
                  '2317': 13.5,
                  '2923': 13.5,
                  '3529': 13.5,
                  '4135': 13.5,
                  '4741': 13.5,
                  '5347': 13.5,
                  '5953': 13.5,
                  '6559': 13.5,
                  '565': 13.5,

                  '612': 13.5,
                  '1218': 13.5,
                  '1824': 13.5,
                  '2430': 13.5,
                  '3036': 13.5,
                  '3642': 13.5,
                  '4248': 13.5,
                  '4854': 13.5,
                  '5460': 13.5,
                  '6066': 13.5,
                  '666': 13.5,

                  '126': 13.5,
                  '1812': 13.5,
                  '2418': 13.5,
                  '3024': 13.5,
                  '3630': 13.5,
                  '4236': 13.5,
                  '4842': 13.5,
                  '5448': 13.5,
                  '6054': 13.5,
                  '6660': 13.5,


                  }

    # 计算每条可行路径的时延
    route_delay = {}
    for i in range(len(path)):
        # 遍历每条路径
        route_delay_temp = 0
        for j in range(len(path[i])):
            # 遍历该路径两两之间的路径
            if j < len(path[i]) - 1:
                node_order = str(path[i][j]) + str(path[i][j + 1])
                route_delay_temp += int(base_delay[node_order])
        route_delay[i] = route_delay_temp / 3000
    return route_delay