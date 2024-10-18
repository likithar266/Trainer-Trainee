class Organization:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Trainer:
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization

    def getOrganization(self):
        return self.organization.getName()

class Trainee:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules

    def getModules(self):
        return self.modules

class Module:
    def __init__(self, name, units):
        self.name = name
        self.units = units
      
    def getUnits(self):
        return self.units
    
class Unit:
    def __init__(self, name, durationInHrs):
        self.name = name
        self.durationInHrs = durationInHrs

    def getDurationHrs(self):
        return self.durationInHrs

class Training:
    def __init__(self, trainees, trainer, course, organization):
        self.trainees = trainees
        self.trainer = trainer
        self.course = course
        self.organization = organization

    def getNumOfTrainees(self):
        return len(self.trainees)

    def getTrainingOrganizationName(self):
        return self.organization.getName()

    def getTrainingDurationInHrs(self):
        totalDuration = 0
        for module in self.course.getModules():
            for unit in module.getUnits():
                totalDuration += unit.getDurationHrs()
        return totalDuration

def main():
    org = Organization('Sahyadri')
    trainer = Trainer('John', org)
  
    # Units
    unit1 = Unit('Introduction', 2)
    unit2 = Unit('Loops', 3)

    # Modules
    module1 = Module('Basics', [unit1])
    module2 = Module('Advanced', [unit2])

    # Course
    course = Course('Python', [module1, module2])

    # Trainees
    trainees = [Trainee('Yahya'), Trainee('Mihir')]

    # Training
    training = Training(trainees, trainer, course, org)

    # Output results
    print('Number of Trainees =', training.getNumOfTrainees())
    print('Training Organization Name =', training.getTrainingOrganizationName())
    print('Total Training Duration in Hrs =', training.getTrainingDurationInHrs())

main()
