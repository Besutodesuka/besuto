def getuniqueclass(data):
    unique_class = []
    for j in data.unique():
        token = re.split(' ',j)
        if len(token)==1:
            unique_class.append(token[0])
        else:
            pass
    return unique_class

def multiclass_encode(labels, unique_class):
    output= []
    decodekey = {}
    unique_class = getuniqueclass(data['labels'])
    for i,value in enumerate(sorted(unique_class)):
        decodekey[value] = i 
    for label in labels:
        token = np.zeros(len(decodekey))
        for i in label:
            index = decodekey[i]
            np.put(token,index,1)
        output.append(token)
    return np.array(output)


labels = multiclass_encode(labels, unique_class)