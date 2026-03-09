def get_university_courses():
    university_courses_code = input("Enter the university courses code separated by commas: ")
    while True:
        course_codes = [code.strip() for code in university_courses_code.split(",")]
        if not course_codes or all(code == "" for code in course_codes):
            print("Input cannot be empty or contain only empty strings. Please enter valid course codes.")
            university_courses_code = input("Enter the university courses code separated by commas: ")
        else:
            return course_codes

course_codes = get_university_courses()


def is_valid_course_code(code: str) -> bool:
    """
    Return True if `code` matches 2-3 uppercase letters followed by 3 digits.

    Examples: TEC001, AU006
    """
    import re
    return bool(re.fullmatch(r'[A-Z]{2,3}\d{3}', code))


if __name__ == '__main__':
    # simple tests
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