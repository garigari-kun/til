def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    nonunique = []
    for num in data:
        if data.count(num) > 1:
            nonunique.append(num)

    #replace this for solution
    return nonunique
