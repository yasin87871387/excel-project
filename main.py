from excel_manager import data_list
from moving import Moving_Average
from report import save_report

forecast, next_day_forecast = Moving_Average(data_list)

save_report(data_list, forecast, next_day_forecast)

print("Report created successfully!")