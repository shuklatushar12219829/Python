

fin = open('InputData3.txt', 'r')	    #Open the text Files for input and output
fout = open('NewK22PF.txt', 'w')
for line in fin:				        #for each line
    fout.write(line)				    #Write the line
fin.close()				                #Close the input file
fout.close()                			#Close the output file
fin = open('NewK22PF.txt' , 'r')
for line in fin:            			#for each line
    print(line,end='')      			#Print line
fin.close()                 			#Close the File
