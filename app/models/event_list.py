from app.models.event import Event

event1 = Event("29/08/1988", "Jinja Bob", 9, "Edinburgh", "Really cool room", False)
event2 = Event("20/03/2020", "Michael's Birfday", 4, "Glasgow", "Could try harder room", True)
event3 = Event("09/08/1928", "Orange Phil", 2, "Dundee", "Less cool room", False)
event4 = Event("29/08/1988", "Billy no mates", 1, "London", "Not a cool room", False)

event_list = [event1, event2, event3, event4]

def add_new_event(new_event):
    event_list.append(new_event)