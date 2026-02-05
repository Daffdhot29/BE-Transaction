from datetime import datetime 

def convert_datetime_str(dt:datetime) -> str : 
    date_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    return date_time 

def convert_str_date(dt_str:str) -> datetime : 
    strDate = datetime.strptime(dt_str,"%d-%m-%Y")
    return strDate
    