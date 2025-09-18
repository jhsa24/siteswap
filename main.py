from aux import lists_with_sum
import argparse

def siteswap(num, len, height):
    potential_siteswaps = lists_with_sum(num * len, len, height)
    valid_siteswaps = []

    for siteswap in potential_siteswaps:
        pass

    return valid_siteswaps

def main():
    parser = argparse.ArgumentParser(description = 'Siteswap Generator')

    parser.add_argument("num", type=int, help="choose how many balls the pattern is for")
    parser.add_argument("length", type=int, help="choose how many throws need to be made before the pattern repeats itself")
    parser.add_argument("height", type=int, help="choose the highest allowable throw in the pattern")

    args = parser.parse_args()

    print(f"received thefollowing arguments: num = {args.num}, length = {args.length}, height = {args.height}")
    return siteswap(args.num, args.length, args.height)

if __name__ == "__main__":
    print(main())
