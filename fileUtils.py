import os, time, datetime
from posixpath import basename
import json
from zipfile import ZipFile
from os.path import basename


#======CONFIG===========#

def getInfo():
    f = open('config.json')
    jfile = json.load(f)
    version = jfile['config']['version']
    if version == '2017':
        DIRnfe = jfile['2017']['nfe']
        DIRnfce = jfile['2017']['nfce']
    elif version == 'mySQL':
        DIRnfe = jfile['mySQL']['nfe']
        DIRnfce = jfile['mySQL']['nfce']

    return (DIRnfce, DIRnfe)

#======CONFIG===========#    

#========DATE Handler=======#
def date():
    '''
    this function is responsible for getting the actual year
    and month and then reducing one month and if necessary 
    one year to pass this data to the listFilesbyDate function
    '''
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    year = datetime.date.today().year
    month =  datetime.date.today().month
    if month == 1:
        month = 12
    else:
        month -= 1

    
    return (months[month], str(year))


#===========XML handler===========#
def creationData(file):
    '''
    this function is responsible for getting the
    full creation data of a specified file
    '''
    date = time.ctime(os.path.getctime(file))
    return date

def year(date):
    '''
    use this function with creationData() returning
    to get the specific part (year)
    '''
    return date[20:24]
    
def month(date):
    '''
    use this function with creationData() returning
    to get the specific part (month)
    '''
    return date[4:7]

def organizedPrint(argleft, argright):
    '''
    helper function to see data
    argleft: what you wanna see on the left
    argright: what you wanna see on the right
    '''
    print(f'{argleft:.<45}{argright:>}')

def listFilesbyDate(DIR='str | Pathlike', date=tuple):
    '''
    This function will iterate trough existing
    files given in the 'DIR' parameter
    and put their path into a list sorting them by
    creation date and finaly return two lists: one for path
    name other for file names. It has to be this way because
    of the zipFile process.
    '''
    
    dir_list = []
    file_list = []
    m, y = date

    if len(m) == 0:
        for f in os.listdir(DIR):
            date = creationData(DIR+'/'+f)
            if year(date) == y:
                organizedPrint(f, date)
    else:
        if not m[0].isupper():
            m = m.capitalize() 

        for f in os.listdir(DIR):
            date = creationData(DIR+'/'+f)
            if year(date) == y and month(date) == m:
                #organizedPrint(f, date)
                dir_list.append(DIR)
                file_list.append(f)
                
    
    return dir_list, file_list


def getFileList(nfe='str | Pathlike', nfce='str | Pathlike'):
    '''
    This function will be responsible for executing listFilesbydate
    sequentialy. First it will search for nfce and then for nfe dir.
    Finally it will return a tuple containing two lists: one list for each
    dir searched.
    '''
    nfce = listFilesbyDate('/home/thalles/Documents', date()) # change to nfce param
    nfe =  listFilesbyDate('/home/thalles/Downloads', date()) # change to nfe param
    
    return (nfe, nfce)

#===========XML handler===========#


#===========ZIP FILE===========#

def zipFiles():
    '''
    CONTINUE: deal with the problem of handling two lists
    '''
    nfe, nfce = getFileList()
    with ZipFile('nfe.zip', 'w') as zip_nfe: 
        for n in nfe[1]:
            zip_nfe.write(n[1], basename(n[0]))
        zip_nfe.close()

    with ZipFile('nfce.zip', 'w') as zip_nfce:
        for n in nfce[1]:
            zip_nfce.write(n[1], basename(n[0]))
        zip_nfce.close()


#===========ZIP FILE===========#

zipFiles()

