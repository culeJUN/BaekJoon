N, M = map(int, input().split())  
result = []                             # 출력할 값 저장 ex) [1 2]
visitied = [False]*(N+1)                # True, False로 값 사용 유무 확인 ex) [1 1] 방지

def dfs(depth):                   # depth는 몇번째 수를 저장할 것인가를 저장
    if depth == M+1:                        # 값을 M개 저장 했으면 result에 저장된 수 출력
        for i in range(0,len(result)):      
            print(result[i],end=" ")
        print()
        return
    for num in range(1,N+1):                # 1부터 N까지 num 증가
        if not visitied[num]:                   # 만약 num번째 수가 False라면(사용 안했으면)
            #visitied[num] = True                    # 사용했다 표시하고
            result.append(num)                      # 그 값을 result에 입력
            dfs(depth+1)                            # 다음 차례로 올 수 를 검색
            #visitied[num] = False                   # 검색하고 왔으면 이제 그 숫자 False로 변경
            result.pop()                            # 그 수를 result에서 빼내줌

dfs(1)