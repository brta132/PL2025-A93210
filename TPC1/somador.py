import sys

def main(debug):
    # Status: 'On' -> 1; 'Off' -> 0
    status = 1
    sum = 0

    for linha in sys.stdin:
        if (debug == True): print('\nLinha: ' + linha)

        i = 0
        while i < len(linha):

            if (debug == True): 
                print('Current i: ' + str(i))
                print('Current SUM: ' + str(sum))


            # check if 'on' or 'off'
            if linha[i].casefold() == 'o':
                if (debug == True): print("Found 'o'!")

                poss_on = ''
                poss_off = ''

                # take 2 chars to match with 'on'
                if(i + 1 < len(linha)):
                    poss_on = linha[i] + linha[i+1]

                    if (debug == True): print("Possible 'on': " + str(poss_on))

                # take 3 chars to match with 'off'
                if(i + 2 < len(linha)):
                    poss_off = linha[i] + linha[i+1] + linha[i+2]

                    if (debug == True): print("Possible 'off': " + str(poss_off))

                # check if 'on'
                if(poss_on.casefold() == 'on'): 

                    if (debug == True): print("Found 'on'!")

                    status = 1
                    i += 2

                # check if 'off'
                elif(poss_off.casefold() == 'off'): 

                    if (debug == True): print("Found 'off'!")

                    status = 0
                    i += 3
                
                else: i += 1

            # check '='
            elif linha[i] == '=':
                if (debug == True): print("Found '='!")

                print(sum)
                i += 1

            # check int
            elif linha[i].isdigit() and status == 1:

                if (debug == True): print("Found digit!")

                j = i + 1
                if (debug == True): print('j (start): ' + str(j))

                digit_str = linha[i]
                
                while j < len(linha) - 1 and linha[j].isdigit():
                    digit_str += linha[j]
                    j += 1

                if (debug == True):
                    print('j (end): ' + str(j))
                    print("Int: " + str(digit_str))

                sum += int(digit_str)
                i = j

            else: 
                i += 1

    return

main(debug=False)