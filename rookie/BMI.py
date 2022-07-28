height = input("請輸入您的身高(公分)")
weight = input("請輸入您的體重(公斤)")

height = int(height)/100
weight = int(weight)

BMI = round(weight/(height ** 2),2)

print(f"您的BMI是：{BMI}")
