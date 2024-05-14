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
명목GDP = [0 for _ in range(len(물가정보))]
실질GDP = [0 for _ in range(len(물가정보))]
경제성장률 = [0 for _ in range(len(물가정보))]
startYear = 물가정보[0][0]

print(*list(map(lambda x:str(x[0]) + '년', 물가정보)), sep="\t")

# 명목GDP 구하기
for 연도,항목,금액 in 거래정보:
  if 항목 == "수입":
    명목GDP[연도 - startYear] -= 금액
  else:
    명목GDP[연도 - startYear] += 금액
print(*명목GDP, sep="\t")

# 실질GDP 구하기
for 연도,물가지수 in 물가정보:
  실질GDP[연도 - startYear] = int(명목GDP[연도 - startYear] * 물가지수)
print(*실질GDP, sep="\t")

# 경제성장률 구하기
for 연도,물가지수 in 물가정보:
  if 연도 == startYear:
    continue
  temp = ((실질GDP[연도 - startYear] - 실질GDP[연도 - startYear - 1]) / 실질GDP[연도 - startYear]) * 100
  경제성장률[연도 - startYear] = int(temp * 10) / 10
print(*경제성장률, sep="\t")