import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

def main():
    # 把 function 轉成可多線程執行的 thread，並建立5個子執行緒
    threads = []
    for i in range(5):
        number = i
        # target 為 function; args 為function參數，須為 tuple 且一定要有逗號
        threads.append(threading.Thread(target=do_job, args=(number,)))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Done')


main()