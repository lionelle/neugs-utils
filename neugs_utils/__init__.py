from .tier_grading import TierMasteryJSONTestRunner, tier, \
    COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR


__version__ = "0.0.1"
__doc__ = """
A simple tool set developed for non-traditional grading and other grading 
tools within the grade-scope autograder environment.
"""

# Developed by Mark Miller for Khoury Align SF campus use. Placed for easy access.

common_style_ignore_list = [
    'E121', # Continuation line under-indented for hanging indent
    'E126', # Continuation line over-indented for hanging indent
    'W291', # Trailing whitespace
    'W503', # Line break before binary operator
    'W504' # Line break after binary operator
    ]
