'''
Created on Mar 31, 2019

@author: Jiaming
'''

def parse_info(str):
    info = str.split(" ")
    x = eval(info[0].split("'")[1].split(',')[0])
    y = eval(info[1].split(",")[0])
    button = eval(info[2][0])
    
    print("x:", x, "y:", y, "button:",button)
    
str = "b'647, 684, 0\r\n'"

parse_info(str)