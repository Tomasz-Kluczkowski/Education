def m_generator(size, low_boundary, upp_boundary):
    '''generates a square matrix of size filled with random numbers from low_boundary to upp_boundary'''
    import  random
    rng = random.Random()       # create object to invoke random methods on

    m = []                      # create empty matrix

    for row in range(size):

        m.append([])            # add row to the matrix

        for col in range(size):

            m[row].append(rng.randrange(low_boundary, upp_boundary))    #add elements to the row being iterated

    return m



m_generator(5, 0, 11)

