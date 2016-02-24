# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:42:42 2016

@author: Chao Zhao

magnify the merge.txt
"""

import codecs

def check_mark():
    i = -1
    flag = ''
    with codecs.open('merge_v3.txt', encoding = "utf-8") as fin:
        for line in fin:
            if 'TxtFile' in line:
                i = -1
                flag = line
            i += 1
            if i == 1:
                if (u'性别' in line) or (u'首次' in line):
                    continue
                print flag
                print line
     
def delete_blank_and_comment():
    fout = codecs.open('merge_v4.txt', "w+", "utf-8")
    
    with codecs.open('merge_v3.txt', encoding = "utf-8") as fin:
        for line in fin:
            if line.startswith('RecordFile')or not line.split():
                continue
            fout.write(line)
    fin.close()
    fout.close()

def split_file():
    new_file = False
    fout = codecs.open('temp', "w+", "utf-8")
    with codecs.open('merge_v3.txt', encoding = "utf-8") as fin:
        for line in fin:
            if line.startswith('RecordFile'):
                pass
            if line.startswith('TxtFile'):
                fout.close()
                filename = line[9:]
                new_file = True
                continue
            if new_file:
                new_file = False
                filename_list = filename.split('.')
                filename = filename_list[0]
                if u'性别' in line:
                    filename += 'discharge.txt'
                elif u'首次' in line:
                    filename += 'progress.txt'
                else:
                    pass
                fout = codecs.open(filename, "w+", "utf-8")
            fout.write(line)
    fout.close()
    
    
    
    
#delete_blank_and_comment()
#delete_blank_and_comment()
split_file()