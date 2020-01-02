import threading
import os

import transit
import solar
import air_quality
import atc

def main():
    prog = [transit, solar, air_quality, atc]

    print(os.getenv('PRAVAH_DB_USERNAME'))
    print(os.getenv('PRAVAH_DB_PASSWORD'))

    for p in prog:
        threading.Thread(target=start_prog, args=(p,)).start()

def start_prog(prog):
    prog.start()

if '__main__' == __name__:
    main()