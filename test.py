print("###########The pro Tip-Calculator#########")
print("###########by - payakan#########")

total_bill = input("enter the total bill : ")
total_bill = float(total_bill)

tip_percent = input("enter the percentage of the tip : ")
tip_percent = float(tip_percent)
tip_percent = tip_percent / 100
tip_percent = total_bill * tip_percent
tip_percent = total_bill+tip_percent

people = input("how peoples are in there : ")
people = int(people)

each_person_pay = tip_percent / people
each_person_pay = round(each_person_pay,2)
each_person_pay = "{:.2f}".format(each_person_pay)

print(f"each person would pay {each_person_pay} ")