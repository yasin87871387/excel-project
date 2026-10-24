import pandas as pd
from calculations import total_revenue, total_quantity, average_total, check_sell


def save_report(data_list, forecast, next_day_forecast):

    report_data = []

    for i in range(len(data_list)):
        row = {
            "Date":data_list[i]["Date"],
            "Daily Sales Count":data_list[i]["Count"],
            "Forecast":forecast[i]
        }

        status = check_sell(data_list[i]["Count"], forecast[i])
        row["Status"] = status

        report_data.append(row)

    report_df = pd.DataFrame(report_data)

    summary = {
        "Total Count":total_quantity(data_list),
        "Average Count":average_total(data_list),
        "Next Day Forecast":next_day_forecast,
        "Total Revenue": total_revenue(data_list)
    }

    summary_df = pd.DataFrame([summary])

    with pd.ExcelWriter('summary.xlsx') as writer:
        report_df.to_excel(writer, sheet_name = "گزارش پیش بینی", index=False)
        summary_df.to_excel(writer, sheet_name= "خلاصه آمار", index=False)
