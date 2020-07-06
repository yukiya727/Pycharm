import threading
import keyboard
import time



def work(id, stop):
    while True:
        time.sleep(0.5)
        print("I am thread doing something")
        if stop():
            break
    print("Terminated")


def main():
    stop_threads = False
    tmp = threading.Thread(target=work, args=(1, lambda: stop_threads))
    tmp.start()

    keyboard.wait(".")
    print("done")
    stop_threads = True
    tmp.join()

if __name__ == '__main__':
    main()