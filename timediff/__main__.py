import datetime as dt
import argparse
import sys


def calc_diff(args):
    try:
        print(f"time1={args.time1}, period1={args.period1}, time2={args.time2},\
              period2={args.period2}")

        # PM flag set
        if args.pmdefault:
            args.period1 = 'PM'
            args.period2 = 'PM'

        args.time1 = dt.datetime.strptime(f"{args.time1} {args.period1}",
                                          "%I:%M %p")
        args.time2 = dt.datetime.strptime(f"{args.time2} {args.period2}",
                                          "%I:%M %p")

    except ValueError:
        print("ERROR: Invalid time format. Please use HH:MM format and AM/PM \
              for periods.")
        sys.exit(1)

    # Times passed midnight
    if args.time2 < args.time1:
        args.time2 += dt.timedelta(days=1)

    return args.time2 - args.time1


def main():
    parser = argparse.ArgumentParser(description='Add two times to see the \
                                     duration.')

    # Positional arguments
    parser.add_argument('time1', help='First time (HH:MM)')
    parser.add_argument('time2', help='Second time (HH:MM)')

    # Optional periods
    parser.add_argument('period1', nargs='?', help='AM/PM for the first time')
    parser.add_argument('period2', nargs='?', help='AM/PM for the second time')

    # PM default flag
    parser.add_argument("-pmd", "--pmdefault", action="store_true",
                        help="Default times to PM if periods are not provided")

    args = parser.parse_args()

    time_diff = calc_diff(args)
    print(f"Time difference: {time_diff}")


if __name__ == "__main__":
    main()
