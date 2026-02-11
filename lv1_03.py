import datetime
birth_day=int(input())
birth_month=int(input())
birth_year=int(input())

today=datetime.date.today()
birth_date=datetime.date(birth_year,birth_month,birth_day)

age_year=today.year - birth_date.year
age_month=today.month - birth_date.month
age_day=today.day - birth_date.day

if age_day<0:
  age_month-=1
  
  prev_month = today.month - 1 if today.month > 1 else 12
  prev_year = today.year if today.month > 1 else today.year - 1
  days_in_prev_month = (datetime.date(prev_year, prev_month % 12 + 1, 1) - datetime.timedelta(days=1)).day
  age_day += days_in_prev_month




if age_month<0:
  age_year-=1
  age_month+=12

print(f"Tuổi của bạn chính xác là: {age_year} tuổi {age_month} tháng {age_day} ngày")



