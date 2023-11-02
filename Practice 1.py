from ast import Add


class Pizza():
    def __init__(self, dough, sauce, filling):
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
    
class Pepperoni(Pizza):
    def __init__(self, dough, sauce, filling):
        super().__init__(dough, sauce, filling)
    
    def getInfo(self):
        return self.dough, self.sauce, self.filling

class BBQ(Pizza):
    def __init__(self, dough, sauce, filling):
        super().__init__(dough, sauce, filling)
    
    def getInfo(self):
        return self.dough, self.sauce, self.filling

class Seafood(Pizza):
    def __init__(self, dough, sauce, filling):
        super().__init__(dough, sauce, filling)
    
    def getInfo(self):
        return self.dough, self.sauce, self.filling

# Переменная с характеристикой пепперони
pepperoni = Pepperoni("Итальянское тесто", "Томатный соус", "Сыр с колбасой")  
# Переменная с характеристикой пиццы барбекью
bbq = BBQ("Дрожжевое тесто", "Соус Барбекью", "Ветчина и курица")
# Переменная с характеристикой пиццы дары моря
seafood = Seafood("Мягкое тесто", "Томатная паста", "Креветки и Кальмары")
order = ()
while True: 
    restart_inner_loop = False

    while True: 
        menu = input("Приветствуем! Выберите пиццу: \n 1. Пепперони 1500 \n 2. Барбекью 2000 \n 3. Дары Моря 2500\n")
        if menu == "1":
            cont = input(f"Характеристики пиццы: {pepperoni.getInfo()} Продолжить?")
            if cont == 1:
                order += 1500
                restart_inner_loop == True
            elif cont == 2:
                print(order)
                break
            break
        
        elif menu == "2":
            order = 2000
            print(order)
            cont = input(f"Характеристики пиццы: {bbq.getInfo()}. Продолжить?")
            if cont == 1:
                order += 2000
                restart_inner_loop == True
            elif cont == 2:
                print(order)
                break
            break

        elif menu == "3":
            order = 2500
            print(order)
            print(f"Характеристики пиццы: {seafood.getInfo()}. Продолжить?")
            if cont == 1:
                order += 2500
                restart_inner_loop == True
            elif cont == 2:
                print(order)
                break
            break
    
        else:
            print("впиши нормально")
        




