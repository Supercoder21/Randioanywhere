try:
    import string
    import sys
    import random
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    print('Not to be used with security purposes')
    x = input('')
    y = x.split()
    if y[0] == 'P':
        if y[1] == 'L':
            letters = 12
            random_string = "".join(random.choice(string.ascii_letters) for i in range(letters))
            print(random_string)
        elif y[1] == 'F':
            y = random.random()
            print(y+random.randint(0,sys.maxsize))
        elif y[1] == 'I':
            t = random.randint(0,sys.maxsize)
            print(t)
        else:
            print('Error')
            time.sleep(5)
    elif y[0] == 'Ranby':
        bits = ''
        for i in range(8):
          bits = bits+str(random.choice([0,1]))
        print(bits)
    elif y[0] == 'Ran10':
      print(random.choice([0,1]))
    elif y[0] == 'RW':
      arra = []
      itter = []
      si = 1
      while si >= 0:
        itter.append(si)
        si = si + random.choice([-1,1])
      li = len(itter)
      for i in range(li):
        arra.append(i)
      name = input('Enter title ' )
      xaxis = input('Enter x axis name ')
      yaxis = input('Enter y axis name ')
      x = np.array(arra)
      y = np.array(itter)
      plt.plot(x,y)
      plt.title(name)
      plt.xlabel(xaxis)
      plt.ylabel(yaxis)
      plt.show()
    elif y[0] == 'Seti':
      seti = random.randint(0,sys.maxsize)
      seti = str(seti)
      print('Seti setting to '+seti+'...')
      time.sleep(5)
      seti = int(seti)
      if y[1] == 'Add':
        setx = random.randint(0,sys.maxsize)
        print(setx + seti)
      elif y[1] == 'Sub':
        setx = random.randint(0,sys.maxsize)
        print(setx - seti)
      elif y[1] == 'Multi':
        setx = random.randint(0,sys.maxsize)
        print(setx*seti)
      elif y[1] == 'Div':
        setx = random.randint(0,sys.maxsize)
        print(setx/seti)
      else:
          print('Error')
          time.sleep(5)
    elif y[0] == 'RWSte':
      l = int(input(''))
      print()
      rwstep = 0
      le = 0
      r = 0
      for i in range(1,l+1):
        t= random.choice([-1,1])
        rwstep = rwstep + t
        if t == -1:
          r = r+1
          print('Right')
        if t==1:
          le = le+1
          print('Left')
      print()
      print('Left steps: '+str(le))
      print('Right steps: '+str(r))   
    else:
      print('Error')
      time.sleep(5)
except:
    print('Error')
    time.sleep(5)
