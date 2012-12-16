import itertools
import operator
import sys

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

with open('sowpods.txt') as f:
	valid_words = set(i.strip() for i in f)

def main():
	all_scores = {}
	rack = sys.argv[1]
	for i in range(2,len(rack)+1):
		for j in itertools.permutations(rack,i):
			word = ''.join(letter for letter in j)
		 	if word in valid_words:
		 		score = sum([scores[i.lower()] for i in word])
		 		all_scores[word] = score
	
	sorted_scores = sorted(all_scores.iteritems(), key=operator.itemgetter(1), reverse=True)
	for i in sorted_scores:
		print("%d %s" % (i[1], i[0]))

if __name__=='__main__':
	main()
