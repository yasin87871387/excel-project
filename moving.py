from excel_manager import data_list

def Moving_Average(data_list,window=3):

    forecast=[]

    for i in range (len(data_list)):
        if i < window:
            forecast.append(None)
        else:

            total=0

            for j in range (i-window,i):

                total+=data_list[j]["Count"]

            forecast.append(total/window)

    total=0

    for i in range (len(data_list) - window , len(data_list)):

        total+=data_list[i]["Count"]

    next_day_forecast= total/window

    return forecast , next_day_forecast

forecasts, next_day = Moving_Average(data_list)

print("پیش‌بینی‌ها:")

for i in range(len(forecasts)):
    print(i + 1, forecasts[i])

print("پیش‌بینی روز بعد:", next_day)