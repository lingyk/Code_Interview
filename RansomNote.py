from collections import defaultdict

class solution(object):
	def canSpell(self, magzine, note):
		letters = defaultdict(int)
		for c in magzine:
			letters[c] += 1
		for c in note:
			if letters[c] <= 0:
				return False
			letters[c] -= 1
			print (letters)
		return True

print(solution().canSpell(['a','b','c','d','e','f'], 'bed'))