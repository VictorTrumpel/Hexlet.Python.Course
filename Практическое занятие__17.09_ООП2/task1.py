class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю!")
        
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def reduce(self):
      g = self.gcd(abs(self.numerator), abs(self.denominator))

      if g > 1:  # дробь можно сократить
          self.numerator //= g
          self.denominator //= g
      # если знаменатель отрицательный — переносим минус в числитель

      if self.denominator < 0:
          self.numerator *= -1
          self.denominator *= -1

      return self  

    # алгоритм Евклида для НОД
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Деление на ноль в дробях!")
        
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator

        return Fraction(num, den)


a = Fraction(1, 2)   
c = Fraction(2, 3)   
e = Fraction(3, 4)   
g = Fraction(4, 5)   
k = Fraction(5, 6)   

Z = (a + c) / e * (g - k)

print("Z =", Z)

print("Z reduce = ", Z.reduce())

reducable_fraction = Fraction(4, 8)

print('Reducable fraction', reducable_fraction)
print('Reduced reducable fraction', reducable_fraction.reduce())
