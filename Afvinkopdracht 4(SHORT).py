bestand = open("seq_afv4.txt")
x = str(bestand.readline())
total = len(x)
cytosine = x.count("c")
guanine = x.count("g")
adenine = x.count("a")
thymine = x.count("t")
gc_total = cytosine+guanine
def main():
	getComplement()
	GC_perc()
	isDNA()
def GC_perc():
	pregc_percentage = gc_total/total
	gc_percentage = pregc_percentage*100
	print ("GC Percentage is: "+str(gc_percentage)+"%")
def isDNA():
	if total == cytosine+guanine+adenine+thymine:
		print ("dit is DNA")
	else:
		print ("dit is geen DNA")
def getComplement():
	print (x.replace("a","T").replace("t","A").replace("c","G").replace("g","C").lower()) 
main()