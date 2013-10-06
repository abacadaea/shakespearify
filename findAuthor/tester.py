import random, math, findAuthor

authors = [
'shakespeare', 
'hi',
]

MAX_LINES_PER_FILE = 30000
MAX_TRAIN = 30000
MAX_TEST = 1000

sent_ind = 0
#files = dict ()
sentences = []

def clean (word):
	ret = ""
	for c in word:
		if c in ascii_lowercase:
			ret = ret + c
	return ret

#open files
#read 
def read_input ():
	for author in authors:
		#files [author] = open ('../data/' + author,'r')
		wordfile = open ('../data/' + author,'r')
		numlines = 0
		words = []

		for line in wordfile:
			cur_words = lines.split ()
			for word in cur_words:
				if (word [len (word) - 1] == '.'):
					if (len (words) > 0):
						sentences.append ([words, author])
						words = []
				word_clean = clean (word.lower ())
				if len (word_clean) > 0:
					words.append (word_clean)


def get_train ():
	if num_train >= MAX_TRAIN:
		return None
	sent_ind += 1
	return sentences [sent_ind]

def test ():
	correct = 0
	total = 0
	
	for i in range (MAX_TRAIN, MAX_TRAIN + MAX_TEST):
		ret = findAuthor.test (sentences[i][0])
		if ret == sentences [i][1]:
			correct += 1
		total += 1
		print correct + '/' + total

random.shuffle (sentences)
=======
from math import log
from tester import get_train

authors = []
EPS = 1E-5

freq = dict()

for author in authors:
	freq[author] = dict()

def train(sentence, author):

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
>>>>>>> 2f29b9fe06f7c72a4a519aabcb581691cc393cfc
