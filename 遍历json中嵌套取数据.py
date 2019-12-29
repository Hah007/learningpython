#! /usr/bin/python
# coding:utf-8 
""" 
@author:Bingo.he 
@file: get_target_value.py 
@time: 2017/12/22 
"""
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list


    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value


    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身

if __name__ == '__main__':
    test_dic={'index': 0, 'keywords': '蜘蛛#侠#', 'vjson': {'v0': ['吸血鬼,0.50844085', '猎人,0.4639404', '雄狮,0.44035226', '小鸟,0.4158151', '接头,0.39510632', '三线,0.3950517', '轴,0.3850325', '绿灯,0.38122165', 'Eta,0.37424707'], 'v1': ['钢铁,0.50844085', '猎人,0.5067125', '阿萨,0.413885', '寄居蟹,0.40661845', '奸,0.358147', '纵坐标,0.3468271', 'nikita,0.34402883', '反派,0.34076482', 'fringe,0.32994255'], 'v2': ['吸血鬼,0.5067125', '钢铁,0.4639404', '省会,0.46083134', '三线,0.42988417', '小鸟,0.36110768', '怪物,0.33483237', '反派,0.32662928', '旅人,0.32142222', 'eThan,0.31405216']}, 'w2vlist': ['钢铁,0.8176874', '吸血鬼,0.48830876', '猎人,0.43854454', '小鸟,0.43056497', '雄狮,0.42994845', '大猩猩,0.42252985', '青蛙,0.3941476', '绿灯,0.38010225', '菇类,0.37977317', '菌,0.36644444']}
    test_list=[1,2,3]
    print('关键词=',get_target_value('keywords',test_dic,[]))
    print('w2vlist=',get_target_value('w2vlist',test_dic,[]))
    print('v0=',get_target_value('v0',test_dic,[]))
    print('v1=',get_target_value('v1',test_dic,[]))
    print('吸血鬼=',get_target_value('index',test_dic,test_list))
