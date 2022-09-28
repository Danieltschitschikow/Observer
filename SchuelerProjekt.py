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
    
    _observers: List[IObserver] = []
    """
    Liste der Subscriber.
    In einem Anwendungsbeispiel koennte man die Liste auch auf einer Datenbank speichern.
    """

    #TODO: Abstrakte Methoden implementieren

    def song_hinzufuegen(self) -> None:
        """
        Business Logik
        """

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

class ObserverA(IObserver):
    """
        Hier koennte man Business Logik einfuehren und zum Beispiel nur bei bestimmten States
        reagieren. Am Bespiel von Spotify dem Benutzer jedes mal eine Nachricht schicken,
        wenn ein neues Lied zur Playlist hinzugefuegt wurde oder nur benachrichtigen, wenn
        die Playlist umbenannt wird.
        """
    #TODO: Interface implementieren


class ObserverB(IObserver):
    """
        Hier koennte man Business Logik einfuehren und zum Beispiel nur bei bestimmten States
        reagieren. Am Bespiel von Spotify dem Benutzer jedes mal eine Nachricht schicken,
        wenn ein neues Lied zur Playlist hinzugefuegt wurde oder nur benachrichtigen, wenn
        die Playlist umbenannt wird.
        """
    #TODO: Interface implementieren


if __name__ == "__main__":

    subject = SpotifyPlaylist()

    observer_a = ObserverA("ObserverA")
    subject.attach(observer_a)

    observer_b = ObserverB("ObserverB")
    subject.attach(observer_b)
    
    subject.song_hinzufuegen()

    subject.detach(observer_a)

    subject.song_hinzufuegen()