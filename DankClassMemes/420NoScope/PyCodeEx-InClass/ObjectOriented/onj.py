class ballon:
    def __inti__(self):
        self.altitude = 0

    def climb(self):
        self.altitude += 1

    def dive(self):
        if self.altitude > 0:
            self.altitude -= 1

    def crashland(self):
        self.altitude = 0

    def setaltitude(self, newaltitude):
        if newaltitude >= 0:
            self.atlitude = newaltitude

    def getaltitude(self):
        return self.altitude

    def __str__(self):
        return 'Current altitude: {}'.format(self.altitude)

if __name__ == '__main__':
    b = balloon()
    b.setaltitude(10000)
    print(b.getaltitude())
    b.climb()
    b.climb()
    b.climb()
    b.dive()
    b.climb()
    b.climb()
    b.climb()
    print(b)
    b.crashland()
    print(b)
    del b
