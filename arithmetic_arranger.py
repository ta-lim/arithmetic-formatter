def arithmetic_arranger(problems, show = False):
  
  qst_1 = ''
  qst_2 = ''
  equal = ''
  ans = ''
  semua = ''
  loop = 1
  
  if len(problems) > 5:
    return 'Error: Too many problems.'
  for numbers in problems:
    number = numbers.split()
    
    if not number[1] == '-':
      if not number[1] == '+':
        return 'Error: Operator must be \'+\' or \'-\'.'
    
    try:
      int_1 = int(number[0])
      int_2 = int(number[2])
    except:
      return 'Error: Numbers must only contain digits.'
      
    if len(number[0]) > 4 or len(number[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
   
    if len(number[0]) >= len(number[2]):
      equal_len = len(number[0]) + 2
    else:
      equal_len = len(number[2]) + 2
    space_1 = equal_len - len(number[0])
    space_2 = equal_len - len(number[2]) - 1

    for i in range(space_1):
      qst_1 += ' '
    qst_1 += number[0]
    if loop < len(problems):
      qst_1 += '    '
    
    qst_2 += number[1]
    for i in range(space_2):
      qst_2 += ' '
    qst_2 += number[2]
    if loop < len(problems):
      qst_2 += '    '

    for i in range(equal_len):
      equal += '-'
    if loop < len(problems):
      equal += '    '
    
    if show:
      if number[1] == '+':
        tmp = int(number[0]) + int(number[2])
      if number[1] == '-':
        tmp = int(number[0]) - int(number[2])
      for i in range(equal_len-len(str(tmp))):
        ans += ' '
  
      ans += str(tmp)
      if loop < len(problems):
        ans += '    '
        
    loop += 1

  if show == True:
    semua = qst_1 + '\n' + qst_2 + '\n' + equal + '\n' + ans
  else: 
    semua = qst_1 + '\n' + qst_2 + '\n' + equal
  return semua