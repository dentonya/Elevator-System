import math
class Floor(object):
	def __init__(self,canvas,app,name):
		self.app = app
		self.name = name
		self.shift_x = 473
		self.canvas=canvas

		self.number = canvas.create_text(75, (10-name)*60 + 10, text=name,activefill="red")
		self.up_status = "off"
		self.down_status = "off"
		self.elevator_floor_up = None
		self.elevator_floor_down = None
		
