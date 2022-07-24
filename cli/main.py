import curses
import sys
from time import sleep
import json
import redis
import requests


def get(host, func):
    res = r.hget(host, func)
    return res.decode() if res else ""


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, bg)
    curses.init_pair(2, curses.COLOR_GREEN, bg)
    curses.init_pair(3, curses.COLOR_WHITE, bg)
    stdscr.clear()
    stdscr.refresh()
    # print(curses.LINES - 1, curses.COLS - 1)
    # t = 0
    while True:
        cur = 0
        # stdscr.addstr(0, 0, str(t))
        for host in hosts:
            pad = curses.newpad(HEIGHT, curses.COLS - 1)
            pad.addstr(0, 0, f"{host['name']} ({host['addr']})")
            line = 1
            for f in host["bool_functions"]:
                data = get(host["addr"], f)
                if data == "true":
                    pad.addstr(line, 0, f + "\n", curses.color_pair(2))
                else:
                    pad.addstr(line, 0, f + "\n", curses.color_pair(1))
                    curses.beep()
                line += 1
            pad.bkgd(" ", curses.color_pair(3))
            pad.refresh(
                0,
                0,
                HEIGHT * (cur % N_PER_COL),
                WIDTH * (cur // N_PER_COL),
                curses.LINES - 1,
                curses.COLS - 1,
            )
            cur += 1

        stdscr.refresh()
        # t += 1
        # k = stdscr.getch()
        sleep(1)


if __name__ == "__main__":
    hosts = json.loads(requests.get("http://localhost/api/hosts").text)
    # print(hosts)
    r = redis.Redis(host="localhost", port=6379, db=0)
    bg = curses.COLOR_BLACK
    HEIGHT = 12
    WIDTH = 60
    N_PER_COL = 3
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Bye")
        sys.exit()
