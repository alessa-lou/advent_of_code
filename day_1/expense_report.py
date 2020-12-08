class ExpenseReport():
  
  def __init__(self):
    self.res = []

  def read_input(self):
    f = open("puzzle_input.txt", "r")
    file_content = [int(line.strip()) for line in f.readlines()]
    # print(file_content)
    return file_content
  
  def add_nums(self):
    file_content = self.read_input()
    print("printing file_content")
    print(file_content)
    print(type(file_content))
    for i, val1 in enumerate(file_content):
      for j, val2 in enumerate(file_content[i+1:]):
        if val1 + val2 == 2020:
          print(val1)
          print(val2)
          self.res.append(val1 + val2)
          print(self.res)
          answer = val1 * val2
          print(answer)
          return answer



    # for i in range(0, len(file_content), 2):
    #   res.append(file_content[i] + file_content[i + 1])
    #   counter+=1
    # print("printing res")
    # print(res)
    # print(counter)
    # return res

   