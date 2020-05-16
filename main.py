import threading

from camera_stream import camera_stream

N_CAMS = 1


class camThread(threading.Thread):
    def __init__(self,camID):
        threading.Thread.__init__(self)
        self.camID = camID

    def run(self):
        print("Starting " + self.preview_name + "\n")
        camera_stream(self.preview_name, self.camID)


if __name__ == "__main__":

    threads = []
    for i in range(N_CAMS):
        threads.append(camThread(i))
        threads[i].start()

    print(f'num threads  {threading.active_count()}', threads)