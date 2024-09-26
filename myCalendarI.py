class MyCalendar:

    def __init__(self):
        self.bookings = []        

    def book(self, start: int, end: int) -> bool:
        for booking in self.bookings:
            booking_start, booking_end = booking
            if booking_start <= start < booking_end or booking_start < end < booking_end:
                return False
            if booking_start <= start < end <= booking_end:
                return False
            if start <= booking_start < booking_end <= end:
                return False
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
