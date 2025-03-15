import datetime

class Product:

  def __init__(self):
    self.manufacture_date = input('enter manufacturing date (MM/DD/YYYY)')
    self.expiry_date = input('enter expiry date (MM/DD/YYYY)')

    self.manufacture_date = datetime.datetime.strptime(self.manufacture_date, '%m/%d/%Y')
    self.expiry_date = datetime.datetime.strptime(self.expiry_date, '%m/%d/%Y')

  def time_to_expire(self):
    today = datetime.datetime.now()

    if today > self.expiry_date:
      print('product expired already')
    else:
      time_left = self.expiry_date.date() - today.date()
      print(time_left)

obj = Product()
obj.time_to_expire()