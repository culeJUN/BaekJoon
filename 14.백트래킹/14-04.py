N, M = map(int, input().split())  
result = []                                 # 출력할 값 저장
def dfs(depth, start):                      # depth는 몇번째 수를 저장할 것인가를 저장
    if depth == M+1:                            # 값을 M개 저장 했으면 result에 저장된 수 출력
        for i in range(0,len(result)):      
            print(result[i],end=" ")
        print()
        return
    for num in range(start,N+1):                # 1부터 N까지 num 증가
        result.append(num)                      # 그 값을 result에 입력
        dfs(depth + 1, num)                     # 다음 차례로 올 수 를 검색
        result.pop()                            # 그 수를 result에서 빼내줌

dfs(1, 1)