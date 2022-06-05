# 分形|fractal
## 1. 分形树
```Python
# fractal|分形树
def setup():
    size(600,600)

def draw():
    background(255)
    translate(300,500)
    level=int(map(mouseX,0,width,0,15))
    y(100,level)
    
def y(sz,level):
    if level>0:
        line(0,0,0,-sz)
        translate(0,-sz)
        angle=map(mouseX,0,height,0,180)
        rotate(radians(angle))
        y(0.8*sz,level-1)
        rotate(radians(-2*angle))
        y(0.8*sz,level-1)
        rotate(radians(angle))
        translate(0,sz)

'''
注：recoded by lfdx @ 2022.05.03
from 《用Python学数学》（Math Adventures with Python）by[美]Peter Farrell
第三部分 第10章 用递归制作分形
'''
```
## 2. 分形雪花
```Python
# 科赫雪花|snowflake
def setup():
    size(600,600)

def draw():
    background(255)
    translate(100,height/2-100)
    level=int(map(mouseX,0,width,0,7))  # 7,means:最高到7级,可改
    snowflake(400,level)
    
def snowflake(sz,level):
    for i in range(3):
        segment(sz,level)
        rotate(radians(120))
        
def segment(sz,level):
    if level==0:
        line(0,0,sz,0)
        translate(sz,0)
    else:
        segment(sz/3.0,level-1)
        rotate(radians(-60))
        segment(sz/3.0,level-1)
        rotate(radians(120))
        segment(sz/3.0,level-1)
        rotate(radians(-60))
        segment(sz/3.0,level-1)

'''
注：recoded by lfdx @ 2022.05.03
from 《用Python学数学》（Math Adventures with Python）by[美]Peter Farrell
第三部分 第10章 用递归制作分形
'''
```
## 3.谢尔宾斯基三角形
```Python
# 谢尔宾斯基三角形
def setup():
    size(600,600)
    
def sierpinski(sz,level):   #sz 三角形的边长;level 级别
    if level==0:
        fill(0)
        triangle(0,0,sz,0,sz/2.0,-sz*sqrt(3)/2.0)
    else:
        for i in range(3):
            sierpinski(sz/2.0,level-1)
            translate(sz,0)
            rotate(radians(-120))
            
def draw():
    background(255)
    translate(50,450)
    sierpinski(400,8)

'''
注：recoded by lfdx @ 2022.05.03
from 《用Python学数学》（Math Adventures with Python）by[美]Peter Farrell
第三部分 第10章 用递归制作分形
'''
```
