#coding=utf-8

'''
Descroption:Word文档转换txt
Author:hah007
Prompt:code in python3.7 env
'''

'''
参数描述：1 filepath 文件路径 2 savepath 保存路径
'''
import os,fnmatch
from win32com import client as wc
from win32com.client import Dispatch,gencache


def word2txt(filepath,savepath=''):

    # dirs,filename=os.path.split(filepath)
    dirs,filename = os.path.split(filepath)
    
    print(dirs,'\n',filename)

    new_filename=''
    if fnmatch.fnmatch(filename,'*.doc'):
        new_filename=filename[:-4]+'.txt'
    elif fnmatch.fnmatch(filename,'*.docx'):
        new_filename=filename[:-5]+'.txt'
    else:
        print('格式不正确，仅支持.doc和.docx')

    if savepath=='':
        savepath=dirs
    else:
        savepath=savepath
    new_save_path=os.path.join(savepath,new_filename)
    print('--->',new_save_path)

    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filepath)
    mytxt.SaveAs(new_save_path,4)
    mytxt.Close()
   

if __name__ == '__main__':
    filename=os.path.abspath(r'../word文件/郸城县建业润城花园B区结构会审建议.doc')
    print(filename)
    word2txt(filename)
