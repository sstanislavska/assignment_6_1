# CLI app - a simple calculator

import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplicate(x, y):
    return x * y


parser = argparse.ArgumentParser(description="CLI app - a simple calculator")
parser.add_argument("x", type=float, help="Input x")
parser.add_argument("y", type=float, help="Input y")
args = parser.parse_args()

print(f"x + y = {add(args.x, args.y)}")
print(f"x - y = {subtract(args.x, args.y)}")
print(f"x * y = {multiplicate(args.x, args.y)}")
