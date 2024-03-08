import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data['type'] = 1 #Создаем новый столбец 'type' в DataFrame data и заполняем го значениями 1.
data.set_index([data.index, 'whoAmI'], inplace=True) # Устанавливаем составной индекс DataFrame: основной индекс и столбец 'whoAmI'.
data = data.unstack(level=-1, fill_value = 0)# Разворачиваем уровень столбца 'whoAmI' в индекс, заполняя отсутствующие значения нулями
data.columns = data.columns.droplevel()  #Убираем уровень заголовков столбцов
data.columns.name = '№' #Устанавливаем № в качестве имени столбцов DataFrame data
print(data)