import pandas as pd
x1 = 79280.5; y1 = 1815.5; z1 = 7054.0;
x2 = 832714.5; y2 = 45810.5; z2 = 17868.0;
x3 = 486088.8; y3 = 32013.5; z3 = 37245.0;
x4 = 1665429.0; y4 = 91621.0; z4 = 35736.0;
x5 = 464588.0; y5 = 25584.0; z5 = 50913.0;
x6 = 2861819.0; y6 = 89378.0; z6 = 52783.0
x7 = 79280.5; y7 = 1815.5; z7 = 7054.0
x8 = 486088.8; y8 = 32013.0; z8 = 37245.0
x9 = 464588.0; y9 = 25584.0; z9 = 50913.0

code1 = "базовий"
code2 = "базовий"
code3 = "попередній"
code4 = "попередній"
code5 = "поточний"
code6 = "поточний"
code7 = "базовий"
code8 = "попередній"
code9 = "поточний"
column = pd.MultiIndex.from_product([['Назви столбів'],["a","b","c","d",]])
column = column.insert(0, ('Код підприємства'))
#column = column.insert(6, ('Awerage price'))

market_price = pd.DataFrame([['1','2','1','2','1','2','3','3','3'],
                              [code1, code2, code3, code4, code5, code6, code7, code8, code9],
                              [x1, x2, x3, x4, x5, x6, x7, x8, x9, ],
                              [y1, y2, y3, y4, y5, y6, y7, y8, y9, ],
                              [z1, z2, z3, z4, z5, z6, z7, z8, z9, ],
                              ], column).T

print(market_price)