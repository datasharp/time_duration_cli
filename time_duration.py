import datetime as dt
import argparse


def calc_diff(time1, period1, time2, period2):
    time1 = dt.datetime.strptime(f"{time1} {period1}", "%I:%M %p")
    time2 = dt.datetime.strptime(f"{time2} {period2}", "%I:%M %p")

    if time2 < time1:
        time2 += dt.timedelta(days=1)

    return time2 - time1


def main():
    parser = argparse.ArgumentParser(description='Add two times to see the \
                                     duration.')
    parser.add_argument('time1',
                        help='First time (HH:MM)')
    parser.add_argument('period1',
                        help='AM/PM for the first time')
    parser.add_argument('time2',
                        help='Second time (HH:MM)')
    parser.add_argument('period2',
                        help='AM/PM for the second time')
    args = parser.parse_args()

    time_diff = calc_diff(args.time1, args.period1, args.time2, args.period2)

    print(f"Time difference: {time_diff}")


if __name__ == "__main__":
    main()
