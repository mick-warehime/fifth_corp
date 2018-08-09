import events


class Listener(object):

    def notify(self, event: events.Event) -> None:
        raise NotImplementedError("Subclasses must implement notify()")
