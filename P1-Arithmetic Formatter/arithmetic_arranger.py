import re
def arithmetic_arranger(problems):
  if len(problems) == 2:
    problems = problems[0]
  
  print(dir(problems))
  arranged_problems = "40"

  #test_too_many_problems
  if len(problems) > 5:
    return "Error: Too many problems."
    
  #convert problems list into a string (without white spaces)
  problemsString = ' '.join(problems)

  problemsOperators = re.findall('\W+', problemsString)
  problemsNumbers = re.findall('\w+', problemsString)

  problemsOperatorsString = ''.join(problemsOperators).replace(" ", "")

  #test_incorrect_operator
  if len(re.findall('[^+-]', problemsOperatorsString)) != 0:
    return "Error: Operator must be '+' or '-'."    
  
  for number in problemsNumbers:
    number = number.strip()
    #test_only_digits
    if len(re.findall('[^0-9]', number)) != 0:
      return "Error: Numbers must only contain digits."
      
    #test_too_many_digits
    if len(number) > 4:
      return "Error: Numbers cannot be more than four digits."
  

  for problemIndex in problems:
    print(problemIndex)
  
  return arranged_problems
