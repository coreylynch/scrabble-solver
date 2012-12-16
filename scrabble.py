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

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
	all_scores = {}
	rack = sys.argv[1]
	if '_' in rack:
		blank_count = rack.count('_')
		rack = rack.replace('_','')
		for letter in alphabet:
			for perm_size in range(2,len(rack)+blank_count+1):
				for perm in itertools.permutations(rack+letter, perm_size):
					word = ''.join(letter for letter in perm)
					if word in valid_words:
						score = sum([scores[i.lower()] for i in word])
						if score - scores[letter.lower()] > 0:
							all_scores[word] = score - scores[letter.lower()]
	else:
		for perm_size in range(2,len(rack)+1):
			for perm in itertools.permutations(rack,perm_size):
				word = ''.join(letter for letter in perm)
			 	if word in valid_words:
			 		score = sum([scores[i.lower()] for i in word])
			 		all_scores[word] = score
	
	sorted_scores = sorted(all_scores.iteritems(), key=operator.itemgetter(1), reverse=True)
	for i in sorted_scores:
		print("%d %s" % (i[1], i[0]))

if __name__=='__main__':
	main()
