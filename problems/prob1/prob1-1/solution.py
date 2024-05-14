import os

A_path = './물가정보.txt'
B_path = './거래정보.txt'
mode = 'r'

# 입력 전처리
물가정보 = []
거래정보 = []
with open(A_path, mode) as fileA:
  streamA = fileA.readline()
  while streamA:
    streamArray = streamA.strip().split(',')
    물가정보.append([int(streamArray[0]), float(streamArray[1])])
    streamA = fileA.readline()
with open(B_path, mode) as fileB:
  streamB = fileB.readline()
  while streamB:
    streamArray = streamB.strip().split(',')
    거래정보.append([int(streamArray[0]), streamArray[1], int(streamArray[2])])
    streamB = fileB.readline()

# 선언
명목GDP = [0, 0, 0]
실질GDP = [0, 0, 0]
경제성장률 = [0, 0, 0]

# 명목GDP 구하기
for 연도,항목,금액 in 거래정보:
  if 항목 == "수입":
    명목GDP[연도 - 2021] -= 금액
  else:
    명목GDP[연도 - 2021] += 금액
print(*명목GDP)
# 302 318 286

# 실질GDP 구하기
for 연도,물가지수 in 물가정보:
  실질GDP[연도 - 2021] = 명목GDP[연도 - 2021] * 물가지수
print(*실질GDP)
# 302.0 286.2 314.6

# 경제성장률 구하기
for 연도,물가지수 in 물가정보:
  if 연도 == 2021:
    continue
  경제성장률[연도 - 2021] = ((실질GDP[연도 - 2022] - 실질GDP[연도 - 2021]) / 실질GDP[연도 - 2022]) * 100
print(*경제성장률)
# 0 5.231788079470203 -9.923130677847672