

csvfile = open ('CSV_Format.csv' , 'r+')
#list1 = ['Full Marks,12,\r', 'Bonus,,\r', 'Name,Roll No,Marks\r', 'SS,2869,21\r', 'sd,232,12\r', 'dsga,12,\r', 'as,,12\r', ',231,231\r', ',,\r', 'das,321,312\r', '']
csv = csvfile.readlines()

'''
if(csv[0][1] != None ):
    print csv[0][1]
    if(csv[1][1] != None):
        print csv[1][1]
        if( csv[3] != None):
            for i in range(3,len(csv)):
                if( (csv[i][0] or csv[i][1] or csv[i][2] ) is None):
                    print 'wrong format'
                print csv[i]
'''                    
            
                
for i in range(0,len(list1)):
    line = list1[i].split(',')
    print "line %s" % (line)
    if(i == 0):
        if(line[1] == ''):
            print 'wrong'        
    if(i == 1):
        if(line[1] == ''):
            print 'wrong'
    if(i > 2):
        if( line[0] == '' or line[1] =='' or line[2] == '' or line[2] == '\r'):
            print 'wrong'
