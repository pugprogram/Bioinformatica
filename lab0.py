def output (name):
    dictForData={}
    with open (name,"r") as f:
        identificator=""
        value=""
        for line in f:
            if (line[0]=='>'):
                if (len(identificator)):
                    dictForData[identificator]=value
                    identificator=""
                    value=""
                identificator=line[0:len(line)-1] 
            else:
                value=value+line[0:len(line)-1]
        dictForData[identificator]=value
    return dictForData

def CompareString(name1, name2):
    scetchik=0
    i=0
    lenName1=len(name1)
    lenName2=len(name2)
    scetchik+=abs(lenName2-lenName1)
    while ((i<len(name1)) and (i<len(name2))):
        if (name1[i]!=name2[i]):
            scetchik+=1
        i+=1
    return scetchik

def alghorythm(ValueForCompare,FileName):
    dictForData={}
    with open(FileName,'r') as f:
        NewIdentificator=""
        value=""
        for line in f:
            if (line[0]=='>'):
                if (len(NewIdentificator)):
                    NewValue=CompareString(ValueForCompare,value)
                    dictForData[NewIdentificator]=NewValue
                    NewIdentificator=""
                    value=""
                NewIdentificator=line[0:len(line)-1] 
            else:
                value=value+line[0:len(line)-1]
        NewValue=CompareString(ValueForCompare,value)
        dictForData[NewIdentificator]=NewValue
    return dictForData

def WritingToFile(nameFile,Result,IdentificatorForCompare):
    file=open(nameFile,'a')
    file.write("Input Identificator:\n")
    file.write(IdentificatorForCompare)
    file.write("\n")
    file.write("Result:\n")
    for value in Result.keys():
        #print(value)
        file.write(value)
        file.write("\n")
    file.close()
    


if __name__ == "__main__":
    InputData=output("lab_0.txt")
    Result={}
    n=1
    for key,value in InputData.items():
        name="output.txt"
        #Result=alghorythm(value,"uniprot_sprot.fasta")
        Result=alghorythm(value,"uniprot_sprot.fasta")
        sorted_value=sorted(Result.items(),key=lambda item:item[1])
        WritingToFile(name,Result,key)
        n+=1
