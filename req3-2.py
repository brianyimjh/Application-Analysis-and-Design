class Hotel:
    def __init__(self, reviews):
        self._reviews = reviews

    def getReviews(self):
        return self._reviews

    def displayReviews(self):
        for review in reversed(self.getReviews()):
            aReview = review
            aReview.display()

def main():
    print('hello world')

if __name__ == '__main__':
    main()