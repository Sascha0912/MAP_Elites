def updateMap(replaced,replacement,map,newInd,fitness,misc):
    # Replace individuals and fitness
    map.fitness[replaced] = fitness[replacement]
    map.genomes[replaced] = newInd[replacement]

    # Replace Miscellaneous Map values
    for iValues in range(len(map.misc)):
        eval('map.' + map.misc[iValues] + '[replaced] = misc[' + str(iValues) + '][replacement]')

    return map