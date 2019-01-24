# -*- coding:utf-8 -*-

class Settings():
	# �洢�����������֡����������� ����
	def __init__(self):
		# ��ʼ����Ϸ�������, ��Ļ����
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (230, 230, 230)
		# �ɴ�������
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		# �ӵ�����
		self.bullet_speed_factor = 0.3
		self.bullet_width = 500
		self.bullet_height = 5
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10	# �洢�����������ӵ���
		# ����������
		self.alien_speed_factor = 0.2	# ���������������ƶ�������
		self.fleet_drop_speed = 50	# ײ����Ļ��Եʱ�����ƶ����ٶ�
		self.fleet_direction = 1	# fleet_directionΪ1��ʾ�����ƶ���Ϊ-1��ʾ�����ƶ�
		
