from math import log
from tester import read_input,get_train, run_tests

authors = []
EPS = 1E-5

freq = dict()

for author in authors:
	freq[author] = dict()

def train():

	example = get_train()

	while example is not None:
		[sentence, author] = example
		words = sentence.rstrip().split()
		for word in words:
			if word not in freq[author]: # this code is ugly
				freq[author] = 0	
			freq[author] = 1

		example = get_train()

def test(sentence):
	bayes = dict()
	for author in authors:
		bayes[author] = 0

	words = sentence.rstrip().split()
	for word in words:
		for author in authors:
			if word not in freq[author]:
				bayes[author] += log(EPS)
			else:
				bayes[author] += log(freq[author][word])

	return max(bayes.iterkeys(), key = (lambda key: bayes[key]))

print "Reading Input..."
read_input ()
print "Training..."
train()
print "Testing..."
run_tests()
