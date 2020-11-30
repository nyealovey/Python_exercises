from Visualization_Data.die import Die

# 创建一个六面骰子
die = Die()

# 掷几次骰子，并将结果存在一个列表中

results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

# 分析结果

frequencies = []