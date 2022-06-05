# 弹跳球程序
xcor=300	# x坐标
ycor=300
xvel=1	# vel：速度
yvel=2

def setup():
	size(600,600)

def draw():
	global xcor,ycor,xvel,yvel
	background(0)
	xcor+=xvel
	ycor+=yvel
	# 如果小球碰到墙（边界）,就改变方向（反弹）
	if xcor>width or xcor<0:
		xvel=-xvel
	if ycor>height or ycor<0:
		yvel=-yvel
	ellipse(xcor,ycor,20,20)
'''
注：recoded by lfdx @ 2022.05.03
from 《用Python学数学》（Math Adventures with Python）by[美]Peter Farrell
第三部分 第9章 用类构建对象
'''
