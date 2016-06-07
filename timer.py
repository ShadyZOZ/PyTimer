from tkinter import *
import time
import winsound
import os

class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec = 100
    countdown = 15 * 60
    soundfile1 = os.path.join(os.getcwd(), 'Windows Exclamation.wav')
    soundfile2 = os.path.join(os.getcwd(), 'Windows Ringin.wav')
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        '''制作时间标签'''
        l = Label(self, textvariable = self.timestr, font='Helvetica -180')
        self._setTime(self._elapsedtime)
        l.pack(fill = 'both', expand = YES)
    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)
        if self.countdown - self._elapsedtime < 0.01:
            self.PlaySound2()
            self.after_cancel(self._timer)
            self._running = False
    def _setTime(self, elap):
        '''将时间格式改为 分：秒：百分秒'''
        elap = self.countdown - elap
        minutes = int(elap/60)
        seconds = int(elap-minutes*60.0)
        # hseconds = int((elap - minutes*60.0 - seconds) *100)
        if minutes == 5 and seconds == 0:
            self.PlaySound1()
        if minutes == 1 and seconds == 0:
            self.PlaySound1()
        if len(str(minutes)) == 1:
            minutes = '0' + str(minutes)
        if len(str(seconds)) == 1:
            seconds = '0' + str(seconds)
        self.timestr.set('%s:%s' % (minutes, seconds))
    def Start(self):
        if not self._running and self.countdown - self._elapsedtime >= 0.01:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False
    def Reset(self):
        '''重设秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._running = False
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
    def PlaySound1(self):
        winsound.PlaySound(self.soundfile1,winsound.SND_ASYNC)
    def PlaySound2(self):
        winsound.PlaySound(self.soundfile2,winsound.SND_ASYNC)
        
        
if __name__ == '__main__':
    def main():
        root = Tk()
        root.title('timer')
        root.geometry('800x600')
        root.rowconfigure(0, weight=4)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=2)
        root.columnconfigure(4, weight=1)
        root.columnconfigure(5, weight=2)
        root.columnconfigure(6, weight=1)
        # root.columnconfigure(3, weight=1)
        # Label(root, bg='white', ).grid(row=0, column=0, rowspan=3 , columnspan=7, sticky=W+E+N+S)
        sw = StopWatch(root)
        sw.grid(row=0, columnspan=7, sticky=W+E+N+S)
        Button(root, text = 'start', font='Helvetica -22', fg="green", command = sw.Start).grid(row=1, column=1, sticky=W+E+N+S)
        Button(root, text = 'pause', font='Helvetica -22', fg="red", command = sw.Stop).grid(row=1, column=3, sticky=W+E+N+S)
        Button(root, text = 'reset', font='Helvetica -22', fg="blue", command = sw.Reset).grid(row=1, column=5, sticky=W+E+N+S)
        Button(root, text = '声音测试1', font='Helvetica -22', command = sw.PlaySound1).grid(row=2, column=2)
        Button(root, text = '声音测试2', font='Helvetica -22', command = sw.PlaySound2).grid(row=2, column=4)
        # Button(root, text = 'quit', command = root.quit).grid(row=1, column=3, sticky=W+E+N+S)
        root.mainloop()
    main()