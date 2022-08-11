def initCounter(init = 0):
  counter = init
  def inc(n = 1):
    counter += n
  return counter, inc