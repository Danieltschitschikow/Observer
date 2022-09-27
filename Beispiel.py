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
    def attach(self, observer: IObserver) -> None:
        """
        Observer meldet sich beim Subject an
        """
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
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
    """
    Verschiedene Dinge, die die SpotifyPlaylist tun kann
    """

    _events= {
        1: "Song hinzugefuegt",
        2: "Name der Playlist geaendert",
        3: "Song entfernt"}

    _observers: List[IObserver] = []
    """
    Liste der Subscriber. 
    In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: IObserver) -> None:
        print("Subject: " + observer.name + " hinzugefuegt.")
        self._observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        print(observer.name + " wurde aus der Aboliste entfernt.")
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
            

    def song_hinzufuegen(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSpotifyPlaylist: Ich habe einen Song zur Playlist hinzugefuegt.")
        self._state = randrange(0, 10)
        
        print(f"SpotifyPlaylist: Mein Status wurde geaendert zu: {self._state}")
        self.notify()

    def song_entfernen(self) -> None:
        print("\nSpotifyPlaylist: Ich habe einen Song zur Playlist hinzugefuegt.")
        self._state = randrange(0, 10)
        
        print(f"SpotifyPlaylist: Mein Status wurde geaendert zu: {self._state}")
        self.notify()


class IObserver(ABC):
    """
    Das IObserver Interface deklariert die Update Methoden, die von dem Subjekt benutzt wird.
    """
    def __init__(self, name, ):
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


class Observer(IObserver):
    
    def update(self, subject: Subject,) -> None:
        """
        Hier koennte man Business Logik einfuehren und zum Beispiel nur bei bestimmten States
        reagieren. Am Bespiel von Spotify dem Benutzer jedes mal eine Nachricht schicken,
        wenn ein neues Lied zur Playlist hinzugefuegt wurde oder nur benachrichtigen, wenn
        die Playlist umbenannt wird.
        """
        print("ObserverA: Reaktion auf das Event")


class ObserverB(IObserver):
    def update(self, subject: Subject) -> None:
        print("ObserverB: Reaktion auf das Event")


if __name__ == "__main__":
    # The client code.

    subject = SpotifyPlaylist()

    observer_a = Observer("ObserverA")
    subject.attach(observer_a)

    observer_b = Observer("ObserverB")
    subject.attach(observer_b)
    
    subject.song_hinzufuegen()

    subject.detach(observer_a)

    subject.song_hinzufuegen()