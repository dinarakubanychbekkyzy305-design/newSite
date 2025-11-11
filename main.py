# class Animal:
#     def make_sounds(self):
#         print("Животные издает звук")

# class Dog(Animal):
#     def make_sounds(self):
#         print("гав-гав")

# class Cat(Animal):
#      def make_sounds(self):
#         print("мяу-мяу")

# animals = [Dog(), Cat(), Animal()]

# for a in animals:
#     a.make_sounds()



# override это переопределение метода создает метод с тем же именем что и у родителя но с новым поведениям




# class Bird:

#     def move(self):
#         print("Птица движется")

# class Duck(Bird):
    
#     def move(self):
#         super().move()  # вызываем поведение родителя
#         print("... и плывет по воде")


# duck = Duck()
# duck.move()


# class Cat:
#     def sound(self):
#         print("meow")

# class Dog:
#     def sound(self):
#         print("gaw")

# def animal_sound(animal):
#     animal.sound()

# cat = Cat()
# dog = Dog()

# animal_sound(cat)
# animal_sound(dog)


# print(len("python"))
# print(len([1,2,3]))
# print(len({"a": 1}))



# задача1



# class Brid:
#     def make_sound(self):
#         return("чирик")
    

# class Crow(Brid):
#     def make_sound(self):
#         return("Кар-кар")
    

# class Owl(Brid):
#     def make_sound(self):
#         return("ух-ух")
    
# birds = [Brid(), Crow(), Owl()]

# for bird in birds:
#     print(bird.make_sound())




# class printer:
#     def print_doc(self):
#         print("Печает документ")


# class scanner:
#     def print_doc(self):
#         print("Сканирует документ")

# def office_device(device):
#     device.print_doc()

# printer = printer()
# scanner = scanner()

# office_device(printer)
# office_device(scanner)