class MyVector:
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)

  def __add__(self, other):
    if isinstance(other, MyVector):
      return MyVector(self.x + other.x, self.y + other.y)
    return NotImplemented

  def __sub__(self, other):
    if isinstance(other, MyVector):
      return MyVector(self.x - other.x, self.y - other.y)
    return NotImplemented

  def __mul__(self, scalar):
    if isinstance(scalar, (int, float)):
      return MyVector(self.x * scalar, self.y * scalar)
    return NotImplemented

  def __rmul__(self, scalar):
    return self.__mul__(scalar)

  def __str__(self):
    return f"MyVector({self.x}, {self.y})"
  
v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)

v_sum = v1 + v2

print(v_sum)

v_diff = v1 - v2
print(v_diff)

v_mul = v1 * 1.5
print(v_mul)

v_rmul = -2 * v1
print(v_rmul)