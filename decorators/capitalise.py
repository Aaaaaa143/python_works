def capitalise(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper



@capitalise
def morning_greetings():
    return "good morning"
@capitalise
def afternoon_greetings():
    return "good afternoon"

def night_greetings():
    return "good evening"
# print(morning_greetings())
# print(afternoon_greetings())  


from datetime import datetime
current_time=datetime.now()
current_hour=current_time.hour
def greetings():
    if current_hour in  range(5,12):
        print(current_hour)
        print(morning_greetings())

    elif current_hour in range(12,17):
        print(current_hour)
        print(afternoon_greetings())

    else:
        print(current_hour)
        print(night_greetings())

greetings()   