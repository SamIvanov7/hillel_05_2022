import functools

# # MODIFY THIS DECORATOR
# def reverse_string(func):
#     """If output is a string, reverse it. Otherwise, return None."""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper

# # TARGET FUNCTIONS
# @reverse_string
# def get_university_name() -> str:
#     return "Western Institute of Technology and Higher Education"

# @reverse_string
# def get_university_founding_year() -> int:
#     return 1957

# # TEST OUPUT
# print(
#     get_university_name(),
#     get_university_founding_year(),
#     sep="\n"
# )
# +++++++++++++++++++++++++++++++++++++++++++++++++


def reverseString(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        smString = func()
        if isinstance(smString, str):
            smStringReversed = smString[::-1]
            return smStringReversed
        return None

    return wrapper


@reverseString
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverseString
def get_university_founding_year() -> int:
    return 1957


print(get_university_name(), get_university_founding_year(), sep="\n")
