from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M;%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%B,%Y")
print(format3)
format4=current_time.strftime("%A,%B %H:%M:%S %P")
print(format4)
format6=current_time.strftime("%a-%b-%d %H:%M:%S %Y")
print(format6)
format7=current_time.strftime("%d")
print(format7)
format8=current_time.strftime("%H:%M:%S")
print(format8)
format9=current_time.strftime("%m")
print(format9)
format10=current_time.strftime("%Y")
print(format10)