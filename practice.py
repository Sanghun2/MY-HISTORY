# 2. 클래스에 길이 두 개를 입력받는 생성자를 만들고 넓이 함수와 둘레함수를 만든다.
# 3. 넓이 함수로 출력
# 4. 둘레함수로 출력
class rectangular:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        ment = f'길이가 {a},{b}인 사각형이 만들어졌습니다.'
        print(ment)

    def Area(self, a, b):
        print("넓이는 ", a*b)

    def Perimeter(self, a, b):
        print("둘레는 ", (2*a + 2*b))

rec1 = rectangular(3, 5)
rec1.Area(3,5)
rec1.Perimeter(3,5)


# 1. Animals 클래스를 만든다.
# 2. 생성자로 이름과 동물을 입력한다.
# 3. 상속을 받아 개 클래스를 만든다.
# 4, 상속을 받아 고양이 클래스를 만든다.
# 5. 개 클래스에서 왈왈 함수를 만든다.
# 6. 고양이 클래스에서 양옹 함수를 만든다.

class Animals:
    def __init__(self, Name, Kind):
        self.Name = Name
        self.Kind = Kind

class Dog(Animals):
    def bark(self):
        print(f"왈왈! {self.Kind}입니다.")

class Cat(Animals):
    def cry(self):
        print(f"야옹~ {self.Kind}입니다.")

dog1 = Dog('바둑', '개')
dog1.bark()
cat1 = Cat('먀옹이', '고양이')
cat1.cry()