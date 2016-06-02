from PorterStemmer import PorterStemmer
from pprint import pprint
import math

corpus = ["At work", "New job", "Enjoying", "Beer", "Days off", "wedding", "Office", "Drinks", "Wine", "Drinks", "Blessed", "A drink", "Hubby", "Much needed", "New place", "Thankful", "apartment", "Excited about", "Vacation", "Celebrate", "Let me know", "Had a blast", "laundry", "care of", "company", "Grocery", "Wishes", "Drinking for eveveryone", "After work", "To work tommorow", "Bills", "taxes", "Husband", "shift", "The bar", "Potty", "ready to", "Celebrating", "To enjoy", "My babies", "Errands", "Relaxing", "apt", "Fingers crossed", "Poor baby", "Day to all", "women", "Work", "Yard", "Doesn't", "Uni", "Days", "Volunteer", "Schedule", "repeat", "House", "Apartment", "Moving", "place", "Rent", "Move", "Month", "Bedroom", "Lease", "Signed", "Roommate", "Interested", "Complex", "Area", "Interest", "apt", "Drinking", "Beer", "Drink", "Cold", "Root", "Beers", "Pong", "Ale", "Ginger", "Cans", "Drinkin", "ginger", "Pint", "Cans", "Bbq", "Pub", "bottles", "Home", "Work", "Ready", "Hubby", "Bed", "Dinner", "relax", "Shower", "Heading", "Relaxing", "Chill", "Nap", "Early", "Supper", "Snuggle", "Money", "Pay", "Bills", "Paid", "Paying", "Bill", "Job", "Month", "Rent", "Check", "Taxes", "Bucks", "Debt", "paycheck", "job", "Position", "Company", "Interview", "Experience", "Manager", "Assistant", "Interested", "Career", "Business", "Resume", "Sales", "Hiring", "Hire"]
stoplist = set('for a of the and to in'.split())

stemmer = PorterStemmer()

texts = [[word for word in string.lower().split() if word not in stoplist]
			for string in corpus]

words = reduce(list.__add__, texts)

stems = []
for word in words:
	stem = stemmer.stem(word)
	stems.append(stem)

stemCounts = {}

numStems = len(stems)
for word in stems:
	if word not in stemCounts:
		stemCounts[word] = 1.0
	else:
		stemCounts[word] = stemCounts[word] + 1.0


for word in stemCounts:
	stemCounts[word] = stemCounts[word]/numStems;
	stemCounts[word] = float("{0:.3f}".format(stemCounts[word]))

print stemCounts

# calculate sqrt(sum(d_i squared))
total = 0.0
for word in stemCounts:
	total += stemCounts[word] * stemCounts[word]

print math.sqrt(total)

