from __future__ import annotations
from abc import ABC, abstractmethod
from os import name
from random import randrange
from typing import List


class Subject(ABC):
    """
    Die Subject Klasse definiert Methoden zum managen der Observer
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Observer meldet sich beim Subject an
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Observer meldet sich beim Subjekt ab
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Benachrichtigt alle Observer ueber ein neues Event
        """
        pass


class SpotifyPlaylist(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    Liste der Subscriber. 
    In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: " + observer.name + " hinzugefuegt.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Die Subscription Management Methoden
    """

    def notify(self) -> None:
        """
        Triggered ein Update fuer jeden Subscriber
        """

        print("SpotifyPlaylist: Benachrichtigung der Oberserver...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSpotifyPlaylist: Ich mache etwas wichtiges.")
        self._state = randrange(0, 10)

        print(f"SpotifyPlaylist: Mein Status wurde geaendert zu: {self._state}")
        self.notify()


class Observer(ABC):
    """
    Das Observer Interface deklariert die Update Methoden, die von dem Subjekt benutzt wird.
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Erhalte Update vom Subjekt.
        """
        pass


"""
Jeder konkrete Observer reagiert auf das Update vom Subjekt bei dem sie aboniert haben

"""


class ConcreteObserverA(Observer):
    
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reaktion auf das Event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reaktion auf das Event")


if __name__ == "__main__":
    # The client code.

    subject = SpotifyPlaylist()

    observer_a = ConcreteObserverA("ObserverA")
    subject.attach(observer_a)

    observer_b = ConcreteObserverB("ObserverB")
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()