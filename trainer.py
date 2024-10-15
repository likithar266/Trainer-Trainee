class Organization:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Trainer:
    def __init__(self, organization):
        self.organization = organization

    def get_organization(self):
        return self.organization.get_name()

class Trainee:
    def __init__(self, name):
        self.name = name

class Topic:
    def __init__(self, name):
        self.name = name

class Unit:
    def __init__(self, duration_hrs):
        self.duration_hrs = duration_hrs
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def get_duration_hrs(self):
        return self.duration_hrs

class Module:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def get_units(self):
        return self.units

class Course:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def get_modules(self):
        return self.modules

class Training:
    def __init__(self, organization, trainer, course):
        self.organization = organization
        self.trainer = trainer
        self.course = course
        self.trainees = []

    def add_trainee(self, trainee):
        self.trainees.append(trainee)

    def get_num_of_trainees(self):
        return len(self.trainees)

    def get_training_organization_name(self):
        return self.organization.get_name()

    def get_training_duration_hrs(self):
        total_duration = 0
        for module in self.course.get_modules():
            for unit in module.get_units():
                total_duration += unit.get_duration_hrs()
        return total_duration

# Test Main
if __name__ == "__main__":
    # Create Organization
    org = Organization("TechCorp")

    # Create Trainer
    trainer = Trainer(org)

    # Create Course structure
    course = Course()
    module1 = Module()
    unit1 = Unit(2)  # 2 hours duration
    unit1.add_topic(Topic("Introduction"))
    unit1.add_topic(Topic("Basics"))
    module1.add_unit(unit1)

    unit2 = Unit(3)  # 3 hours duration
    unit2.add_topic(Topic("Advanced Concepts"))
    module1.add_unit(unit2)

    course.add_module(module1)

    # Create Training
    training = Training(org, trainer, course)

    # Add Trainees
    training.add_trainee(Trainee("Alice"))
    training.add_trainee(Trainee("Bob"))
    training.add_trainee(Trainee("Charlie"))

    # Display results
    print(f"Number of trainees: {training.get_num_of_trainees()}")
    print(f"Training organization: {training.get_training_organization_name()}")
    print(f"Total training duration: {training.get_training_duration_hrs()} hours")