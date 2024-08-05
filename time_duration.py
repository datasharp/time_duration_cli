import datetime as dt
import argparse


def calc_diff(time1, time2):
    time1 = time1.split(':')
    time1 = dt.datetime.combine(dt.date.today(), dt.time(hour=int(time1[0]),
                                                         minute=int(time1[1])))

    time2 = time2.split(':')
    time2 = dt.datetime.combine(dt.date.today(), dt.time(hour=int(time2[0]),
                                                         minute=int(time2[1])))

    time_diff = time2 - time1
    return time_diff


def main():
    parser = argparse.ArgumentParser(description='Add two times to see the \
                                     duration.')
    parser.add_argument('time1', help='first time for the duration \
                        calculation (HH:MM)')
    parser.add_argument('time2', help='second time for the duration\
                        calculation (HH:MM)')
    args = parser.parse_args()

    time_diff = calc_diff(args.time1, args.time2)

    print(f"Time difference: {time_diff}")


if __name__ == "__main__":
    main()
