# Programmers Level 2

프로그래머스 Level 2 문제 풀이 기록 정리

---

## 1. 올바른 괄호

### 문제 접근

괄호 문자열을 앞에서부터 순서대로 확인하면서 `(`와 `)`의 짝을 확인해야 한다.

`(`가 나오면 아직 짝이 맞지 않은 괄호이므로 스택에 추가한다.

반대로 `)`가 나오면 이전에 나온 `(`하나와 짝을 이루어야 하므로 스택에서 하나를 `pop()`한다.

만약 스택이 이미 비어 있는데 `pop()`을 시도한다면 현재 `)`와 짝을 이룰 `(`가 없다는 뜻이다.

따라서 `IndexError`가 발생하면 즉시 `False`를 반환한다.

문자열 순회가 끝난 뒤 스택이 비어 있다면 모든 괄호가 정확하게 짝지어진 것이므로 `True`를 반환한다.

반대로 스택에 `(`가 남아 있다면 `)`가 부족한 것이므로 `False`를 반환한다.

### Code

```python
def solution(s):
    answer = []

    for i in s:
        if i == "(":
            answer.append(i)
        else:
            try:
                answer.pop()
            except IndexError:
                return False

    return len(answer) == 0
```

### 시간복잡도

문자열 `s`의 길이를 `n`이라고 하면 모든 문자를 한 번씩 순회하므로 `O(n)`이다.

반복문 내부에서 수행되는 주요 연산은 다음과 같다.

* 괄호 비교: `O(1)`

* `append()`: `O(1)`

* `pop()` : `O(1)`

* `len(answer)`: `O(1)`

따라서 전체 시간복잡도는 `O(n)`

### 공간복잡도

최악의 경우 문자열이 모두 `(`로 이루어져 있다면 모든 괄호가 스택에 저장된다.

따라서 공간복잡도는 `O(n)`

### 배운 점

괄호의 짝처럼 최근에 들어온 값과 가장 먼저 대응해야 하는 구조에서는 스택을 활용할 수 있다.

또한 스택이 비어 있는 상태에서 `)`가 등장하는 경우와, 순회가 끝난 뒤에도 `(`가 남아 있는 경우를 각각 확인해야 한다.

---

## 2. 프로세스

### 문제 접근

처음에는 문제에 나온 운영체제의 프로세스 실행 방식을 대략적으로 구현하는 것부터 시작했다.

우선순위가 낮은 프로세스가 큐의 앞에 있더라도, 뒤에 더 높은 우선순위의 프로세스가 존재하면 해당 프로세스를 다시 큐의 뒤로 보내는 방식이다.

처음에는 다음과 같이 `deque`에 우선순위 값만 저장했다.

```python
from collections import deque

def solution(priorities, location):
    temp = deque(priorities)

    while len(temp) > 0:
        a = temp.popleft()

        for j in temp:
            if a < j:
                temp.append(a)
                break

        if len(temp) == 0:
            return 1
```

이렇게 프로세스의 동작 자체는 어느 정도 구현할 수 있었지만 두 가지 문제가 있었다.

첫 번째는 `for`문 안에서 `break`가 실행되어 프로세스를 다시 큐에 넣은 것인지 끝까지 순회를 마치고 실제로 프로세스가 실행된 것인지 구분하기 어렵다는 점이었다.

두 번째는 `popleft()`와 `append()`가 반복되면서 큐의 순서가 계속 바뀌기 때문에 각 프로세스가 원래 어디에 있었는지 알 수 없다는 점이었다.

이 상태로는 `location`에 해당하는 프로세스가 몇 번째로 실행되는지 알 수 없다.

그래서 실행된 프로세스의 개수를 저장하기 위한 `num` 변수를 추가하고, `for`문이 `break` 없이 끝까지 실행된 경우에만 `num`을 1씩 증가시키도록 했다.

이때 `for-else`를 사용했다.

```python
for i, v in temp:
    if b < v:
        temp.append((a, b))
        break
else:
    num += 1
```

`for-else`에서 `else`는 반복문이 `break` 없이 정상적으로 끝났을 때만 실행되니까 현재 프로세스가 실제로 실행된 경우를 구분하기에 적합했다.

또한 원래 위치 정보를 보존하기 위해

```python
deque(enumerate(priorities))
```

를 사용했다.

이렇게 하면 큐의 각 원소가

```text
(원래 인덱스, 우선순위)
```

형태의 튜플로 저장된다.

따라서 프로세스가 큐의 뒤로 이동한다고 해도 원래 위치 정보는 그대로 유지된다.

마지막으로 실제로 프로세스가 실행되는 순간, 해당 프로세스의 원래 인덱스가 `location`과 같다면 현재까지 실행된 횟수 `num`을 return하도록 했다.

### Code

```python
from collections import deque

def solution(priorities, location):
    temp = deque(enumerate(priorities))
    num = 0

    while len(temp) > 0:
        a, b = temp.popleft()

        for i, v in temp:
            if b < v:
                temp.append((a, b))
                break
        else:
            num += 1

            if a == location:
                return num
```

### 시간복잡도

먼저

```python
deque(enumerate(priorities))
```

를 생성하는 데 `n`개의 원소를 처리하므로 `O(n)`이 필요하다.

`popleft()`와 `append()`는 각각 `O(1)`이다.

하지만 각 프로세스를 꺼낼 때마다 현재 큐 안의 다른 프로세스들을 `for`문으로 확인한다.

최악의 경우 하나의 프로세스를 확인할 때 큐 전체를 순회할 수 있고, 이러한 과정이 여러 번 반복될 수 있으므로 전체 시간복잡도는

```text
O(n^2)
```

이다.

초기 큐 생성 비용 `O(n)`을 포함해도

```text
O(n) + O(n^2) = O(n^2)
```

이므로 최종 시간복잡도는 `O(n^2)`

### 공간복잡도

`enumerate(priorities)`의 결과를 `deque`에 저장하므로 최대 `n`개의

```text
(인덱스, 우선순위)
```

튜플을 저장한다.

따라서 공간복잡도는

```text
O(n)
```

이다.

### 배운 점

이번 문제에서는 단순히 값만 큐에 저장하면 원래 위치를 추적할 수 없기 때문에, `enumerate()`를 사용해 인덱스와 값을 함께 저장하는 방법을 연습했다.

또한 반복문이 `break` 없이 끝났는지를 구분해야 하는 상황에서 `for-else`를 사용할 수 있다는 걸 배웠다.

그리고 `deque`의 `popleft()`와 `append()`를 사용하면 프로세스를 앞에서 꺼내고 뒤로 보내는 `FIFO`규칙을 구현할 수 있다.

---

## 3. 의상

### 문제 접근

먼저 `clothes`의 각 원소를 옷 종류별로 분류하고,
각 종류마다 몇 개의 옷이 있는지 딕셔너리에 저장했다.

```python
for name, kind in clothes:
    count[kind] = count.get(kind, 0) + 1
```

이렇게 하면 `count`의 value에는 각 옷 종류별 개수가 저장된다.

이후 각 종류에서 선택할 수 있는 경우의 수를 계산해야 한다.

어떤 종류의 옷이 `i`개 있다면 해당 종류에서는

- i개의 옷 중 하나를 선택하는 경우
- 아예 입지 않는 경우

가 있으므로 총 `i + 1`개의 선택지가 존재한다.

따라서 모든 종류의 선택지를 곱하면 전체 조합의 수를 구할 수 있다.

```python
for i in count.values():
    answer *= i + 1
```

이때 아무것도 입지 않는 경우는 존재하면 안되니까 최종적으로 answer - 1을 한 값을 리턴한다. 

### Code

```python
def solution(clothes):
    count = {}
    answer = 1

    for name, kind in clothes:
        count[kind] = count.get(kind, 0) + 1

    for i in count.values():
        answer *= i + 1

    return answer - 1
```

### 시간복잡도

`clothes`의 길이를 `n`, 옷 종류의 개수를 `k`라고 할때, `clothes`를 한 번 순회하면서 각 종류의 개수를 딕셔너리에 저장하므로 `O(n)`이 필요하다.

그 다음 `count.values()`를 순회하면서 각 종류별 경우의 수를 곱한다.
이 과정은 옷 종류의 개수만큼 반복되므로 `O(k)`이다.

`k <= n`이므로 전체 시간복잡도는 `O(n + k) = O(n)`

### 공간복잡도

옷 종류별 개수를 저장하는 딕셔너리는 최대 `k`개의 key를 가지므로
공간복잡도는 `O(k)`

최악의 경우 모든 옷의 종류가 서로 다를 때 `k = n`이므로 `O(n)`이다.

### 배운 점

이 문제에서는 실제 옷 조합을 하나씩 만들어 볼 필요 없이,
각 종류에서 가능한 선택지의 수를 곱하는 방식으로 전체 경우의 수를 구할 수 있었다.

문제의 접근법을 생각하는 것보다 마지막에 `answer` 구하는 공식을 구하는 게 더 오래 걸렸던 문제. 수학을 모른다면 더 오래 걸릴 것 같다.

어떤 종류의 옷이 `i`개 있다면 `i`개의 옷 중 하나를 고르는 경우뿐 아니라
아예 입지 않는 경우까지 포함해 `i + 1`가지 선택지가 존재한다.

모든 종류의 선택지를 곱한 뒤 아무것도 입지 않는 경우 한 가지를 빼면
정답을 구할 수 있다.
