import re;

# Writes the all compositors names, in alphabetic order, to an output file or to the screen.
# Names of type "LastName, FirstName" are rewritten as "FirstName LastName"
def compOrder(match_lst, outFileName, writeOutputToFile):
    comp_lst = []
    broken_name_re = r'(.+?),(.+)'

    #fix names that don't match the surname order
    for match in match_lst:
        comp = match[2]

        if (broken_name := re.match(broken_name_re,comp)) != None:
            comp = (broken_name[2] + " " + broken_name[1]).strip()

        comp_lst.append(comp)

    # get unique and sort
    comp_lst = list(set(comp_lst))
    comp_lst.sort()

    # write to output file || sys.out
    if(writeOutputToFile):
        with open(outFileName,'w+') as out:
            for comp in comp_lst:
                out.write(f'{comp}\n')
    else:
        print(comp_lst)
    
    return

# Creates a dictionary with the Periods (keys) and how many songs where written during those periods (values)
# if "writeOutputToFile" is set to True, writes the dictionary to a file specified by "outFileName"
def ObrasPeriodDict(match_lst, outFileName, writeOutputToFile):
    dic_ObrasPer = {}

    for match in match_lst:
        if(match[1] in dic_ObrasPer):
            dic_ObrasPer[match[1]] += 1
        else:
            dic_ObrasPer[match[1]] = 1

    # write to output file || sys.out
    if(writeOutputToFile):
        with open(outFileName,'w+') as out:
            for key, value in dic_ObrasPer.items():
                out.write(f'{key}: {value}\n')
    else:
        print(dic_ObrasPer)

    return

# Creates a dictionary with all Periods (keys) and an ordered list of all the song written during those periods (values)
# if "writeOutputToFile" is set to True, writes the dictionary to a file specified by "outFileName"
def ObrasPeriodListaOrd(match_lst, outFileName, writeOutputToFile):
    dic_ObrasPer = {}

    # Create dic
    for match in match_lst:
        if(match[1] not in dic_ObrasPer):
            dic_ObrasPer[match[1]] = []
        dic_ObrasPer[match[1]].append(match[0])

    # Order Value List
    for value in dic_ObrasPer.values():
        value.sort()         

    # Write to output file || sys.out
    if(writeOutputToFile):
        with open(outFileName,'w+') as out:
            for key, value in dic_ObrasPer.items():
                out.write(f'{key}: \n')
                for val in value:
                    out.write(f'\t{val}\n')
                out.write("\n")
    else:
        print(dic_ObrasPer)

    return

def main(writeOutputToFile):

    #regex
    idented_line_regex = r'^\W+'
    full_line_regex = r'(.+?);.+?;\d+;(.+?);(.+?);\d\d:\d\d:\d\d;O\d+'

    match_count = 0
    match_lst = []
    
    # open file
    with open("obras.csv",'r') as file:
        
        #skip first line
        file.readline()

        line = file.readline()

        #read  csv file line by line
        while(file):

            full_line = line

            # remove formating to inline the full csv line (multi-line descriptions)
            if(not re.match(full_line_regex, line)):

                line = file.readline() # get idented line

                while(re.match(idented_line_regex,line)):
                    full_line += line
                    line = file.readline()

                # remove extra space
                full_line = re.sub(r'\s\s+',"",full_line)

            else: 
                line = file.readline()

            # Find matches and add to match list
            matches = re.findall(full_line_regex, full_line)
            if(matches != []):
                match_lst.append(matches[0])
                match_count += 1
            else:
                break

# ----------------------------- Manipulate data here  -----------------------------
    outFile__Comp = 'obras__CompositoresPorOrdemAlfabetica.txt'
    compOrder(match_lst, outFile__Comp, writeOutputToFile)
    print("\n")

    outFile__ObrasPeriodo = 'obras__NumObrasPorPeriodo.txt'
    ObrasPeriodDict(match_lst, outFile__ObrasPeriodo, writeOutputToFile)
    print("\n")


    outFile__ObrasPeriodoListaOrd = 'obras__ObrasPorPeriodoListaOrd.txt'
    ObrasPeriodListaOrd(match_lst, outFile__ObrasPeriodoListaOrd, writeOutputToFile)

    return


if __name__ == "__main__":
    main(writeOutputToFile=False)