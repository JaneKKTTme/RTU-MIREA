class EventBus():
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, method):
        if event_type not in self.subscribers.keys():
            self.subscribers[event_type] = [method]
        else:
            self.subscribers[event_type].append(method)

    def raise_event(self, event_type, *data):
        if event_type in self.subscribers.keys():
            for method in self.subscribers[event_type]:
                method(*data)

    def unsubscribe(self, event_type, method):
        if event_type in self.subscribers.keys():
            self.subscribers[event_type].remove(method)
            if len(self.subscribers[event_type]) == 0:
                del self.subscribers[event_type]

if __name__ == '__main__':
    events = EventBus()
    callback1 = lambda x: print("Event №1: " + x)
    callback2 = lambda x: print("Event №2: " + x)
    events.subscribe("1", callback1)
    events.subscribe("2", callback1)
    events.subscribe("1", callback2)
    events.subscribe("2", callback2)
    events.subscribe("2", callback1)
    events.raise_event("1", "Buy it!")
    events.raise_event("2", "Kill him!")
    events.unsubscribe("1", callback1)
