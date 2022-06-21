text = input()
if text in ["Привет", "Здарова", "Хеллоу"]:
  print(random.choice(["Здрасте", "Йоу", "Приветики"]))
elif text in ["Пока", "Увидимся", "Чао"]:
  print(random.choice(["Буду ждать нашей встречи", "Ок", "Бай-бай"]))
else:
  print("Не понял")