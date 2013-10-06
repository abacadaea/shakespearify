authors = [
'shakespeare', 
'hi',
]

MAX_LINES_PER_FILE = 30000
#files = dict ()
sentences = []

#open files
#read 
for author in authors:
	#files [author] = open ('../data/' + author,'r')
	wordfile = open ('../data/' + author,'r')
	numlines = 0

	for line in wordfile:
		cur_words = lines.split ()
		for word in cur_words:
			if (word [len (word) - 1] == '.'):

