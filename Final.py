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
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization

    def getOrganization(self):
        return self.organization.getName()

class Training:
    def __init__(self, organization, course):
        self.organization = organization
        self.course = course
        self.trainees = []

    def addTrainee(self, trainee):
        self.trainees.append(trainee)

    def getNumOfTrainees(self):
        return len(self.trainees)

    def getTrainingOrganizationName(self):
        return self.organization.getName()

    def getTrainingDurationHrs(self):
        return self.course.getTotalDuration()

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def addModule(self, module):
        self.modules.append(module)

    def getModules(self):
        return self.modules

    def getTotalDuration(self):
        return sum(module.getTotalDuration() for module in self.modules)

class Module:
    def __init__(self, name):
        self.name = name
        self.units = []

    def addUnit(self, unit):
        self.units.append(unit)

    def getUnits(self):
        return self.units

    def getTotalDuration(self):
        return sum(unit.getDurationHrs() for unit in self.units)

class Unit:
    def __init__(self, name, duration_hrs):
        self.name = name
        self.duration_hrs = duration_hrs
        self.topics = []

    def addTopic(self, topic):
        self.topics.append(topic)

    def getDurationHrs(self):
        return self.duration_hrs

class Topic:
    def __init__(self, name):
        self.name = name

def get_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    # Create Organization
    org_name = get_input("Enter organization name: ")
    org = Organization(org_name)

    # Create Trainer
    trainer_name = get_input("Enter trainer name: ")
    trainer = Trainer(trainer_name, org)

    # Create Course
    course_name = get_input("Enter course name: ")
    course = Course(course_name)

    # Create Course structure
    num_modules = get_input("Enter number of modules: ", int)

    for i in range(num_modules):
        module_name = get_input(f"Enter name for Module {i+1}: ")
        module = Module(module_name)
        num_units = get_input(f"Enter number of units for Module {i+1}: ", int)

        for j in range(num_units):
            unit_name = get_input(f"Enter name for Unit {j+1} of Module {i+1}: ")
            duration = get_input(f"Enter duration (in hours) for Unit {j+1} of Module {i+1}: ", int)
            unit = Unit(unit_name, duration)

            num_topics = get_input(f"Enter number of topics for Unit {j+1} of Module {i+1}: ", int)
            for k in range(num_topics):
                topic_name = get_input(f"Enter name for Topic {k+1} of Unit {j+1}, Module {i+1}: ")
                unit.addTopic(Topic(topic_name))

            module.addUnit(unit)

        course.addModule(module)

    # Create Training
    training = Training(org, course)

    # Add Trainees
    num_trainees = get_input("Enter number of trainees: ", int)
    for i in range(num_trainees):
        trainee_name = get_input(f"Enter name for Trainee {i+1}: ")
        trainee = Trainee(trainee_name, org)
        training.addTrainee(trainee)

    # Display results
    print("\n--- Training Details ---")
    print(f"Training Organization: {training.getTrainingOrganizationName()}")
    print(f"Trainer: {trainer.name}")
    print(f"Course Name: {course.name}")
    print(f"Number of Trainees: {training.getNumOfTrainees()}")
    print(f"Total Training Duration: {training.getTrainingDurationHrs()} hours")

    # Display course structure
    print("\n--- Course Structure ---")
    print(f"Course: {course.name}")
    for i, module in enumerate(course.getModules(), 1):
        print(f"\nModule {i}: {module.name}")
        for j, unit in enumerate(module.getUnits(), 1):
            print(f"  Unit {j}: {unit.name} (Duration: {unit.getDurationHrs()} hours)")
            for k, topic in enumerate(unit.topics, 1):
                print(f"    Topic {k}: {topic.name}")
