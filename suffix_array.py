from functools import cmp_to_key

class suffix():
	def __init__(self, rank, index, next):
		self.rank = rank
		self.index = index
		self.next = next

def sorter(a, b):
	if a.rank != b.rank:
		return 1 if a.rank > b.rank else -1
	else:
		return 1 if a.next > b.next	else -1

def suffix_array(string):	
	suffixes = [suffix(ord(string[i]) - ord('a'), i, 0) for i in range(len(string))]
	for s in suffixes:
		if s.index + 1 >= len(string):
			s.next = -1
		else:
			s.next = suffixes[s.index+1].rank
	suffixes.sort(key=cmp_to_key(sorter))
	ind = [0] * len(string)
	i = 4
	while i < 2*len(string):
		rank = 0
		prev = suffixes[0].rank
		suffixes[0].rank = rank
		ind[suffixes[0].index] = 0
		for j in range(1, len(string)):
			if suffixes[j].rank == prev and suffixes[j].next == suffixes[j - 1].next:
				prev = suffixes[j].rank
				suffixes[j].rank = rank
			else:
				prev = suffixes[j].rank
				suffixes[j].rank = rank + 1
				rank += 1
			ind[suffixes[j].index] = j
		for k in range(len(string)):
			next_idx = suffixes[k].index + i // 2
			if next_idx < len(string):
				suffixes[k].next = suffixes[ind[next_idx]].rank
			else:
				suffixes[k].next = -1
		i*=2
		suffixes.sort(key=cmp_to_key(sorter))
	return suffixes

def print_suffix(string, suffix_array):
	for s in suffix_array:
		print(string[s.index:])


string = "banana"
result = suffix_array(string)
print_suffix(string, result)