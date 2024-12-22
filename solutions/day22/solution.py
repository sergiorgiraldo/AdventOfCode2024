# puzzle prompt: https://adventofcode.com/2024/day/22

import sys
import time

sys.path.insert(0,"..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 22
    
    _is_debugging = False

    def CalcAndMixAndPrune(self, secret): #recipe from the puzzle
        next_secret = secret

        x = next_secret * 64
        next_secret ^= x
        next_secret %= 16777216

        x = next_secret // 32
        next_secret ^= x
        next_secret %= 16777216

        x = next_secret * 2048
        next_secret ^= x
        next_secret %= 16777216

        return next_secret

    def GetNthSecret(self, secret, n):
        for _ in range(n):
            secret = self.CalcAndMixAndPrune(secret)

        return secret

    def CreateSecrets(self, input):
        res = sum(self.GetNthSecret(secret, 2000) for secret in input)
        return res

    def GetPrices(self, s, n):
        prices = []

        previous_price = s % 10
        
        for _ in range(n):
            s = self.CalcAndMixAndPrune(s)
            price = s % 10
            change = price - previous_price
            prices.append((price, change))
            previous_price = price
        
        return prices

    def GetSequences(self, s, n):
        sequences = {}
        
        prices = self.GetPrices(s, n)
        
        for i in range(3, n):
            trailing_4 = prices[i-3:i+1]
            sequence = tuple(price_change[1] for price_change in trailing_4)
            if sequence in sequences:
                continue
            price = prices[i][0]
            sequences[sequence] = price
        
        return sequences

    def BuyBananas(self, input):
        all_sequences = set()
        sequence_prices = []
        
        for secret in input:
            sequences = self.GetSequences(secret, 2000)
            sequence_prices.append(sequences)
            for k, _ in sequences.items():
                all_sequences.add(k)

        best_price = 0
        
        for sequence in all_sequences:
            total_price = sum(price.get(sequence, 0) for price in sequence_prices)
            if total_price > best_price:
                best_price = total_price

        return best_price

    def pt1(self, input):
        self.debug(input)

        res = self.CreateSecrets(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.BuyBananas(input)

        return res
        
    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution(to_int=True)

    solution.part_1()
    
    solution.part_2()