import math
import random
No_of_rounds = int(input('how many times you want to try: '))
i = 0
j = 0
while i<=No_of_rounds:
    rand1 = math.pi * random.random()
    rand2 = math.pi * 2 * random.random()
    if rand2 <= rand1:
        j = j + 1
    i = i+1
print(f'\n\n\nThe computer has tried it for you \nAnd got that \n(No. of times centre was in the triangle) /(total tries) = \n{j/No_of_rounds}')
print('that is preety close to what khushank said :-)')