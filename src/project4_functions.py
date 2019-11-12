def regex_nodigits(df,col):
    '''use regex to clean string: 
    get rid of punctuations, capitalized letters and numbers'''
    #df['col'] = re.sub(r'[^\w\s]','',str(s)) #replaces anything not alphanumeric or whitespace with empty str
    #df['col'] = re.sub(r'["ADVERTISEMENT"]','',str(s))#replace the word "ADVERTISEMENT"--also replaced capital letters
    s = re.sub(r'[\d]','',str(df[col]))#replace digits with empty str
    return s

    ##*for re.sub, always change input to strings with str() (wouldn't hurt if it's already a string)