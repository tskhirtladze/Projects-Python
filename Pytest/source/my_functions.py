
# ტესტირება გააკეთეთ რიცხვებზე: 4, 7, 8
def is_even(number):
    return number % 2 == 0


# ტესტირება გააკეთეთ: (10, 20), (0, 0), (-5, 5)
def average(a, b):
    return (a + b) / 2


# ტესტირება გააკეთეთ რიცხვებზე: 80, 51, 41
def passed_exam(score):
    return score >= 51


# ტესტირება გააკეთეთ რიცხვებზე: 3, 1, 0
def submitted(homework_count):
    return homework_count > 0


# ტესტირება გააკეთეთ რიცხვებზე: (13, 7), (12, 6), (11, 7), (13, 5)
def can_join_club(age, grade):
    return age >= 12 and grade >= 6


class StringHelper:
    def shout(self, text):
        return text.upper()

    def reverse(self, text):
        return text[::-1]