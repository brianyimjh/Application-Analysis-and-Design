class OrchestratingClass:
    def __init__(self, hotels):
        self._hotels = hotels

    def getHotel(self, hotelName):
        return self._hotels.get(hotelName)

    def displayReviews(self, hotelName):
        aHotel = self.getHotel(hotelName)
        aHotel.displayReviews()

def main():
    print('hello world')

if __name__ == '__main__':
    main()