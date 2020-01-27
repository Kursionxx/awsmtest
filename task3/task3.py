import sys
import os
  
file = open(sys.argv[1])
Cash1 = []
for line in file:
    Cash1.append(float(line))
file.close()

file = open(sys.argv[2])
Cash2 = []
for line in file:
    Cash2.append(float(line))
file.close()

file = open(sys.argv[3])
Cash3 = []
for line in file:
    Cash3.append(float(line))
file.close()

file = open(sys.argv[4])
Cash4 = []
for line in file:
    Cash4.append(float(line))
file.close()

Cash1_max = max(Cash1) # максимальное значение для первой кассы
Cash2_max = max(Cash2)
Cash3_max = max(Cash3)
Cash4_max = max(Cash4)

Cash1_max_index = Cash1.index(Cash1_max) # индекс максимального значения для первой кассы
Cash2_max_index = Cash2.index(Cash2_max)
Cash3_max_index = Cash3.index(Cash3_max)
Cash4_max_index = Cash4.index(Cash4_max)

Max_cash = (Cash1_max, Cash2_max, Cash3_max, Cash4_max) # список максимальных значений среди всех касс
Max_cash_index = (Cash1_max_index, Cash2_max_index, Cash3_max_index, Cash4_max_index) # список индексов максимальных значений среди всех касс

Max_Max_cash = max(Max_cash) # максимальное значение среди всех касс
Max_Max_cash_index = Max_cash.index(Max_Max_cash) # индекс максимального значения среди всех касс

Max_interval = Max_cash_index[Max_Max_cash_index] # максимальный интервал - 1
final_Max_interval = Max_interval + 1 # максимальный интервал

print(final_Max_interval)



