from abc import ABC, abstractmethod


class ISeeingWalkable(ABC):
    @abstractmethod
    def see(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class ISeeing(ABC):
    @abstractmethod
    def see(self):
        pass


class IWalkable:
    @abstractmethod
    def walk(self):
        pass


class Person(ISeeing, IWalkable):
    def see(self):
        print("This person see you")

    def walk(self):
        print("this prrson walking")


class BlindPerson(ISeeingWalkable):
    def walk(self):
        print("this prrson walking")

    def see(self):
        raise Exception("Blind persons cannot see anythong")


l: [IWalkable] = []