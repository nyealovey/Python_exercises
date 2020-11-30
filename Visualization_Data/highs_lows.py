import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温,最低和日期
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        low = int(row[3])
        lows.append(low)
    print(highs)

# 根据数据绘制图形

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates,highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式

plt.title("Daily high and low temperatures,2014", fontsize=24)
plt.xlabel("Temperature(F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()