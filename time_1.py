class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        totalsec=self.__second+other.__second
        totalmin=self.__second+other.__minute+(totalsec//60)
        totalhr=self.__hour+other.__hour+(totalmin//60)
        return time(totalhr,(totalmin % 60),(totalsec % 60))
    def display(self):
        print(f"The sum of the given time is:{self.__hour:02}:{self.__minute:02}:{self.__second:02}")
time1=time(10,12,23)
time2=time(12,33,24)
sum=time1+time2
sum.display()
