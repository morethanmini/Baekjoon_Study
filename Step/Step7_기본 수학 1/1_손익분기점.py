A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))

"""
A : 고정비용
B : 노트북 단가
X : 노트북 개수
총 생산 비용 : A + (B * X)

C : 노트북 가격
총 수입 : C * X

Q. 총 수입이 총 생산 비용보다 커지는 금액
"""