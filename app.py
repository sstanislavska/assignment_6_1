# CLI app - a simple calculator

import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        print("You can't divide by zero")
        exit()
    return x / y


parser = argparse.ArgumentParser(description="CLI app - a simple calculator")
parser.add_argument("x", type=float, help="Input x")
parser.add_argument("y", type=float, help="Input y")
args = parser.parse_args()

print(f"x + y = {add(args.x, args.y)}")
print(f"x - y = {subtract(args.x, args.y)}")
print(f"x / y = {divide(args.x, args.y)}")
