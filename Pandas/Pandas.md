## 판다스(Pandas)

---

- 파이썬 처리를 위한 라이브러리
- 파이썬을 이용한 데이터 분석과 같은 작업에서 필수 라이브러리로 알려져있음.
- Pandas의 경우 pd라는 명칭으로 임포트하는 것이 관례임.

```python
import pandas as pd
```

- Pandas는 총 세 가지의 데이터 구조를 사용함.
  - 시리즈(Series)
  - **데이터 프레임(DataFrame)** - 가장 많이 사용됨.
  - 패널(Panel)

### 비교

| Python | NumPy   | Pandas |
| ------ | ------- | ------ |
| list   | ndarray | Series |

## 시리즈(Series)

---

- 시리즈 클래스는 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 구조를 갖고 있음.

```python
sr = pd.Series([17000, 18000, 1000, 5000],
								index=["피자", "치킨", "콜라", "맥주"])
print('시리즈 출력: ')
print('-'*15)
print(sr)
```

```python
시리즈 출력:
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
피자    17000
치킨    18000
콜라    1000
맥주    5000
dtype: int64
```

- 값(values)과 인덱스(index)를 출력함.

```python
print('시리즈의 값: {}'.format(sr.values))
print('시리즈의 인덱스: {}'.format(sr.index))
```

```python
시리즈의 값: [17000, 18000, 1000, 5000]
시리즈의 인덱스: Index(['피자', '치킨', '콜라', '맥주'], dtype='object')
```

## 데이터 프레임(DataFrame)

---

- 2차원 리스트를 매개변수로 전달함.
- 2차원이므로 행방향 인덱스(index)와 열방향 인덱스(column)가 존재함.
- 다시 말해, 행과 열을 가지는 자료구조임.
- 시리즈가 인덱스(index)와 값(values)으로 구성된다면, 데이터 프레임은 열(column)까지 추가되어 열(column), 인덱스(index), 값(value)으로 구성됨.
- DataFrame의 **head, info, describe 사용**

```python
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)

print('데이터프레임 출력: ')
print('-'*18)
print(df)
```

```python
데이터프레임 출력:
------------------
       A B C
one    1 2 3
two    4 5 6
three  7 8 9
```

## 데이터 프레임의 생성

---

- 데이터프레임은 리스트(List), 시리즈(Series), 딕셔너리(dict), Numpy의 ndarrays, 또 다른 데이터프레임으로부터 생성할 수 있음.
- 리스트와 딕셔너리를 사용하여 데이터 프레임을 생성해보자.

### 이중 리스트로 데이터 프레임 생성

```python
# 리스트로 생성하기
data = [
		['1000', 'Steve', 90.72],
		['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

df = pd.DataFrame(data)
print(df)
```

```python
			0         1      2
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

- 생성된 데이터 프레임에 열(columns)을 지정해줄 수 있음.

```python
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)
```

```python
		학번        이름     점수
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

### 딕셔너리(dictionary)를 통해 데이터 프레임을 생성

```python
# 딕셔너리로 생성하기
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

df = pd.DataFrame(data)
print(df)
```

```python
		학번        이름     점수
0  1000     Steve  90.72
1  1001     James  78.09
2  1002    Doyeon  98.43
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

## 데이터 프레임 조회하기

---

### 데이터 프레임에서 원하는 구간만 확인하기 위한 명령어

- df.head(n) - 앞 부분을 n개만 보기
- df.tail(n) - 뒷 부분을 n개만 보기
- df[’열이름’] - 해당되는 열을 확인

```python
# 앞 부분을 3개만 보기
print(df.head(3))
```

```python
		학번      이름     점수
0  1000   Steve  90.72
1  1001   James  78.09
2  1002  Doyeon  98.43
```

```python
# 뒷 부분을 3개만 보기
print(df.tail(3))
```

```python
학번        이름     점수
3  1003      Jane  64.19
4  1004  Pilwoong  81.30
5  1005      Tony  99.14
```

```python
# '학번'에 해당되는 열을 보기
print(df['학번'])
```

```python
0    1000
1    1001
2    1002
3    1003
4    1004
5    1005
Name: 학번, dtype: object
```

## 외부 데이터 읽기

---

- Pandas는 CSV, 텍스트, Excel, SQL, HTML, JSON 등 다양한 데이터 파일을 읽고 데이터 프레임을 생성할 수 있음.
- 예를 들어, csv 파일을 읽을 때는 **pandas.read_csv()**를 통해 읽을 수 있음.
- 다음과 같은 example.csv 파일이 있다고 가정

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0b44ec3-5099-416d-b13c-23228cfad66b/Untitled.png)

```python
df = pd.read_csv('example.csv')
print(df)
```

```python
   student id      name  score
0        1000     Steve  90.72
1        1001     James  78.09
2        1002    Doyeon  98.43
3        1003      Jane  64.19
4        1004  Pilwoong  81.30
5        1005      Tony  99.14
```

- 이 경우 인덱스가 자동으로 부여됨.

```python
print(df.index)
```

```python
RangeIndex(start=0, stop=6, step=1)
```

## 표기법

---

- dot notation
- bracket notation

```python
# dot notation
df.col_name

# bracket notation
df['col_name']
```

- 둘 중 아무거나 써도 상관없음.

## iloc과 loc

---

iloc - integer 뒤에거에서 숫자를 감소 [ : -1]

loc - 그대로 [ ] [ ]
