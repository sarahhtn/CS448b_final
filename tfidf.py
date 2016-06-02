from gensim import corpora, models, similarities
from pprint import pprint
from PorterStemmer import PorterStemmer
import variables
import string
import collections
import math

corpus = ["At work","New job","Enjoying","Beer","Days off","wedding","Office","Drinks","Wine","Drinks","Blessed","A drink","Hubby","Much needed","New place","Thankful","apartment","Excited about","Vacation","Celebrate","Let me know","Had a blast","laundry","care of","company","Grocery","Wishes","Drinking for eveveryone","After work","To work tommorow","Bills","taxes","Husband","shift","The bar","Potty","ready to","Celebrating","To enjoy","My babies","Errands","Relaxing","apt","Fingers crossed","Poor baby","Day to all","women","Work","Yard","Doesn't","Uni","Days","Volunteer","Schedule","repeat","House","Apartment","Moving","place","Rent","Move","Month","Bedroom","Lease","Signed","Roommate","Interested","Complex","Area","Interest","apt","Drinking","Beer","Drink","Cold","Root","Beers","Pong","Ale","Ginger","Cans","Drinkin","ginger","Pint","Cans","Bbq","Pub","bottles","Home","Work","Ready","Hubby","Bed","Dinner","relax","Shower","Heading","Relaxing","Chill","Nap","Early","Supper","Snuggle","Money","Pay","Bills","Paid","Paying","Bill","Job","Month","Rent","Check","Taxes","Bucks","Debt","paycheck","job","Position","Company","Interview","Experience","Manager","Assistant","Interested","Career","Business","Resume","Sales","Hiring","Hire"]
stemmer = PorterStemmer()
#stem words
# stems = ['At work', 'New job', 'Enjoi', 'Beer', 'Days off', 'wed', 'Office', 'Drink', 'Wine', 'Drink', 'Bless', 'A drink', 'Hubbi', 'Much need', 'New plac', 'Thank', 'apart', 'Excited about', 'Vacat', 'Celebr', 'Let me know', 'Had a blast', 'laundri', 'care of', 'compani', 'Groceri', 'Wish', 'Drinking for eveveryon', 'After work', 'To work tommorow', 'Bill', 'tax', 'Husband', 'shift', 'The bar', 'Potti', 'ready to', 'Celebr', 'To enjoi', 'My babi', 'Errand', 'Relax', 'apt', 'Fingers cross', 'Poor babi', 'Day to al', 'women', 'Work', 'Yard', 'Doesn\xc3\xadt', 'Uni', 'Dai', 'Volunt', 'Schedul', 'repeat', 'Hous', 'Apartment', 'Move', 'place', 'Rent', 'Move', 'Month', 'Bedroom', 'Leas', 'Sign', 'Roommat', 'Interest', 'Complex', 'Area', 'Interest', 'apt', 'Drink', 'Beer', 'Drink', 'Cold', 'Root', 'Beer', 'Pong', 'Ale', 'Ginger', 'Can', 'Drinkin', 'ginger', 'Pint', 'Can', 'Bbq', 'Pub', 'bottl', 'Home', 'Work', 'Readi', 'Hubbi', 'Bed', 'Dinner', 'relax', 'Shower', 'Head', 'Relax', 'Chill', 'Nap', 'Earli', 'Supper', 'Snuggl', 'Monei', 'Pai', 'Bill', 'Paid', 'Pai', 'Bill', 'Job', 'Month', 'Rent', 'Check', 'Tax', 'Buck', 'Debt', 'paycheck', 'job', 'Posit', 'Compani', 'Interview', 'Experienc', 'Manag', 'Assistant', 'Interest', 'Career', 'Busi', 'Resum', 'Sale', 'Hire', 'Hire']

# preprocessing
# weightedStems = {'Potti': 0.008, 'Thank': 0.008, 'New job': 0.008, 'Leas': 0.008, 'ready to': 0.008, 'Pint': 0.008, 'wed': 0.008, 'Dai': 0.008, 'Roommat': 0.008, 'Compani': 0.008, 'apart': 0.008, 'Day to al': 0.008, 'Buck': 0.008, 'Yard': 0.008, 'Sale': 0.008, 'Dinner': 0.008, 'Can': 0.015, 'Posit': 0.008, 'Days off': 0.008, 'Manag': 0.008, 'Husband': 0.008, 'Wine': 0.008, 'Volunt': 0.008, 'Readi': 0.008, 'Resum': 0.008, 'Celebr': 0.015, 'Tax': 0.008, 'Enjoi': 0.008, 'Drinking for eveveryon': 0.008, 'Doesn\xc3\xadt': 0.008, 'Move': 0.015, 'Area': 0.008, 'Hire': 0.015, 'Errand': 0.008, 'Beer': 0.023, 'Complex': 0.008, 'Interest': 0.023, 'Head': 0.008, 'Let me know': 0.008, 'Pub': 0.008, 'Job': 0.008, 'Check': 0.008, 'Experienc': 0.008, 'Fingers cross': 0.008, 'Hous': 0.008, 'Work': 0.015, 'Vacat': 0.008, 'Assistant': 0.008, 'job': 0.008, 'Uni': 0.008, 'shift': 0.008, 'Ginger': 0.008, 'Sign': 0.008, 'A drink': 0.008, 'place': 0.008, 'Bedroom': 0.008, 'Home': 0.008, 'Pong': 0.008, 'Drinkin': 0.008, 'Apartment': 0.008, 'To work tommorow': 0.008, 'apt': 0.015, 'At work': 0.008, 'Bbq': 0.008, 'Had a blast': 0.008, 'Earli': 0.008, 'Relax': 0.015, 'Much need': 0.008, 'My babi': 0.008, 'After work': 0.008, 'Snuggl': 0.008, 'Paid': 0.008, 'Supper': 0.008, 'Chill': 0.008, 'bottl': 0.008, 'relax': 0.008, 'Career': 0.008, 'Excited about': 0.008, 'Bed': 0.008, 'Bless': 0.008, 'Poor babi': 0.008, 'compani': 0.008, 'women': 0.008, 'Debt': 0.008, 'Office': 0.008, 'The bar': 0.008, 'Schedul': 0.008, 'Cold': 0.008, 'Bill': 0.023, 'tax': 0.008, 'ginger': 0.008, 'Nap': 0.008, 'Busi': 0.008, 'care of': 0.008, 'To enjoi': 0.008, 'Interview': 0.008, 'Pai': 0.015, 'Month': 0.015, 'Drink': 0.031, 'repeat': 0.008, 'Wish': 0.008, 'Hubbi': 0.015, 'Shower': 0.008, 'laundri': 0.008, 'Monei': 0.008, 'Root': 0.008, 'New plac': 0.008, 'paycheck': 0.008, 'Ale': 0.008, 'Groceri': 0.008, 'Rent': 0.015}

d_i = variables.weightedStems
exclude = set(string.punctuation)


for test in variables.textfiles:
	print "===================================================="
	print "----------    ", test, "    ----------"
	print "===================================================="
	# file -> array of individual responses
	filename = "responses/" + test
	f = open(filename, 'r')
	buff = f.read()
	buff = buff.replace(",", " ")
	buff = ''.join(ch for ch in buff if ch not in exclude)
	indiv_responses = buff.split('\n')

	tfidf = []
	# go through individual responses in this test condition
	for i in indiv_responses:
		arr = [word for word in i.lower().split() if word not in variables.stoplist]
		
		query_stems = []
		# stem each word in response
		for word in arr:
			query_stems.append(stemmer.stem(word))

		# calculate q_i
		query_stem_counts = collections.defaultdict(lambda:0.0)
		num_query_stems = len(query_stems)
		for stem in query_stems:
			query_stem_counts[stem] += 1.0

		q_i = collections.defaultdict(lambda:0.0)
		for stem, count in query_stem_counts.items():
			q_i[stem] = float("{0:.3f}".format(count/num_query_stems))

		# calculate tf-idf per response
		numerator = 0.0
		denominator_q_i2 = 0.0

		
		for word in query_stem_counts:
			if word in variables.d_stems:
				numerator += q_i[word] * d_i[word]
				denominator_q_i2 += q_i[word]*q_i[word]
		if denominator_q_i2 == 0:
			score = 0
		else:
			score = numerator / (math.sqrt(denominator_q_i2) * variables.sqrt_d_i2)
		tfidf.append(score)
		# print score

	#normalize tf-idf according to max score
	print "MAX: ", max(tfidf)
	norm = [float(i)/max(tfidf) for i in tfidf]
	for x in norm:
		print x










