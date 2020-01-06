# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:51:54 2019

@author: wupeng
"""

# -*- coding: utf-8 -*-
#@author: Yuhao Zhang
#2018.5.30

import jieba
import codecs
from collections import defaultdict
from pandas import DataFrame
import pandas as pd

#路径设置。
#文档介绍
#jsjs.txt是胡兰成写的小说《今生今世》。
#person.txt是一个语料库，里面放了很多该小说的角色名称。
#synonymous_dict.txt是角色的别名
#其他两个文件是存放程序计算所得各个人物关系之间的边的权重
TEXT_PATH = 'qingyunian.txt'
DICT_PATH = 'person.txt'
SYNONYMOUS_DICT_PATH = 'synonymous_dict.txt'
SAVE_NODE_PATH = 'node.csv'
SAVE_EDGE_PATH = 'edge.csv'

#类的初始化
class RelationshipView:
    def __init__(self, text_path, dict_path, synonymous_dict_path):
        self._text_path = text_path
        self._dict_path = dict_path
        self._synonymous_dict_path = synonymous_dict_path
        self._person_counter = defaultdict(int)
        self._person_per_paragraph = []
        self._relationships = {}
        self._synonymous_dict = {}

    def generate(self):
        self.count_person()
        self.calc_relationship()
        self.save_node_and_edge()

    def synonymous_names(self):
        with codecs.open(self._synonymous_dict_path, 'r', 'utf-8') as f:
            lines = f.read().split('\n')
        for l in lines:
            self._synonymous_dict[l.split(' ')[0]] = l.split(' ')[1]
        return self._synonymous_dict

    def get_clean_paragraphs(self):
        new_paragraphs = []
        last_paragraphs = []
        with open(self._text_path, encoding='gb18030') as f:
            paragraphs = f.read().split('\r\n')
            paragraphs = paragraphs[0].split('\u3000')
        for i in range(len(paragraphs)):
            if paragraphs[i] != '':
                new_paragraphs.append(paragraphs[i])
        for i in range(len(new_paragraphs)):
            new_paragraphs[i] = new_paragraphs[i].replace('\n', '')
            new_paragraphs[i] = new_paragraphs[i].replace(' ', '')
            last_paragraphs.append(new_paragraphs[i])
        return last_paragraphs

    def count_person(self):
        paragraphs = self.get_clean_paragraphs()
        synonymous = self.synonymous_names()
        print('start process node')
        with codecs.open(self._dict_path, 'r', 'utf-8') as f:
            name_list = f.read().split( )
            print(name_list)
        for p in paragraphs:
            jieba.load_userdict(self._dict_path)
            poss = jieba.cut(p)
            self._person_per_paragraph.append([])
            for w in poss:
                if w not in name_list:
                    continue
                if synonymous.get(w):
                    #print(w)
                    w = synonymous[w]
                self._person_per_paragraph[-1].append(w)
                if self._person_counter.get(w) is None:
                    self._relationships[w] = {}
                self._person_counter[w] += 1
        return self._person_counter

    def calc_relationship(self):
        print("start to process edge")
        for p in self._person_per_paragraph:
            for name1 in p:
                for name2 in p:
                    if name1 == name2:
                        continue
                    if self._relationships[name1].get(name2) is None:
                        self._relationships[name1][name2] = 1
                    else:
                        self._relationships[name1][name2] += 1
        return self._relationships

    def save_node_and_edge(self):
        excel = []
        for name, times in self._person_counter.items():
            excel.append([])
            excel[-1].append(name)
            excel[-1].append(name)
            excel[-1].append(str(times))
        data = DataFrame(excel, columns=['Id', 'Label', 'Weight'])
        data.to_csv('node.csv', encoding='gbk')

        excel = []
        for name, edges in self._relationships.items():
            for v, w in edges.items():
                if w > 3:
                    excel.append([])
                    excel[-1].append(name)
                    excel[-1].append(v)
                    excel[-1].append(str(w))
        data = DataFrame(excel, columns=['Source', 'Target', 'Weight'])
        data.to_csv('edge.csv', encoding='gbk')

        print('save file successful!')

if __name__ == '__main__':
    v = RelationshipView(TEXT_PATH, DICT_PATH, SYNONYMOUS_DICT_PATH)
    v.generate()