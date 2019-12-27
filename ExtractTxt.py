#coding=utf-8
'''
Description: 多文档格式转换工具
Author：hah007
Prompt: code in Python3.7
'''

import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch,gencache

'''
功能描述：抽取文件文本信息
参数描述：1 filePath：文件路径 2 savePath： 指定保存路径
'''
def Files2Txt(filePath,savePath=''):
        
    try:

        # 1 切分文件上级目录和文件名
        dirs,filename = os.path.split(filePath)
        print('目录：',dirs,'\n文件名：',filename)

        # 2 修改转化后的文件名
        typename = os.path.splitext(filename)[-1].lower() # 获取后缀
        new_name = TranType(filename,typename)
        print('新的文件名：',new_name)

        # 3 文件转化后的保存路径
        if savePath=="": savePath = dirs
        else: savePath = savePath
        new_save_path = os.path.join(savePath,new_name)
        print('保存路径：',new_save_path)

        # 4 加载处理应用
        wordapp = wc.Dispatch('Word.Application')
        mytxt = wordapp.Documents.Open(filePath)
        mytxt.SaveAs(new_save_path,4)
        mytxt.Close()
    except Exception as e:
        pass
    '''
    功能描述：根据文件后缀修改文件名
    参数描述：1 filePath：文件路径 2 typename 文件后缀
    返回数据：new_name 返回修改后的文件名
    '''
def TranType(filename,typename):

    # 新的文件名称
    new_name = ''
    if typename == '.pdf' : # pdf->txt
        if fnmatch.fnmatch(filename,'*.pdf') :
            new_name = filename[:-4]+'.txt' # 截取".pdf"之前的文件名
        else: return
    elif typename == '.doc' or typename == '.docx' :  # word->txt
        if fnmatch.fnmatch(filename, '*.doc') :
            new_name = filename[:-4]+'.txt'
        elif fnmatch.fnmatch(filename, '*.docx'):
            new_name = filename[:-5]+'.txt'
        else: return
    else:
        print('警告：\n您输入[',typename,']不合法，本工具仅支持pdf/doc/docx格式,请输入正确格式。')
        return
    return new_name


if __name__ == '__main__':

    filePath1 = os.path.abspath(r'../word文件/郸城县建业润城花园B区结构会审建议.doc')
    # print(filePath1)
    filePath2 = os.path.abspath(r'../word文件/高吨位消防车等效荷载取值研究.pdf')
    # filePath3 = os.path.abspath(r’../dataSet/Corpus/wordtotxt/科技项目数据挖掘决策架构.docx’)
    Files2Txt(filePath2)
 
'''
转化代码含义：
wdFormatDocument                    =  0
wdFormatDocument97                  =  0
wdFormatDocumentDefault             = 16
wdFormatDOSText                     =  4
wdFormatDOSTextLineBreaks           =  5
wdFormatEncodedText                 =  7
wdFormatFilteredHTML                = 10
wdFormatFlatXML                     = 19
wdFormatFlatXMLMacroEnabled         = 20
wdFormatFlatXMLTemplate             = 21
wdFormatFlatXMLTemplateMacroEnabled = 22
wdFormatHTML                        =  8
wdFormatPDF                         = 17
wdFormatRTF                         =  6
wdFormatTemplate                    =  1
wdFormatTemplate97                  =  1
wdFormatText                        =  2
wdFormatTextLineBreaks              =  3
wdFormatUnicodeText                 =  7
wdFormatWebArchive                  =  9
wdFormatXML                         = 11
wdFormatXMLDocument                 = 12
wdFormatXMLDocumentMacroEnabled     = 13
wdFormatXMLTemplate                 = 14
wdFormatXMLTemplateMacroEnabled     = 15
wdFormatXPS                         = 18
'''