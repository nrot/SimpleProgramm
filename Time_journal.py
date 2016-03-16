__author__ = 'nrot'

# -*- coding: utf-8 -*-

import time


def take_now_day():
    time.strftime("%Y_%m_%d", time.gmtime(time.time()))


def take_now_time():
    time.strftime("%Y %m %d %H %M %S", time.gmtime(time.time()))


def take_dif_time(t1, t2):
    t = t2 - t1
    t = time.gmtime(t)
    t = [t[i] - time.gmtime(0)[i] for i in range(9)]
    s = 0
    re = ["years=", "mons=", "days=", "hours=", "mins="] # u can edit this like add in end "seconds="
    while t[s] == 0:
        s += 1
    re = re[s:len(re) - 1]
    for i in range(s, len(re)):
        re[i - s] += str(t[i])
    return ";".join(re) + ";"


def main():
    import argparse

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("file", help="Journal file", default="journal", nargs='?')
    group.add_argument("-d", "--day", help="Create journal for everyday")
    args = parser.parse_args()

    if args.day:
        name_file = args.file + take_now_day()
    else:
        name_file = args.file

    try:
        journal = open(name_file, "at")
    except:
        journal = open(name_file, "wt")

    global_work = True
    start_time = None
    while global_work:
        print(":", end="")
        command = str(input()).lower().strip()
        # print(command)
        if command == "start":
            if start_time is None:
                start_time = time.time()
                journal.write("".join(["#" for i in range(127)]) + "\n")
                journal.write("Start work: {time} \n".format(time=time.ctime(start_time)))
            else:
                print("Work already start")
        elif command == "stop":
            if start_time is not None:
                end_time = time.time()
                print("Write what u doing in this time:")
                work = str(input())
                journal.write(work + "\n")
                journal.write("End work: {time} \n".format(time=time.ctime(end_time)))
                journal.write("Take time: {time} \n".format(time=take_dif_time(start_time, end_time)))
                journal.write("".join(["#" for i in range(127)]) + "\n")
                start_time = None
            else:
                print("Work not start")
        elif command == "exit":
            if start_time is not None:
                print("U not stop work. Save and exit or just exit? (answer: s,e)")
                answer = str(input())
                if answer == "s":
                    end_time = time.time()
                    print("Write what u doing in this time:")
                    work = str(input())
                    journal.write(work + "\n")
                    journal.write("End work: {time} \n".format(time=time.ctime(end_time)))
                    journal.write("Take time: {time} \n".format(time=take_dif_time(start_time, end_time)))
                    journal.write("".join(["#" for i in range(127)]) + "\n")
                    start_time = None
                    journal.close()
                    print("Good bye")
                    exit()
                elif answer == "e":
                    journal.close()
                    print("Good bye")
                    exit()
            else:
                print("Good bye")
                exit()
        else:
            print("U print this: " + command)
            print("U can print smth like this {'start', 'stop', 'exit'}")

if __name__ == "__main__":
    main()
