import abc

from pyparsing import abstractmethod

class IAgent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_action(self, state: tuple) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def add(self, state, action, reward) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def update(self) -> None:
        raise NotImplementedError()