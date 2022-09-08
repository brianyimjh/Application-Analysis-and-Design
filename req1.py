class OrchestratingClass:
    def __init__(self, courses, professors):
        self._courses = courses
        self._professors = professors

    def getCourse(self, course_id):
        return self._courses.get(course_id)

    def getProfessor(self, professor_name):
        return self._professors.get(professor_name)

    def addProfessor(self, course_id, professor_name):
        aCourse = self.getCourse(course_id)
        specialtyArea = aCourse.retrieveSpecialtyArea()

        aProfessor = self.getProfessor(professor_name)
        listOfExpertise = aProfessor.retrieveListOfExpertise()

        for expertise in listOfExpertise:
            expertiseName = expertise.getName()

            if specialtyArea == expertiseName:
                aCourse.addProfessor(aProfessor)

def main():
    pass

if __name__ == '__main__':
    main()