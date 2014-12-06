#########################################################################################
##Application to proccess DNA sequences in order to find: AT GC %, Legitimacy of DNA#####
##and its complementary sequence, By Richard Jansen, HAN University, 5-12-2014###########
#########################################################################################


##########################
##Pre-defined variables###
##########################

bestand = open("seq_afv4.txt")
x = str(bestand.readline())
total = len(x)
cytosine = x.count("c")
guanine = x.count("g")
adenine = x.count("a")
thymine = x.count("t")
gc_total = cytosine+guanine
at_total = adenine+thymine


################################################
##Main function referring to the subfunctions###
################################################

def main():
	getComplement()
	GC_perc()
	AT_perc()
	isDNA()



##############################
##Function to determine GC%###
##############################

def GC_perc():
	pregc_percentage = gc_total/total
	gc_percentage = pregc_percentage*100
	print ("GC Percentage is: "+str(gc_percentage)+"%")



##############################
##Function to determine GC%###
##############################

def AT_perc():
	preat_percentage = at_total/total
	at_percentage = preat_percentage*100
	print ("AT percentage is: "+str(at_percentage)+"%")



###################################################
##Funtion to determine the legitimacy of the DNA###
###################################################

def isDNA():
	if total == cytosine+guanine+adenine+thymine:
		print ("dit is DNA")
	else:
		print ("dit is geen DNA")



#########################################################################
##Function to determine the complementary strand to the given sequence###
#########################################################################

def getComplement():
	print (x.replace("a","T").replace("t","A").replace("c","G").replace("g","C").lower())



main()
