import datetime

def getage():
    birthdate = datetime.datetime(1979, 2, 22)  
    today = datetime.datetime.today()
    delta = today - birthdate

    return delta.days / 365.25  

def getemploymentstatus():
    return True