from abc import ABC, abstractmethod

class Subject(ABC):
    abstractmethod
    def registerObserver(self, observerObj):
        pass

    abstractmethod
    def removeObserver(self, observerObj):
        pass

    abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    abstractmethod
    def update(self, subject):
        pass

class Student(Observer):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def update(self, confirmedCourse):
        self.sendEmail(confirmedCourse)

    def sendEmail(self, confirmedCourse):
        # Simulated email
        print(f'''
        To: {self._email}

        Dear {self._name},

        Please enroll into the following course:
        
        Course ID: {confirmedCourse.id}
        Course Name: {confirmedCourse.name}

        Thank you.
        ''')

class Course(Subject):
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._observers = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    # Administrator confirms course
    def confirm(self):
        self.notifyObservers()

    # Student register interest for a course
    def registerObserver(self, observerObj):
        self._observers.append(observerObj)

    def removeObserver(self, observerObj):
        self._observers.remove(observerObj)

    def notifyObservers(self):
        for o in self._observers:
            o.update(self)

def main():
    aCourse = Course('ICT340', 'Coding')
    studentA = Student('Brian Yim', 'brianyimjh@gmail.com')
    studentB = Student('Alex Ong', 'alex.ong@gmail.com')

    aCourse.registerObserver(studentA)
    aCourse.registerObserver(studentB)

    aCourse.confirm()

if __name__ == '__main__':
    main()