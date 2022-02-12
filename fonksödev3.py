vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))
genel_not = vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10
for dongu in range(0,1):
  if vize1 > 100 or vize1 < 0 or vize2 > 100 or vize2 < 0 or final > 100 or final < 0 :
       print("Lütfen 0-100 aralığında not giriniz")
       break
  if (genel_not >= 90):
     print("AA")
  elif (genel_not >= 85):
       print("BA")
  elif (genel_not >= 80):
        print("BB")
  elif (genel_not >= 75):
       print("CB")
  elif (genel_not >= 70):
       print("CC")
  elif (genel_not >= 65):
       print("DC")
  elif (genel_not >= 60):
       print("DD")
  elif (genel_not >= 55):
       print("FD")
  else:
       print("FF")