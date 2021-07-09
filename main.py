#main file will handle data collection and printing of algorithm results
###

'''
This function will parse the file

data is structured as 
    fromID -> toID

@param the filepath of the data
@return a dictionary containing the node to node connection
'''
def collectData(filePath):
    data = {}
    with open(filePath) as f:
        for line in f:
            l = line.split()
            fromID = l[0]
            toID = l[1]
           
        
                
    



def main():
    #we should collect the data first
    data = collectData('data/roadNet-TX.txt')











if __name__ == '__main__':
    main()