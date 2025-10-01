class DvizhimiyObject:
  def __init__(self, model_name, num_wheels):
    self.model_name = model_name
    self.num_wheels = num_wheels

class LegkovoyAvtomobil(DvizhimiyObject):
  def __init__(self, model_name, num_wheels, num_doors, has_autopilot):
    super().__init__(model_name, num_wheels)
    self.num_doors = num_doors
    self.has_autopilot = has_autopilot

  def set_doors(self, new_doors): 
    if (new_doors > 5): return
    if (new_doors < 2): return

    self.num_doors = new_doors

  def get_info(self):
    print(f'Модель: ’{self.model_name}’, {self.num_wheels} колеса, {self.num_doors} двери и статус автопилота: {self.has_autopilot}')

is_auto = True

car = LegkovoyAvtomobil('Модель X', 4, 4, is_auto)
car.get_info()

car.set_doors(2)
car.get_info()

car.set_doors(7)
car.get_info()