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
    Das Subjekt kann verschiedene Stati einnehmen und die Observer ueber den Status informieren
    """
    """
    Verschiedene Dinge, die die SpotifyPlaylist tun kann
    """
    
    _observers: List[IObserver] = []
    """
    Liste der Subscriber.
    In einem Anwendungsbeispiel koennte man die Liste auch auf einer Datenbank speichern.
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


"""
Jeder konkrete Observer reagiert auf das Update vom Subjekt bei dem sie aboniert haben

"""



class ObserverA(IObserver):
    """
        Hier koennte man Business Logik einfuehren und zum Beispiel nur bei bestimmten States
        reagieren. Am Bespiel von Spotify dem Benutzer jedes mal eine Nachricht schicken,
        wenn ein neues Lied zur Playlist hinzugefuegt wurde oder nur benachrichtigen, wenn
        die Playlist umbenannt wird.
        """
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print(self.name + ": Reacted to the event")


class ObserverB(IObserver):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print(self.name + ": Reacted to the event")


if __name__ == "__main__":

    subject = SpotifyPlaylist()

    observer_a = ObserverA("ObserverA")
    subject.attach(observer_a)

    observer_b = ObserverB("ObserverB")
    subject.attach(observer_b)
    
    subject.song_hinzufuegen()

    subject.detach(observer_a)

    subject.song_hinzufuegen()