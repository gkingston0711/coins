

def OpenCSV(FileName):

    dict_coins = {'pennies': 0, 'nickles': 0, 'dimes': 0, 'quarters': 0}

    FileOpen = open(FileName,'r')
    i=0

    for line in FileOpen:
        line = line.split(' ')

        for i in range(0,len(line),2):
            if line[i] in dict_coins:
                dict_coins[line[i]] += int(line[i+1])


    return dict_coins

def CountCoins(dict_coins):

    SUM = 0
    for k, v in dict_coins.items():
        print k, '>', v
        if k == 'quarters':
            SUM += v*.25
        if k == 'nickles':
            SUM += v*.05
        if k == 'dimes':
            SUM += v*.1
        if k == 'pennies':
            SUM += v*.01


    #SUM = psum + nsum + dsum + qsum

    return SUM



def main():

    coins = OpenCSV('coins.txt')
    print coins

    SUM = CountCoins(coins)

    print 'The total amount of money in change: ', SUM


main()
