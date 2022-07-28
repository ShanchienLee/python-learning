height = input("請輸入您的身高(公分)")
weight = input("請輸入您的體重(公斤)")

height = int(height)/100
weight = int(weight)

BMI = round(weight/(height ** 2),2)

if BMI < 18.5:
    print(f"您的BMI是：{BMI}(體重過輕)")
elif BMI < 24:
    print(f"您的BMI是：{BMI}(正常體位)")
elif BMI < 27:
    print(f"您的BMI是：{BMI}(體重過重)")
elif BMI < 30:
    print(f"您的BMI是：{BMI}(輕度肥胖)")
elif BMI < 35:
    print(f"您的BMI是：{BMI}(中度肥胖)") 
else:
    print(f"您的BMI是：{BMI}(重度肥胖)") 
