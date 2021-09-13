# kind of very specific, but can use similar ideas in the future
# take positive or negative integers with double spaces in an *xN grid and format them in a nested list
def take_input(N):
  return [list(map(int, filter(lambda x: int(x.strip()) if x!='' else False, input().split(" ")))) for _ in range(N)]
