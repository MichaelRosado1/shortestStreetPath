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
    data = [] 
    with open(filePath) as f:
        for line in f:
            l = line.split()
            #we now have the from and to ID's
            fromID = l[0]
            toID = l[1]
            #we want to store the pair before we convert it into a graph
            pair = (fromID, toID)
            data.append(pair)

    return data
           
        
                
    



def main():
    #we should collect the data first
    data = collectData('data/roadNet-TX.txt')

    print(data[0])










if __name__ == '__main__':
    main()
