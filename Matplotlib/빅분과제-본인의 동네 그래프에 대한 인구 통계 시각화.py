import csv
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/BigData/data-csv/202303_202303_연령별인구현황_월간.csv'
f = open(fr'{path}', encoding='cp949') #raw 표기법
data = csv.reader(f)
result=[]

city = input("사시는 동네 이름을 작성해주세요: ")
for row in data:
    if city in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',', '')))
print(result)

plt.plot(result)
ymax = max(result)
xpos = result.index(ymax)

plt.grid(True, axis='x', color='red', alpha=1)
plt.grid(True, axis='y', color='black', alpha=1, linestyle='--')

plt.style.use('classic')

plt.annotate(f'local max({xpos}age)', xy=(xpos, ymax), xytext=(70,430), arrowprops=dict(facecolor='yellow'))

plt.title('Population status by age', loc='center', pad=10)
plt.xlabel('Age', labelpad=10)
plt.ylabel('Population', labelpad=10)

plt.show()