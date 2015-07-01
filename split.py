from bs4 import BeautifulSoup
import urllib2

def break_words (movie_name):
#Breaks up movie_name into constituent words	
	words = movie_name.split()
	return words

def print_first_word (words):
#Returns first word of list after popping it out	
	word = words.pop(0)
	return word

def print_all_words (movie_name):
#Adds '+' in between words
	words = break_words(movie_name)
	movie_with_plus = ""
	for i in range(0,len(words)):
		movie_with_plus = movie_with_plus + "+" + print_first_word(words)
	return movie_with_plus

print "Enter the name of the movie"
movie_name = raw_input(">>")
movie_with_plus = print_all_words (movie_name)

common_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="

#url to IMDb page created
new_url =  common_url + movie_with_plus

page = urllib2.urlopen(new_url)
soup_package1 = BeautifulSoup(page)
expression = soup_package1.find(class_ = "result_text")

#class = "result_text" attribute not found 
if expression is None:
	print "No results found for " + "\"" + movie_name + "\""
	exit(0)

atag = expression.a
movie_link = (atag['href'])

#final link to IMDb page for movie created
proper_movie_link = "http://www.imdb.com" + movie_link 

new_page = urllib2.urlopen(proper_movie_link)

#URL created is invalid i.e. cannot be opened
if new_page is None:
	print "Proper movie link cannot be opened"
	exit(0)

soup_package2 = BeautifulSoup(new_page)
finding_rating = soup_package2.find("div", class_ = "star-box-details")
 
# class = "star-box-details" attribute does not exist 
if finding_rating is None:
	print "Invalid movie name"
	exit(0)

rating_span = finding_rating.span

#Movie does not have rating
if rating_span is None:
	print "Type complete movie name"
	exit(0)

#Displaying rating
print("The rating is "+rating_span.string)






















