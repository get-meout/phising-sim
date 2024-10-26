import datetime as DT
today = DT.date.today()
week_ago = today + DT.timedelta(days=7)

formatted_date = week_ago.strftime("%d %b")
day = int(week_ago.strftime("%d"))

if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]

formatted_date = f"{day}{suffix} {week_ago.strftime('%b')}"
print(formatted_date)