cells = [0]*30
current_cell = 0
program = input("brainf***> ")
program = list(program)
output = ""
def run(program):
  global cells
  global current_cell
  global output
  for char in program:
    if char == ">":
      current_cell += 1
    elif char == "<":
      current_cell -= 1
    elif char == "+":
      cells[current_cell] += 1
    elif char == "-":
      cells[current_cell] -= 1
    elif char == ".":
      output += str(chr(cells[current_cell]))
    elif char == ",":
      cells[current_cell] = int(input("Enter Value: "))
    elif char == "[":
      while cells[current_cell] != 0:
        loop = program[program.index(char)+1:program.index("]")]
        print(cells[current_cell])
        run(loop)
run(program)
print(cells)
print(output)
#hello world
#++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]
#add two numbers
#++>+++++[<+>-]++++++++[<++++++>-]<.
