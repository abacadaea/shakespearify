from math import log
from tester import read_input,get_train, run_tests, authors

EPS = 1E-3

freq = dict()
word_count = dict()

for author in authors:
	freq[author] = dict()

def train():

	example = get_train()

	while example is not None:
		[sentence, author] = example
		words = sentence
		for word in words:
			if word not in freq[author]: # this code is ugly
				freq[author][word] = 0
			freq[author][word] += 1

		example = get_train()

	for author in authors:
		word_count[author] = sum([freq[author][key] for key in freq[author]]) + 0.0


def test(sentence):
	bayes = dict()
	for author in authors:
		bayes[author] = 0

	words = sentence
	for word in words:
		for author in authors:
			if word not in freq[author]:
				bayes[author] += log(EPS) - log(word_count[author])
			else:
				bayes[author] += log(freq[author][word]) - log(word_count[author])

	return max(bayes.iterkeys(), key = (lambda key: bayes[key]))

print "Reading Input..."
read_input ()
print "Training..."
train()


print "Testing..."
run_tests(test)
