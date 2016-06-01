from gensim import corpora, models, similarities
from pprint import pprint

corpus = ["At work","New job","Enjoying","Beer","Days off","wedding","Office","Drinks","Wine","Drinks","Blessed","A drink","Hubby","Much needed","New place","Thankful","apartment","Excited about","Vacation","Celebrate","Let me know","Had a blast","laundry","care of","company","Grocery","Wishes","Drinking for eveveryone","After work","To work tommorow","Bills","taxes","Husband","shift","The bar","Potty","ready to","Celebrating","To enjoy","My babies","Errands","Relaxing","apt","Fingers crossed","Poor baby","Day to all","women","Work","Yard","Doesn't","Uni","Days","Volunteer","Schedule","repeat","House","Apartment","Moving","place","Rent","Move","Month","Bedroom","Lease","Signed","Roommate","Interested","Complex","Area","Interest","apt","Drinking","Beer","Drink","Cold","Root","Beers","Pong","Ale","Ginger","Cans","Drinkin","ginger","Pint","Cans","Bbq","Pub","bottles","Home","Work","Ready","Hubby","Bed","Dinner","relax","Shower","Heading","Relaxing","Chill","Nap","Early","Supper","Snuggle","Money","Pay","Bills","Paid","Paying","Bill","Job","Month","Rent","Check","Taxes","Bucks","Debt","paycheck","job","Position","Company","Interview","Experience","Manager","Assistant","Interested","Career","Business","Resume","Sales","Hiring","Hire"]
stoplist = set('for a of the and to in'.split())

texts = [[word for word in string.lower().split() if word not in stoplist]
			for string in corpus]


pprint(texts)

dictionary = corpora.Dictionary(texts)
print(dictionary)

#stem words

# preprocessing
# mapping of each word in dictionary to its d_i value
#foreach word in dictionary, 
		#sum(d_i^2)

#for each query
	# foreach word in query, check if in dictionary
		# sum(q_i * d_i)

	#denominator
	# foreach word in query, check if in dictionary
		#sum(q_i^2)

# normalize by max value



# code to read in queries and print out values


