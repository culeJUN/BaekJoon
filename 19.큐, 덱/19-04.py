case = int(input())
for i in range(case) :
    N, M = map(int, input().split())            # 프린트 개수, 몇번째가 궁금해?
    paper = list(map(int, input().split()))     # 프린트 리스트
    order = list(range(len(paper)))             # n번째 저장 리스트
    order[M] = '?'                              # 중요도 중에 M번째가 궁금하니까 '?'로 바꿈
    grade = 0

    while True :
        if paper[0] == max(paper) :                 # 프린트의 맨 앞이 제일 중요한거라면
            grade += 1                              # 프린트와 동시에 순서 + 1
            if order[0] == '?' :                        # 근데 심지어 그게 궁금했던 순서라면
                print(grade)                                # 순서 프린트
                break
            else :                                      # 궁금한거 아니면 
                paper.pop(0)                                # 프린트 된거 삭제
                order.pop(0)                                # 프린트 된거 삭제
        else :                                      # 더 중요한게 있다면
            paper.append(paper.pop(0))                  # 프린트 마지막 순번으로 교체
            order.append(order.pop(0))                  # n번째 저장 순서 마지막으로 교체