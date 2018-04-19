def date_sorter(s):
    import re

    # replace '-' with '/'
    s = s.str.replace('-', '/')

    # map month names to numbers
    dict = {'Jan': '01', 'jan': '01', 'January': '01',
            'Feb': '02', 'feb': '02', 'February': '02',
            'Mar': '03', 'mar': '03', 'March': '03',
            'Apr': '04', 'apr': '04', 'April': '04',
            'May': '05', 'may': '05',
            'Jun': '06', 'jun': '06', 'June': '06',
            'Jul': '07', 'jul': '07', 'July': '07',
            'Aug': '08', 'aug': '08', 'August': '08',
            'Sep': '09', 'sep': '09', 'September': '09',
            'Oct': '10', 'oct': '10', 'October': '10',
            'Nov': '11', 'nov': '11', 'November': '11',
            'Dec': '12', 'dec': '12', 'December': '12'}

    #Regex
    regex = re.compile(r'\b((%s)\S*)\b' %'|'.join(dict.keys()), re.I)

    # create df from series
    df = pd.DataFrame(s, columns=['original'])

    # map months to numbers
    def dict_lookup(val):
        return dict[val.group(2)]

    def lookup(value):
        try:
            match = dict[regex.search(value).group(2)]
        except AttributeError:
            match = ''

        return regex.sub(dict_lookup, value)

    df['new'] = df['original'].map(lambda x: lookup(x))

    # remove alpha characters
    df['new'] = df['new'].str.replace('[A-Za-z]', '')

    #df['new'] = df['new'].str.split(',')

    return df
