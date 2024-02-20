import datetime

current_date = datetime.datetime.today()
past_date = current_date - datetime.timedelta(days=1)
future_date = current_date + datetime.timedelta(days=1)
print("\n",past_date,"\n",current_date,"\n",future_date)