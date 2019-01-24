# -*- coding:utf-8 -*-

class Settings():
	# 存储《外星人入侵》的所有设置 的类
	def __init__(self):
		# 初始化游戏外观设置, 屏幕设置
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (230, 230, 230)
		# 飞船的设置
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		# 子弹设置
		self.bullet_speed_factor = 0.3
		self.bullet_width = 500
		self.bullet_height = 5
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10	# 存储所允许的最大子弹数
		# 外星人设置
		self.alien_speed_factor = 0.2	# 设置外星人向右移动的速速
		self.fleet_drop_speed = 50	# 撞到屏幕边缘时向下移动的速度
		self.fleet_direction = 1	# fleet_direction为1表示向右移动，为-1表示向左移动
		
