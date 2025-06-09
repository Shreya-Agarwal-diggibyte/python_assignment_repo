from src.time_delta.util import time_delta
def main():
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))
if __name__ == "__main__":
    main()