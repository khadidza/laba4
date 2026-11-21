class Calculator:
  def add(self, a: float, b: float) -> float:
    return a+b
  def subs(self, a: float, b: float) -> float:
    return a - b
  def mult(self, a:float, b: float) -> float:
    return a * b
   def mult(self, a:float, b: float) -> float:
     if b == 0:
       raise ValueError
      return a / b
