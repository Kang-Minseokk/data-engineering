
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x = [1,2,3]
y = [2,4,8]

plt.plot(x,y)
plt.title("꺾은선 그래프")
plt.show()

import pandas as pd
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)
df

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

plt.bar(df['영화'], df['평점'])

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('국내 Top 8 영화 평점 정보')
plt.xticks(rotation=90)
plt.xlabel('영화')
plt.ylabel('평점')
plt.bar(df['영화'], df['평점'])


import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

# plt.title('국내 Top 8 영화 평점 정보')
# plt.xticks(rotation=90)
# plt.xlabel('영화')
# plt.ylabel('평점')
# plt.bar(df['영화'], df['평점'])

df_group = df.groupby('개봉 연도').mean()
df_group

plt.plot(df_group.index, df_group['평점'], marker='o')
plt.xticks(np.arange(2005, 2025, 5))
plt.yticks(np.arange(7.0, 10.0, 0.5))



import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

filt = df['평점']>=9.0
values = [len(df[filt]), len(df[~filt])]
labels = ['9점 이상', '9점 미만']

plt.pie(values, labels=labels, autopct="%.1f%%")
plt.legend(loc=(1, 0.3))
plt.show()

