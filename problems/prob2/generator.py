import random
import math
import os

filePath = './금융상품목록.txt'
mode = 'w'

ADJECTIVES = [ "행복한", "기쁜", "즐거운", "만족한", "신나는", "열광적인", "명랑한", "들뜬", "환희에 찬", "희망찬", "자신감 있는", "차분한", "편안한", "용감한", "대담한", "모험적인", "우아한", "고상한", "매력적인", "잘생긴", "매력적인", "똑똑한", "현명한", "영리한", "빛나는", "박식한", "친절한", "관대한", "동정심 있는", "동정적인", "친근한", "충실한", "성실한", "신뢰할 수 있는", "정직한", "진실한", "근면한", "성실한", "부지런한", "생산적인", "야심찬", "예의 바른", "공손한", "사려 깊은", "존경하는", "창의적인", "기발한", "상냥한", "자비로운", "온화한", "참을성 있는", "용서하는", "용기 있는", "열정적인", "성실한", "겸손한", "인내심 있는", "신뢰할 수 있는", "유머러스한", "낙천적인", "상냥한", "재능 있는", "독창적인", "헌신적인", "충성스러운", "용맹한", "사려 깊은", "성실한", "긍정적인", "활기찬", "열정적인", "적극적인", "공감하는", "인정 많은", "기운찬", "믿음직한", "열렬한", "기운찬", "자신감 있는", "생기 있는", "행운의", "활발한", "지혜로운", "믿을 만한", "깨끗한", "청결한", "정리된", "잘 정돈된", "효율적인", "체계적인", "신뢰성 있는", "유능한", "기술 좋은", "책임감 있는", "적응력 있는", "유연한", "협조적인", "팀워크 좋은", "매너 있는", "독립적인" ]
FOODS = [ "김치", "비빔밥", "불고기", "된장찌개", "삼겹살", "갈비찜", "잡채", "순두부찌개", "떡볶이", "해물파전", "김밥", "냉면", "설렁탕", "육개장", "감자탕", "닭갈비", "찜닭", "닭강정", "해물탕", "수제비", "라면", "콩나물국", "부대찌개", "쭈꾸미볶음", "골뱅이무침", "낙지볶음", "꼬막무침", "순대", "족발", "보쌈", "소불고기", "양념치킨", "후라이드치킨", "찜질방계란", "오징어볶음", "된장국", "콩비지찌개", "물냉면", "비빔냉면", "동치미", "동태찌개", "북엇국", "미역국", "육전", "갈비탕", "삼계탕", "생선구이", "새우튀김", "오뎅", "문어숙회", "전복죽", "육회", "곱창", "대창", "막창", "초밥", "참치회", "연어회", "회덮밥", "알밥", "우동", "덴푸라", "타코야키", "돈까스", "카레라이스", "오코노미야키", "야키소바", "라멘", "스키야키", "샤부샤부", "피자", "스파게티", "라자냐", "리조또", "파스타", "치즈버거", "핫도그", "프렌치프라이", "샌드위치", "토스트", "팟타이", "쌀국수", "카오팟", "반미", "솜땀", "마파두부", "딤섬", "탕수육", "깐풍기", "마라탕", "훠궈", "초밥", "우동", "덮밥", "타코", "브리또", "퀘사디아", "치즈나쵸", "칠리콘카르네", "파히타" ]
START_PRICE_RANGE = [1, 10000]
END_PRICE_RANGE = [7500, 20000]
randomNames = []

def getAccumulatedProb(count):
  return [ ((i + 1) / count) for i in range(count) ]

def getRandomIndex(accumulatedProb):
  rand = random.random()
  
  for i in range(len(accumulatedProb)):
    if rand < accumulatedProb[i]:
      return i
  
  return len(accumulatedProb) - 1

def generate():
  startPriceStart, startPriceEnd = START_PRICE_RANGE
  probStartPrice = getAccumulatedProb(startPriceEnd - startPriceStart + 1)
  endPriceStart, endPriceEnd = END_PRICE_RANGE
  probEndPrice = getAccumulatedProb(endPriceEnd - endPriceStart + 1)
  
  results = []
  
  for randName in randomNames:
    randStartPrice = START_PRICE_RANGE[0] + getRandomIndex(probStartPrice)
    randEndPrice = END_PRICE_RANGE[0] + getRandomIndex(probEndPrice)
    row = [randName, randStartPrice, randEndPrice]
    results.append(row)
  
  with open(filePath, mode) as file:
    file.write('\n'.join(list(map(lambda x: ','.join(list(map(str,x))), results))))

def main():
  for adj in ADJECTIVES:
    for food in FOODS:
      randomNames.append(adj + ' ' + food)
  random.shuffle(randomNames)
  
  generate()

if __name__ == "__main__":
  main()