class TrainCarriage:
    def __init__(self, carriage_id, total_seats):
        
        self.carriage_id = carriage_id
        self.total_seats = total_seats
        self.reserved_seats = []

    def reserve_seat(self, seat_number):
        
        if seat_number not in range(1, self.total_seats + 1):
            return "Invalid seat number."
        if seat_number in self.reserved_seats:
            return f"Seat {seat_number} is already reserved."
        
        self.reserved_seats.append(seat_number)
        return f"Seat {seat_number} reserved."

    def cancel_reservation(self, seat_number):
        
        if seat_number not in self.reserved_seats:
            return f"Seat {seat_number} is not reserved."
        
        self.reserved_seats.remove(seat_number)
        return f"Seat {seat_number} reservation canceled."

    def reset_reservations(self):
        
        self.reserved_seats.clear()
        return "All reservations cleared."

    def is_full(self):
        
        return len(self.reserved_seats) == self.total_seats

    def get_reservation_report(self):
        
        reserved = sorted(self.reserved_seats)
        available = [seat for seat in range(1, self.total_seats + 1) if seat not in self.reserved_seats]

        return f"Reserved seats: {reserved}\nAvailable seats: {available}"


carriage = TrainCarriage("A1", 5)


for seat in [1, 3, 4]:
    print(carriage.reserve_seat(seat))


print(carriage.cancel_reservation(3))


print(carriage.get_reservation_report())


print("Is the carriage full?", carriage.is_full())


print(carriage.reset_reservations())


print(carriage.get_reservation_report())
