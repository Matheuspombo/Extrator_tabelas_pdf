import tabula
import numpy as np
import pandas as pd
import openpyxl
df1 = tabula.read_pdf("Tabela de precos_SoulBrasil.pdf", pages="1", multiple_tables=True)

df = pd.DataFrame(np.concatenate(df1))
y = np.shape (df)
x = type (df)
df.to_excel('TabelaSoulBrasil.xlsx')
#print(df1)
print(x)
print(y)
#df2= pd.DataFrame(df1)



#table[0]
#print(df1)

#print(5)

