class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        seat_arrangement = [['0' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = seat_arrangement
        self._show_list.append((show_id, movie_name, time))

    def book_seats(self, show_id, num_tickets):
        if show_id not in self._seats:
            print("Invalid show ID")
            return []

        seat_map = self._seats[show_id]
        booked_seats = []

        for _ in range(num_tickets):
            valid_seat = False
            while not valid_seat:
                row = input(f"Enter seat row: ")
                col = input(f"Enter seat column: ")

                if row.isdigit() and col.isdigit():
                    row = int(row)
                    col = int(col)
                    if 0 <= row < self._rows and 0 <= col < self._cols:
                        if seat_map[row][col] != '1':
                            seat_map[row][col] = '1'
                            booked_seats.append((row, col))
                            valid_seat = True
                        else:
                            print("Seat already booked. Please choose another seat.")
                    else:
                        print("Invalid seat selection. Please try again.")
                else:
                    print("Invalid input. Please enter integers for row and column.")

        return booked_seats

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("Invalid show ID")
            return

        seat_map = self._seats[show_id]
        print(f"Available seats for Show ID {show_id} in Hall {self._hall_no} (Row, Col):")
        for row in range(self._rows):
            for col in range(self._cols):
                print(seat_map[row][col], end=',')
            print()


def format_booked_seats(seats):
    if not seats:
        return ""

    seat_strings = [f"({seat[0]},{seat[1]})" for seat in seats]
    if len(seat_strings) == 1:
        return seat_strings[0]
    else:
        return ', '.join(seat_strings[:-1]) + ' and ' + seat_strings[-1]


def main():
    
    hall1 = Hall(rows=7, cols=7, hall_no=1)
    hall2 = Hall(rows=6, cols=8, hall_no=2)

    hall1.entry_show("111", "Avengers", "15:00")
    hall1.entry_show("222", "Jumanji", "18:30")
    hall2.entry_show("333", "Inception", "20:00")

    while True:
        print("\nOptions:")
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            for hall in Star_Cinema.hall_list:
                print(f"\nHall {hall._hall_no} Shows:")
                for show in hall.view_show_list():
                    print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

        elif choice == "2":
            show_id = input("Enter show ID to view available seats: ")
            for hall in Star_Cinema.hall_list:
                if show_id in hall._seats:
                    hall.view_available_seats(show_id)
                    break
            else:
                print("Invalid show ID")

        elif choice == "3":
            show_id = input("Enter show ID to book ticket: ")
            num_tickets_input = input("Enter number of tickets to book: ")

            if num_tickets_input.isdigit():
                num_tickets = int(num_tickets_input)
                for hall in Star_Cinema.hall_list:
                    if show_id in hall._seats:
                        booked_seats = hall.book_seats(show_id, num_tickets)
                        if booked_seats:
                            print("Booking Successful!")
                            print(f"Seats {format_booked_seats(booked_seats)} booked for show {show_id}")
                        break
                else:
                    print("Invalid show ID")
            else:
                print("Invalid input. Please enter a valid number of tickets.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
