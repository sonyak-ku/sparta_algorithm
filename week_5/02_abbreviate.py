import heapq
input = "abcabcabcabcdededededede"


def string_compression(string):
    compressed_len = []
    leng = len(string)
    #압축의 길이는 최대 절반일 것
    for i in range(1, leng//2 + 1):
        # print(i)
        start = 0
        count = 1  # 중복되는 숫자 체크용
        ex_ = ''  # 첫 값을 집어넣을 공간
        comp_ = ''  # 완성된 문장들
        for _ in range(leng // i):  # 전체 스트링에서 놀아야 하지 않을까?
            lost_first = False
            end = start + i
            word = string[start:end]  # 주어진 숫자에 따라 마디마디로 끊기 위함
            start = end
            # print(word)
            if ex_ == '':  # 비교를 위한 첫 값을 넣을 공간이 비었을때 , 맨 처음 스타트용!
                ex_ = word  # 처음 자른값이 안에 들어가게끔
                if ex_ != string[end:end + i]:  # 맨 처음에만 중복이 이루어지지 않기 때문에 뒤에서 맨 처음값을 놓칠 거라는 경고
                    lost_first = True
                continue  # continue 아래의 코드들을 멈추고 다음 반복을 시작해랴! / break 반복문을 깨뜨려라

            if word == ex_:  # 이전의 값과 같을때 (중복될때)
                count += 1
                if _ == leng // i - 1:  # 중복되다가 끝났을때의 경우 체크
                    comp_ += str(count)
                    comp_ += ex_
                    # print('roop_while_duplicate :', comp_)
            else:  # 중복되지 않을때
                if count != 1:  # 중복되다가 끊겼을때
                    comp_ += str(count)
                    comp_ += ex_  # 그 이전까지 중복되고 있었던 문자를 집어넣기용!
                    # print('comp is1:', comp_)
                    ex_ = word  # 초기화
                    count = 1
                    if _ == leng // i - 1:  # 중복되다가 끝났을때의 경우 체크
                        comp_ += word
                else:  # 중복되다가 끊긴경우가 아닐때, 계속 다른값이 나오고 있는 중일때
                    if lost_first:
                        comp_ += string[0:i]  # 맨 처음 값을 넣자.
                        lost_first = False
                    comp_ += ex_  # 뒤에서 중복될수가 있는데 현재값으로 처리하는거 자체가 문제가 있음 , 그렇기 때문에 뒤에서 이전값 처리.
                    # print('comp is2:', comp_)
                    ex_ = word
                    if _ == leng // i - 1:  # 중복되다가 끝났을때의 경우 체크
                        comp_ += word
        comp_ += string[end:]  # 마디마디로 나누어 지지 않는 꼬투리들 더하기
        # print('final comp:', comp_)  # 꼬리부분 더하는 코드 두줄
        heapq.heappush(compressed_len, len(comp_))
    return heapq.heappop(compressed_len) # 압축된 길이들 중 가장 짧은 길이를 리턴하도록


print(string_compression(input))  # 14 가 출력되어야 합니다!
#
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))

# k = 'zxxxksssvbnlaxb'
# len_k = len(k)
# for i in range(1, len_k//2 + 1):
#     print(i)
#     start = 0
#     count = 1 #중복되는 숫자 체크용
#     ex_ = '' #첫 값을 집어넣을 공간
#     comp_ = '' #완성된 문장들
#     for _ in range(len_k//i): #전체 스트링에서 놀아야 하지 않을까?
#         lost_first = False
#         end = start + i
#         word = k[start:end] #주어진 숫자에 따라 마디마디로 끊기 위함
#         start = end
#         print(word)
#         if ex_ == '': #비교를 위한 첫 값을 넣을 공간이 비었을때 , 맨 처음 스타트용!
#             ex_ = word   # 처음 자른값이 안에 들어가게끔
#             if ex_ != k[end:end+i]: #맨 처음에만 중복이 이루어지지 않기 때문에 뒤에서 맨 처음값을 놓칠 거라는 경고
#                 lost_first = True
#             continue  # continue 아래의 코드들을 멈추고 다음 반복을 시작해랴! / break 반복문을 깨뜨려라
#
#         if word == ex_: #이전의 값과 같을때 (중복될때)
#             count += 1
#             if _ == len_k//i - 1: #중복되다가 끝났을때의 경우 체크
#                 comp_ += str(count)
#                 comp_ += ex_
#                 print('roop_while_duplicate :', comp_)
#         else: #중복되지 않을때
#             if count != 1: #중복되다가 끊겼을때
#                 comp_ += str(count)
#                 comp_ += ex_  # 그 이전까지 중복되고 있었던 문자를 집어넣기용!
#                 print('comp is1:',comp_)
#                 ex_ = word # 초기화
#                 count = 1
#                 if _ == len_k // i - 1:  # 중복되다가 끝났을때의 경우 체크
#                     comp_ += word
#             else: #중복되다가 끊긴경우가 아닐때, 계속 다른값이 나오고 있는 중일때
#                 if lost_first:
#                     comp_ += k[0:i] #맨 처음 값을 넣자.
#                     lost_first = False
#                 comp_ += ex_  #뒤에서 중복될수가 있는데 현재값으로 처리하는거 자체가 문제가 있음 , 그렇기 때문에 뒤에서 이전값 처리.
#                 print('comp is2:', comp_)
#                 ex_ = word
#                 if _ == len_k // i - 1:  # 중복되다가 끝났을때의 경우 체크
#                     comp_ += word
#     comp_ += k[end:] # 마디마디로 나누어 지지 않는 꼬투리들 더하기
#     print('final comp:', comp_)  # 꼬리부분 더하는 코드 두줄
#
#맨 앞에꺼 패쓰하는 문제 >> 맨 뒤에꺼 패스하는 문제 >> 해결을 위해, 현재꺼를 더하는 식으로 코드 짜야 될것.!!!, #맨 마지막에 남는 꼬리부분을 어디서 더할지 체크해야한다.
#맨 마지막에 남는 꼬리부분을 어디서 더할지 체크해야한다.
#####여기까지의 코드는 주어진 스트링을 1개씩부터, 2개씩 ... 절반의개수씩 잘라보는 코드임.