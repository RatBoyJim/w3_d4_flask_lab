class Event:
    def __init__(self, date, name, num_guests, room_location, description, is_weekly):
        self.date = date
        self.name = name
        self.num_guests = num_guests
        self.room_location = room_location
        self.description = description
        self.is_weekly = is_weekly

#         * Date
        # * Name of Event
        # * Number of guests
        # * Room Location
        # * Description