import numpy as np

def ref(A):
    A = np.array(A, dtype=float)

    rows, cols = A.shape

    # 각 행을 순차적으로 처리하기 위한 설정, 0부터 'rows-1'까지 생성 (0은 생략가능)
    for i in range(rows):

    # 피벗(=선도1) 요소 초기화, 아직 피벗이 선택되지 않음을 의미, 어떤 다른 문자를 이용해도 상관은 없다.
      pivot = None

    # 각 행을 순차적으로 처리하여 pivot 결정
      for j in range(i, rows):
        if A[j, i] != 0:
          pivot = j
          break

    # 피벗이 없으면 넘어간다.
      if pivot is None:
        continue

    # 기본행연산
      A[[i, pivot]] = A[[pivot, i]]
      A[i] = A[i] / A[i, i]
      for j in range(i+1, rows):
        A[j] = A[j] - A[j, i] * A[i]

    return(A)

def rref(A):
    # 행 사다리꼴 형태에서 기약 행 사다리꼴 형태로 변환
    A = ref(A)

    rows, cols = A.shape

    #1. rows-1부터 역순으로 순회
    for i in range(rows-1, -1, -1):

    #2. 각 행에서 열을 순차적으로 순회
        for j in range(cols):

    #3. i행에서 피벗 찾기
            if A[i, j] == 1:

    #4. i-1부터 역순으로 순회
                 for k in range(i-1, -1, -1):

    #5. k행을 기준으로 기본 행 연산
                    A[k] -= A[k, j] * A[i]
                 break
    return A