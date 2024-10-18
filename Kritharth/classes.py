trainerCount = 0
traineeCount = 0

class Organization:
    def __init__(self,orgName:str) -> None:
        self.orgName = orgName

    def trainerName(self,name):
        self.name = name
    
    def getName(self) -> str:
        return self.name
    
    def totalTrainee(self) -> int:
        return traineeCount
    
    def totalTrainer(self):
        return trainerCount

        

class Trainee:
    def __init__(self,name:str,course:Course) -> None:
        self.name = name
        self.course = course
        traineeCount += 1

        

class Trainer:
    def __init__(self,name:str,trainee:Trainee,orgName:Organization,course:Course) -> None:
        self.name = name
        self.trainee = []
        trainerCount += 1

    def getOrganization(self) -> str:
        return self.orgName
    
    def numberOfTrainees(self) -> int:
        return len(self.trainee)
    
class Topic:
    def __init__(self,name) -> None:
        self.name = name

class Unit:
    def __init__(self,hrs:int,topic:Topic) -> None:
            self.hrs = hrs
            self.topic = []
    
    def addTopic(self,topic:Topic):
        self.topic.append(topic)
    
    def hours(self,addHrs):
        self.hrs += addHrs
    
    def getDurationHrs(self) -> int:
        return self.hrs
    
class Module:
    def __init__(self,unit:Unit) -> None:
        self.unit = []
    
    def addUnit(self,addUnit:Unit):
        self.unit.append(addUnit)
    
class Course:
    def __init__(self,module:Module,trainer:Trainer) -> None:
        self.module = []
        self.trainer = trainer

    def  addModule(self,add:Module):
        self.module.append(add)

    def getModules(self) -> Module:
        return self.module
    
class Training:
    def __init__(self,orgName:Organization,trainer:Trainer,course:Course) -> None:
        self.orgName = orgName
        self.trainer = trainer
        self.course = course

    def addTrainee(self, trainee:Trainee):
        self.trainees.append(trainee)

    def trainee_Count(self):
        self.traineeCount = traineeCount