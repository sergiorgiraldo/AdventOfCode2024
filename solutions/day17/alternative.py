import functools


class Simulator:
  def __init__(self, prog):
    self.prog = prog
    self.minback = 1e20

  #see `decompile`
  def simulate(self,register):
    a, b, c = register, 0, 0
    ans = []
    while a:
      b = a % 8
      b = b ^ 3
      c = a // (2 ** b)
      a = a // 8
      b = b ^ 4
      b = b ^ c
      ans.append(b % 8)
    return ans

  @functools.cache
  def recursive(self, back, shift):
    if shift == 16:
      x = self.simulate(back)
      if x[:shift] == self.prog[:shift]:
        self.minback = min(self.minback, back)
      return
    for i in range(256 * 8):
      stable = 2 ** (3 * shift)
      n = back + i * stable
      x = self.simulate(n)
      if x[:shift + 1] == self.prog[:shift + 1]:
        self.recursive(n % (2 ** (3 * shift + 3)), shift + 1)

  def search(self):
    self.recursive(0, 0)
    return self.minback

simluator = Simulator([2,4,1,3,7,5,0,3,1,4,4,7,5,5,3,0])
print(simluator.search())