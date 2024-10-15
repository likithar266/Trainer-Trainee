# Organization class
class Organization:
    def __init__(self, name):
        self.name = name
        self.trainees = []  # List to keep track of trainees

    def getName(self):
        return self.name

    def addTrainee(self, trainee):
        self.trainees.append(trainee)

    def getNumOfTrainees(self) -> int:
        return len(self.trainees)

# Trainer class
class Trainer:
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization

    def getOrganization(self):
        return self.organization.getName()


# Trainee class
class Trainee:
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization
        organization.addTrainee(self)  # adding the trainee to the organization

    def getOrganization(self):
        return self.organization.getName()

