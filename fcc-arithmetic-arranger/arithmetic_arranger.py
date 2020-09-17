def arithmetic_arranger(problems, printstat = False):
  
  addend1 = ""
  addend2 = ""
  dashes = ""
  result = ""

  if len(problems)>5:
    return "Error: Too many problems."
         
  arranged_problems = []
  
  for i in problems:
    x = i.split()
    n1 = x[0]
    n2 = x[2]
    op = x[1]
      
    if op == "*" or op == "/":
      return "Error: Operator must be '+' or '-'."
    else:
      if not n1.isdigit() or not n2.isdigit():
        return "Error: Numbers must only contain digits."
      else:
        if len(n1)>4 or len(n2)>4:
          return "Error: Numbers cannot be more than four digits."
        else:
          if op == "+":
            answer = int(n1) + int(n2)
          else:
            answer = int(n1) - int(n2)
            
          width = max(len(n1),len(n2))+2
          addend1 += str(n1.rjust(width))
          addend2 +=  str(op + n2.rjust(width-1)) 
          dashes += str("-" * width)
          result += str(answer).rjust(width)

          if i != problems[-1]:
            addend1 += "    "
            addend2 += "    "
            dashes += "    "
            result += "    "
            
          else:
            if printstat == True:
              arranged_problems = (addend1 + "\n" + addend2 + "\n" + dashes + "\n" + result)
            else: 
              arranged_problems = (addend1 + "\n" + addend2 + "\n" + dashes)

  return arranged_problems

  