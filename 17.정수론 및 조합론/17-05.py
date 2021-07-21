num=int(input())
num_list=[]
for i in range(num) :
    num_list.append(int(input()))

m = abs(num_list[0] - num_list[1])      # m = 맨 앞 두 수 뺀거
m_yak = [m]
for i in range(2,int(m ** 0.5) + 1) :   # 약수구하기
    if m % i==0 :
        m_yak.append(i)
        m_yak.append(m//i)
 
answer=[]
for i in range(len(m_yak)) :
    r = num_list[0] % m_yak[i]              # r = m의 약수로 나눈 나머지(모든 num을 m의 약수로 나눴을때 모두 r로 같아댜 됨)
    for j in range(1,len(num_list)) :       # 나머지 같은지 확인
        if r != num_list[j] % m_yak[i] :        # 나머지가 다르면 패스
            break
        if j == len(num_list) - 1 :             # 모든 나머지가 같으면 m추가
            answer.append(m_yak[i])
 
answer.sort()
for i in answer :
    print(i, end = ' ')