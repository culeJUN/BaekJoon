# https://atgane.github.io/%EB%B0%B1%EC%A4%80/%EC%8A%A4%ED%83%9D/2021/02/10/%EB%B0%B1%EC%A4%80-6549-%ED%8C%8C%EC%9D%B4%EC%8D%AC.html

while True :
    graph = list(map(int, input().split()))         # 층이 순서대로 저장
    if graph[0] == 0 :                              # 0이면 끝
        break
    graph.append(0)                                 # graph 맨 뒤에 0
    answer = 0                                      # 답을 저장
    stack = [[0, 0]]                                # 칸, 층 을 저장 시작은 0, 0
    for i in range(1, graph[0] + 2) :               # 1부터 맨 마지막에 저장한 0까지 for문
        while stack[-1][1] > graph[i] :                 # stack 마지막 높이가 graph 높이보다 크면 넓이 구하기 (그래프가 감소하는 순간)
            tmp_list = stack.pop()                          # tmp_list에 stack pop 저장
            tmp_area = 0
            while stack[-1][1] == tmp_list[1] :             # pop 하고나서도 높이가 같은면 그 마저도 pop(i - stack 마지막)
                stack.pop()
            tmp_area = max((i - 1 - stack[-1][0]) * tmp_list[1],    # (높이 같은거 고려해준)밑변 X 높이
                            (i - tmp_list[0]) * tmp_list[1])        # (그냥 지금 칸까지의)밑변 X 높이
            if tmp_area > answer :                          # tmp_area가 answer보다 크면 교체
                answer = tmp_area
        stack.append([i, graph[i]])                 # stack 마지막 높이가 graph보다 작으면 새로 stack에 저장
    print(answer)