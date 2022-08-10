def initCounter(counter = 0):
  def inc(n = 1):
    counter += n
  return counter, inc