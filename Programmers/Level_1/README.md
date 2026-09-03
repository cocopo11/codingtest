# Programmers Level 1

프로그래머스 Level 1 문제 풀이 기록 정리

---

## 1. 제일 작은 수 제거하기

### 문제 접근

배열에서 가장 작은 값만 제거하고 나머지 배열을 반환해야 함

처음에는 배열을 `sort()`로 정렬한 뒤 첫 번째 원소를 제거하는 방법을 생각했지만 배열을 통째로 정렬할 필요가 없고 최솟값 하나만 찾으면 되므로, `O(n log n)`의 시간복잡도를 가지는 정렬보다 `min()`을 이용해 최솟값을 찾는 방법을 사용했음

`min(arr)`로 최솟값을 구하고 `arr.index()`를 이용해 해당 값의 인덱스를 찾은 뒤 `del`로 제거함

제거한 뒤 arr을 return하고 배열이 비어 있으면 문제 조건에 따라 `[-1]`을 return함

### Code

```python
def solution(arr):
    a = min(arr)
    del arr[arr.index(a)]

    if len(arr) == 0:
        return [-1]

    return arr
```

### 시간복잡도

`min(arr)` -> 배열 전체를 탐색하므로 `O(n)`

`arr.index(a)` -> 최솟값 위치를 찾기 위해 최대 `O(n)`이 필요

`del` -> 리스트에서 원소를 삭제할 때 뒤쪽 원소들을 이동시킬 수 있으므로 최악의 경우 `O(n)`

따라서 전체 시간복잡도는

```text
O(n)
```

### 배운 점

최솟값 하나만 필요한 경우 배열 전체를 sort할 필요가 없다.

```text
sort(): O(n log n)
min():  O(n)
```

따라서 문제에서 실제로 필요한 연산이 무엇인지 먼저 생각하면 불필요한 정렬을 피할 수 있음.

---

## 2. 나누어 떨어지는 숫자 배열

### 문제 접근

배열의 원소 중 `divisor`로 나누어떨어지는 값만 선택해야 함

리스트 컴프리헨션을 이용해

```python
i % divisor == 0
```

조건을 만족하는 원소만 새로운 리스트에 저장했다.

결과를 오름차순으로 반환해야 하므로 `sorted()`를 사용함

조건을 만족하는 원소가 하나도 없으면 `answer`는 빈 리스트가 된다. 

Python에서 빈 리스트는 false로 취급되는 것을 응용해서 or를 써서 한 줄로 작성했다.

```python
sorted(answer) or [-1]
```

`sorted(answer)`가 빈 리스트라면 `or` 뒤의 `[-1]`이 return되고, 원소가 존재한다면 정렬된 리스트가 그대로 반환된다.

### Code

```python
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return sorted(answer) or [-1]
```

### 시간복잡도

배열의 길이를 `n`, 조건을 만족하는 원소의 개수를 `k`라고 하면 배열을 한 번 탐색하므로

```text
O(n)
```

이 필요하다.

선택된 `k`개의 원소만 정렬하므로

```text
O(k log k)
```

가 필요하다.

따라서 전체 시간복잡도는

```text
O(n + k log k)
```

이다.

최악의 경우 모든 원소가 조건을 만족하면 `k = n`이므로

```text
O(n log n)
```

이 된다.

### 배운 점

또한 Python의 true / false 특성을 활용하면

```python
if len(answer) == 0:
    return [-1]
```

로 썼을 if문을

```python
answer or [-1]
```

형태로 짧게 표현할 수 있다.

## 3. 같은 숫자는 싫어

### 문제 접근

처음에는 빈 리스트 `answer`를 만들고 `arr`를 순회하면서, 이미 `answer`에 존재하는 원소라면 건너뛰는 방법을 생각했다.

하지만 이 문제는 단순히 중복된 원소 전체를 제거하는 것이 아니라 같은 숫자가 연속해서 나타나는 경우에만 제거해야 한다.

따라서 첫 번째 원소 `arr[0]`을 미리 `answer`에 넣고, 두 번째 원소부터 순회하도록 구현했다.

현재 원소 `arr[i]`와 `answer`의 마지막 원소 `answer[-1]`을 비교한다.

두 값이 같다면 직전에 결과에 추가된 숫자와 연속된 것이므로 건너뛰고, 다르다면 `answer`에 추가한다.

### Code

```python
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] == answer[-1]:
            continue
        answer.append(arr[i])
    return answer
```

### 시간복잡도

배열의 길이를 `n`이라고 하면 `for`문에서 배열을 한 번 순회한다.

`append()`는 평균적으로 `O(1)`이므로 전체 시간복잡도는 `O(n)`

### 배운 점 

단순히 중복된 값인지 확인하는 것과 연속된 중복을 확인하는 것은 다르다.

문제의 조건을 정확하게 파악하고, 현재 값과 직전에 결과에 추가한 값을 비교하면 한 번의 순회만으로 연속된 중복을 제거할 수 있다.

## 4. 없는 숫자 더하기

### 문제 접근

`numbers`에 없는 숫자를 굳이 하나하나 찾아서 직접 더할 필요가 없는 문제.

0부터 9까지의 합은 항상 45이고, 문제 조건에 따라 `numbers`의 원소에는 중복이 없다.

따라서

`0부터 9까지의 합 = numbers에 존재하는 숫자의 합 + 존재하지 않는 숫자의 합`

이라는 관계를 이용할 수 있다.

즉, 45에서 `numbers`의 모든 원소의 합을 빼면 존재하지 않는 숫자들의 합을 한번에 구할 수 있다.

### Code

```python
def solution(numbers):
    return 45 - sum(numbers)
```

### 시간복잡도

`sum(numbers)`가 리스트의 모든 원소를 한 번씩 확인하므로 `O(n)`이다.

빼기 연산은 `O(1)`이므로 전체 시간복잡도는 `O(n)`

### 배운 점

문제에서 요구하는 값을 직접 찾는 대신, 전체 합에서 이미 존재하는 값들의 합을 빼는 방식으로 문제를 단순화할 수 있다.

## 5. 행렬의 덧셈

### 문제 접근

두 행렬의 같은 위치에 있는 원소끼리 더하면 되므로 이중 `for`문을 사용해 각 행과 열의 인덱스에 직접 접근했다.

먼저 결과를 저장하기 위해 `arr1`과 동일한 크기를 가지며 모든 원소가 0인 `answer` 행렬을 생성했다.

그 후 행을 나타내는 `i`와 열을 나타내는 `j`를 이용해 각 위치에 접근하고,

`arr1[i][j] + arr2[i][j]`

의 결과를 `answer[i][j]`에 저장했다.

### Code

```python
def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr1[i]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
```

### 시간복잡도

행의 개수를 `M`, 열의 개수를 `N`이라고 하면 `answer` 행렬을 생성하는 데 `O(MN)`이 필요하다.

이후 모든 행과 열을 순회하면서 덧셈을 수행하는 데 다시 `O(MN)`이 필요하다.

따라서 전체 시간복잡도는 `O(MN)`

### 배운 점

2차원 리스트는 이중 반복문을 사용해 `행 → 열` 순서로 순회할 수 있으며, `arr[i][j]`를 이용하면 특정 행과 열의 원소에 직접 접근할 수 있다.
