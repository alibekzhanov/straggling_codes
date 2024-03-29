from __future__ import annotations


class ComplexNumber:
    def __init__(self, real: int, img: str) -> None:
        """Создает 2 аттрибута real: int, img: int"""
        self.real = real
        self.img = img

    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть складывается с реальной, воображаемая с воображаемой"""
        return ComplexNumber(self.real + cx.real, self.img + cx.img)

    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть отнимается с реальной, воображаемая с воображаемой"""
        return ComplexNumber(self.real - cx.real, self.img - cx.img)

    def __repr__(self) -> str:
        """Возвращает в формате: 5 + 7j"""
        return f"{self.real} + {self.img}j"
    
    def __iadd__(self, cx: ComplexNumber) -> ComplexNumber:
        self.real += cx.real
        self.img += cx.img
        return self

    def __isub__(self, cx: ComplexNumber) -> ComplexNumber:
        self.real -= cx.real
        self.img -= cx.img
        return self

    def __eq__(self, cx: ComplexNumber) -> bool:
        return self.real == cx.real and self.img == cx.img


c1 = ComplexNumber(5, 7)
c2 = ComplexNumber(3, 2)

# Сложение
c3 = c1 + c2
print(c3)  # 8 + 9j

# Вычитание
c4 = c1 - c2
print(c4)  # 2 + 5j

# Сложение на месте
c1 += c2
print(c1)  # 8 + 9j

# Вычитание на месте
c1 -= c2
print(c1)  # 5 + 7j

# Сравнение
print(c1 == c2)  # False

# __add__ +
# __sub__ -
# __iadd__ +=
# __isub__ -=
# __eq__ ==