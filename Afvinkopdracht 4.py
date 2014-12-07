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
	print (" ")
	print ("##################################################")
	print (" ")
	GC_perc()
	print (" ")
	print ("###################################################")
	print (" ")
	AT_perc()
	print (" ")
	print ("####################################################")
	print (" ")
	isDNA()
	print (" ")
	print ("#####################################################")
	print (" ")
	translation()



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

###############################################################
##Function to translate the sequence to a aminoacid sequence###
###############################################################
	
def translation():
        with open ("seq_afv4.txt", "r") as seq:
                data=seq.readlines()

        map = {"ttt":"F", "ttc":"F", "tta":"L", "ttg":"L",
               "tct":"S", "tcc":"S", "tca":"S", "tcg":"S",
               "tat":"Y", "tac":"Y", "taa":"STOP", "tag":"STOP",
               "tgt":"C", "tgc":"C", "tga":"STOP", "tgg":"W",
               "ctt":"L", "ctc":"L", "cta":"L", "ctg":"L",
               "cct":"P", "ccc":"P", "cca":"P", "ccg":"P",
               "cat":"H", "cac":"H", "caa":"Q", "cag":"Q",
               "cgt":"R", "cgc":"R", "cga":"R", "cgg":"R",
               "att":"I", "atc":"I", "ata":"I", "atg":"M/START",
               "act":"T", "acc":"T", "aca":"T", "acg":"T",
               "aat":"N", "aac":"N", "aaa":"K", "aag":"K",
               "agt":"S", "agc":"S", "aga":"R", "agg":"R",
               "gtt":"V", "gtc":"V", "gta":"V", "gtg":"V",
               "gct":"A", "gcc":"A", "gca":"A", "gcg":"A",
               "gat":"D", "gac":"D", "gaa":"E", "gag":"E",
               "ggt":"G", "ggc":"G", "gga":"G", "ggg":"G",}

        DNA=data[0].strip()
        start = DNA.find('atg')
        if start!= -1:
            while start+2 < len(DNA):
                codon = DNA[start:start+3]
                if codon == "tag": break;
                print(map[codon])
                start+=3


main()
