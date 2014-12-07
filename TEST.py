############################################################
###Application to translate DNA to Protein, 6-12-2014#######
###By: Richard Jansen, HAN University of Applied Sciences###
############################################################

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
