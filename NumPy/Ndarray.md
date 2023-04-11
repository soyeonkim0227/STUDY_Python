# Ndarray

- NumPy의 N차원 배열 객체이다.
- 데이터 분석을 하기 위해 사용한다.
- Python의 list와 가장 큰 차이점은, **하나의 데이터 타입만 넣을 수 있다는 점이다.** (Python List는 Dynamic typing을 지원하지만, **ndarray는 지원하지 않는다.**)
- C의 Array와 동일하다고 이해하면 가장 쉽다.

# 2. int 타입의 ndarray 생성하기

```python
# a의 list를 int 타입의 ndarray로 생성하여 a_ndarray 변수에 담는다.
a = [1, 2, 3, 4, 5]
a_ndarray = np.array(a, int)
```

- **np.array 함수**는 기존의 리스트 형태의 데이터와 데이터 타입을 입력받아 ndarray 형태로 변환해주는 함수이다.

# 3. String 타입의 자동 형 변환

```python
# b[3]을 Float type으로 입력해도, ndarray는 하나의 타입만 가질 수 있다.
b = [1, 4, 5, '8']
b_ndarray = np.array(b, float)
print(b_ndarray) # 출력을 해서 확인할 수도 있고
type(b_ndarray[3]) # 직접 타입을 확인해도, float로 잘 변환된 것을 확인할 수 있다.
```

- 위에서 다뤘듯이 python list는 Dynamic typing이 가능하여 여러 데이터 타입이 존재할 수 있지만, ndarray는 하나의 타입만 존재할 수 있다.
- 그래서 List에 여러 데이터 타입이 존재하더라도 ndarray는 알아서 하나의 타입으로 형 변환을 수행한다.
- 위와 같이 string으로 입력하여도, 요청한 float형태로 자동 형 변환을 수행한다.
- print와 type 함수를 통해 원하는 type으로 잘 형 변환이 되었는지 확인할 수 있다.

# 4. shape과 dtype property 사용하는 방법

```python
c = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
c_ndarray = np.array(c, int)
c_ndarray.shape # (3,3)의 크기를 반환
c_ndarray.dtype # 해당 ndarray의 타입(int)을 반환
```

- **ndarray.shape**은 해당 ndarray의 크기를 반환
- **ndarray.dtype**은 해당 ndarray의 데이터 타입을 반환

# 5. 3차원 배열의 shape, dtype, ndim, size property 사용하는 방법

```python
d = [[[1, 2, 5, 8], [1, 2, 5, 8], [1, 2, 5, 8]],
     [[1, 2, 5, 8], [1, 2, 5, 8], [1, 2, 5, 8]],
     [[1, 2, 5, 8], [1, 2, 5, 8], [1, 2, 5, 8]],
     [[1, 2, 5, 8], [1, 2, 5, 8], [1, 2, 5, 8]]]  # 4x3x4 3차원 배열 선언
d_ndarray = np.array(d, int)
print(d_ndarray.shape) # 3rd order tensor
print(d_ndarray.ndim) # number of dimensions
print(d_ndarray.size) # 48 == 4x3x4

d_ndarray = np.array(d, dtype=np.int8) # 기본은 int32인데, 메모리 낭비가 커서 int8로 사용가능
print(d_ndarray.dtype) # int8 출력
```

- 위와 같이 4x3x4의 3차원 배열을 선언했을 때에도, shape/dtype은 동일하게 동작한다.
- **.shape**은 4x3x4를 반환한다.
- **.ndim**은 3(3차원의 의미)을 반환한다.
- **.size**는 배열의 크기인 48을 반환한다.
- 위와 같은 예제도 데이터가 많아서 복잡한데, 실제 데이터 분석을 위해 사용되는 데이터는 훨씬 방대하다.
- 그렇기 때문에 데이터의 상/하한 값을 안다면, 그에 맞춰 **dtype을 np.int8과 같이 줄여서 메모리 낭비를 줄일 수 있다.**

# 6. nbytes로 데이터의 Byte 크기 추출하기

```python
# 소수점까지 있어야 정확한 Y값 예측이 가능해져서 대부분의 경우 float를 사용함.
d_ndarray = np.array(d, dtype=np.float32)
print(d_ndarray.nbytes) # byte size를 출력함. 48개 x 4B == 192B 출력
```

- Machine Learning을 하며 Y값을 잘 예측하기 위해서는 float를 사용하여 소수점까지 정확하게 계산할 필요가 있다.
- 그래서 주로 float를 사용할 것이고, 이런 데이터의 **Byte 단위 크기**를 알고 싶다면 .**nbytes**를 사용하면 된다.
