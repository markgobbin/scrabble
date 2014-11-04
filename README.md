scrabble
========

a basic scrabble word solver:

after initialising the class, use the load() function. Then use solveForRack(rack,blanks=0) 
with rack = a string of letters that you have in scrabble, blanks = the number of blanks that you have.
If you have no blanks, use solveForLetters(rack) which is a bit faster.
solveForWords(rack,words,blanks=0) #(Slow). Given a list of words, finds larger words containing one of the words
  #For example you could use solveForWords("abcdefg",["oat","ow"]) and it will return boat, goat, cow, bow, possibly others
solveAcrossWord(rack,word,blanks=0) #Given a word, find words that can go perpendicularly across the word 
  #For example if you have the word "father" then the word "men" can go across the "e" if you have "m" and "n"
load() #Use this after initialising the class. It loads dictionary and letter frequency file (below)
loadSowpods() #loads the dictionary, sowpods.txt. not necessary for normal use
loadFrequencies() #loads the letter frequency file. not necessary for normal use
saveFrequencies() #not necessary for normal use. this simply generates the letter frequency file, which i have included already, from the dictionary, which must be loaded
