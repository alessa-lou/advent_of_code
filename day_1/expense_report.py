class ExpenseReport():
  
  def __init__(self):
    self.res = []
    self.res_two = []

  def read_input(self):
    f = open("puzzle_input.txt", "r")
    file_content = [int(line.strip()) for line in f.readlines()]
    # print(file_content)
    return file_content
  
  def add_nums(self):
    file_content = self.read_input()
    for i, val1 in enumerate(file_content):
      for j, val2 in enumerate(file_content[i+1:]):
        if val1 + val2 == 2020:
          self.res.append(val1 + val2)
          part_one_answer = val1 * val2
          print(part_one_answer)
          return part_one_answer

  def add_three_nums(self):
    file_content = self.read_input()
    for i, val1 in enumerate(file_content):
      for j, val2 in enumerate(file_content[i+1:]):
        for val3 in file_content[i+j+1:]:
          if val1 + val2 + val3 == 2020:
            self.res_two.append(val1+val2+val3)
            print(self.res_two)
            part_two_answer = val1*val2*val3
            print(part_two_answer)
            return part_two_answer
    


   