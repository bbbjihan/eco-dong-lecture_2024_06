import random
import math
import os

pathA = './물가정보.txt'
pathB = './거래정보.txt'
mode = 'w'

GENERATE_COUNT = 10000

NATION_CASES = ['a']
DETAIL_CASES = ['소비','투자','정부구입','수입','수출']
YEAR_CASES = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
AMOUNT_RANGE = [50, 200]
PRICE_RANGE = [0.5, 1.5]

def getAccumulatedProb(count):
  return [ ((i + 1) / count) for i in range(count) ]

def getRandomIndex(accumulatedProb):
  rand = random.random()
  
  for i in range(len(accumulatedProb)):
    if rand < accumulatedProb[i]:
      return i
  
  return len(accumulatedProb) - 1

def generateNewTradeData(count):
  probNation = getAccumulatedProb(len(NATION_CASES))
  probDetail = getAccumulatedProb(len(DETAIL_CASES))
  probYear = getAccumulatedProb(len(YEAR_CASES))
  amountStart, amountEnd = AMOUNT_RANGE
  probAmount = getAccumulatedProb(amountEnd - amountStart + 1)

  results = []

  for _ in range(count):
    randNation = NATION_CASES[getRandomIndex(probNation)]
    randDetail = DETAIL_CASES[getRandomIndex(probDetail)]
    randYear = YEAR_CASES[getRandomIndex(probYear)]
    randAmount = AMOUNT_RANGE[0] + getRandomIndex(probAmount)
    row = [randYear, randDetail, randAmount]
    results.append(row)

  with open(pathB, mode) as file:
    file.write('\n'.join(list(map(lambda x: ','.join(list(map(str, x))), results))))

def generateNewPriceData():
  priceStart, priceEnd = PRICE_RANGE
  probPrice = getAccumulatedProb(math.ceil((priceEnd - priceStart) * 10) + 1)
  
  results = []
  
  for i in range(len(NATION_CASES)):
    for j in range(len(YEAR_CASES)):
      randPrice = 1.0 if j == 0 else int(PRICE_RANGE[0] * 10 + getRandomIndex(probPrice)) / 10
      nation = NATION_CASES[i]
      year = YEAR_CASES[j]
      row = [year, randPrice]
      results.append(row)
  
  with open(pathA, mode) as file:
    file.write('\n'.join(list(map(lambda x: ','.join(list(map(str, x))), results))))

def main():
  generateNewPriceData()
  # generateNewTradeData(GENERATE_COUNT)

if __name__ == "__main__":
	main()