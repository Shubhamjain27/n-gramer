import sys, json;
import requests
from bs4 import BeautifulSoup
import csv, re, sys
import tempfile

requests.packages.urllib3.disable_warnings()

INFO = "Info"
# https://books.google.com/ngrams/graph?content=Albertv%2Csoja&year_start=1800&year_end=2000&corpus=15&smoothing=3

corpora = "'American_English-2012':17, 'American English-2009':5, 'British English-2012':18, 'British English-2009':6, 'Chinese-2012':23, 'Chinese-2009':11,'English-2012':15, 'English-2009':0,'English Fiction-2012':16, 'English Fiction-2009':4, 'English OneMillion-2009':1, 'French-2012':19, 'French-2009':7, 'German-2012':20, 'German-2009':8, 'Hebrew-2012':24, 'Hebew-2009':9, 'Spanish-2012':21,'Spanish-2009':10, 'Russian-2012':25, 'Russia-2009':12, 'Italian':22"


def read_in():
    input=sys.stdin.readlines();
    return json.loads(input[0]);

def main():
    input = read_in();
    
    
    result = gngram(input);

    print result;

def gngram(data):
    data=data
    argumentString = data['arguments']
    if argumentString == '':
        main()
    start_year = ''
    end_year = ''
    corpus = ''
    smoothing = ''
    try:
        start_year = int(data['startYear'])
        

    except:
        print 'Oops:Start Year Must Be 4 digit Number,Try Again'
        print '\n'
        sys.exit()
    if start_year < 1500:
        print 'Oops:Start Year Should Not Be Less Than 1500,Try Again'
        print '\n'
        sys.exit()

    if start_year > 2007:
        print 'Oops:Start Year Should Not Be Greater Than 2007,Try Again'
        print '\n'
        sys.exit()

    try:
        end_year = int(data['endYear'])

    except:
        print 'Oops:End Year Must Be 4 digit Number,Try Again'
        print '\n'
        sys.exit()

    if end_year > 2008:
        print 'Oops:End Year Cant Not Be Greater Than 2008 ,Try Again'
        print '\n'
        sys.exit()

    if end_year == start_year:
        print 'Oops:Start Year And End Year Cant Not Be Equal,Try Again'
        print '\n'
        sys.exit()

    if start_year > end_year:
        print 'Oops:Start Year Can Not Be Gretaer Than End Year,Try Again'
        print '\n'
        sys.exit()

    try:
        lis2=[]
        corpus2 = data['corpora']
        if isinstance(corpus2, list):
            lis2=map(int, corpus2)
        else:
            lis2.append(int(corpus2))
        print lis2
        # if ',' in corpus2:
        #     split = corpus2.split(',')
        #     for alls in split:
        #         lis2.append(alls)
        # else:
        #     lis2.append(corpus2)

        # lis2 = map(int, lis2)
        
    except:
        print 'Oops:Choose A Corpora,Try Again'
        print '\n'
        sys.exit()

    try:
        smoothing = int(data['smoothing'])
    except:
        print 'Oops:Choose A Smoothing,Try Again'
        print '\n'
        sys.exit()

    year_difference = end_year - start_year
    year_difference = year_difference + 1
    result=""
    try:
        result=runQuery(argumentString, start_year, end_year, lis2, smoothing, year_difference)
    except Exception as s:
        print s
    return result;

def runQuery(argumentString, start_year, end_year, lis2, smoothing, year_difference):
    lis = []

    if ',' in argumentString:
        split = argumentString.split(',')
        for alls in split:
            lis.append(alls)
    else:
        lis.append(argumentString)

    # dynamic url

    query = ''
    if len(lis) == 1:
        query = lis[0]
    else:
        for x in lis:
            query += x + "%2C"
    
    f=tempfile.NamedTemporaryFile(mode='a',suffix=".csv", prefix="ngram-", dir='./output', delete=False)
    name=f.name
    f.close()

    for corpus in lis2:
        url = 'https://books.google.com/ngrams/graph?content=' + str(query) + '&year_start=' + str(
            start_year) + '&year_end=' + str(end_year) + '&corpus=' + str(corpus) + '&smoothing=' + str(smoothing) + ''

        # write first row

        row_list = []
        for names in lis:
            row_list.append(names)

        response = requests.get(url, verify=False)

        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        soup = str(soup)
        data=[]
        final_data=[]
        not_found= ["NA"]*year_difference
        x = re.findall(r'data(.*?)""}];', soup)
        evalVal= 'data'+x[0]+'""}];'
        exec(evalVal)


        returned_data = []  #returned_data is the list containing the keywords/ngrams for which the result is found
        for i in range(0, len(data)):
            returned_data.append(data[i]['ngram'])

        for i in range(0, len(lis)):
                if lis[i]  in returned_data:
                    j = returned_data.index(lis[i])
                    final_data.extend(data[j]['timeseries'])
                else:
                    final_data.extend(not_found)


        try:
            out=open(name,'a')
            writer = csv.writer(out)
            writer.writerow(row_list)

            blank_lis = []
            pairs = len(row_list)

            imax = 0
            x_index = 0
            zeal = 0
            neah = 0

            year_appended_l = []
            for yea_ap in range(start_year, end_year + 1):
                year_appended_l.append(yea_ap)

            for_yea = 0
            deal = 0
            condition = (pairs * year_difference) + year_difference

            while for_yea < condition:

                if len(blank_lis) == pairs:
                    print blank_lis
                    print '\n'
                    writer = csv.writer(out)
                    writer.writerow(blank_lis)
                    blank_lis = []
                    x_index = x_index + 1
                    imax = x_index


                else:
                    blank_lis.append(final_data[imax])
                    imax = imax + year_difference
                for_yea = for_yea + 1


        except Exception as r:
            print r
        out.close()
    return f.name

if __name__ == '__main__':
    main()