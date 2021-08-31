"""Numeric Operators!"""

__author__ = "730395784"

left: str = input( "Left-hand side: ")
right: str = input( "Right-hand side: ")
left_integer: int = int(left)
right_integer: int = int(right)
print(left + " ** " + right + " is " + str(left_integer ** right_integer))
print(left + " / " + right + " is " + str(left_integer / right_integer))
print(left + " // " + right + " is " + str(left_integer // right_integer))
print(left + " % " + right + " is " + str(left_integer % right_integer))