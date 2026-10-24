from moving import forecasts
from excel_manager import data_list


def total_quantity(data_list):

    total=0

    for row in data_list:
        total+=row["Count"]

    return total

def total_revenue(data_list):

    total=0

    for row in data_list:
        total+=row["Count"]*row["Price"]

    return total

def average_total(data_list):

    total=total_quantity(data_list)

    if len(data_list) == 0:
        return 0

    return total/len(data_list)

print(f"شده مجموع کل تعداد محصوالت فروخته :{total_quantity(data_list)}")

print(f"مجموع کل درآمد حاصل از فروش :{total_revenue(data_list)}")

print(f"میانگین تعداد فروش روزانه :{average_total(data_list)}")

def check_sell(actual, forecasts):
    if forecasts is None:
        return None

    if actual > forecasts * 1.10:
        return "فروش عالی"

    elif actual < forecasts * 0.90:
        return "فروش ضعیف"

    else:
        return "فروش معمولی"
