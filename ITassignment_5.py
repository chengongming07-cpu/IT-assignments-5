#Excersise 1:
def is_valid_course_code(code: str) -> bool:
    """
    Return True if `code` matches 2-3 uppercase letters followed by 3 digits.

    Examples: TEC001, AU006
    """
    import re
    return bool(re.fullmatch(r'[A-Z]{2,3}\d{3}', code))


if __name__ == '__main__':
    tests = {
        "TEC001": True,
        "AU006": True,
        "A006": False,
        "TE0011": False,
        "tec001": False,
        "TE C001": False,
        "AB123": True,
        "ABC999": True,
        "AB12": False,
    }
    for s, expected in tests.items():
        result = is_valid_course_code(s)
        print(f"{s}: {result} (expected {expected})")


#Exercise 2:
Web_color = input("Enter a web color code:")
def is_valid_web_color(color: str) -> bool:
    import re
    return bool(re.fullmatch(r'#[A-F0-9]{6}', color))

if __name__ == '__main__':
    print(is_valid_web_color(Web_color))    

#Exercise 3:
paragraph = input("Enter a paragraph:")
def sum_of_numbers_in_paragraph(paragraph: str) -> int:
    import re
    numbers = re.findall(r'\d+', paragraph)
    return sum(int(num) for num in numbers)

if __name__ == '__main__':
    print(sum_of_numbers_in_paragraph(paragraph))


#Exercise 4:
def hide_phone_numbers(text: str) -> str:
    import re
    return re.sub(r'\+84\d{9}|\d{10}', '*', text)
if __name__ == '__main__':    input_text = input("Enter a string with phone numbers:")
print(hide_phone_numbers(input_text))

#Exercise 5:
import random
def estimate_pi(num_points: int) -> float:
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4
if __name__ == '__main__':    num_points = int(input("Enter the number of random points to generate:"))
print(estimate_pi(num_points))
 
