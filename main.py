from student import Student

lajos = Student("Lajos", 13, 178, "fiu")
anna  = Student("Anna", 15, 167, "lany")


print(lajos.height)
print(lajos.name)
print(lajos.score)
lajos.learn(10)
lajos.learn(10)
print(lajos)
print(lajos.score)
print(anna)
print(anna.score)


print(anna.introduce())
print(lajos.introduce())