class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = {}  # Store available movies
        self.booked_tickets = {}  # Store booked tickets with unique IDs
        self.ticket_id_counter = 1  # Counter for generating unique ticket IDs

    def add_movie(self):
        try:
            movie_id = int(input("Enter Movie ID: ").strip())
            if movie_id in self.movies:
                print("Movie ID already exists. Try another ID.")
                return
            name = input("Enter Movie Name: ").strip()
            showtimes = input("Enter Showtimes (comma-separated): ").split(",")
            self.movies[movie_id] = {'name': name, 'showtimes': [showtime.strip() for showtime in showtimes]}
            print(f"Movie '{name}' added successfully!")
        except ValueError:
            print("Invalid input. Movie ID should be a number.")

    def view_movies(self):
        if not self.movies:
            print("No movies available.")
            return
        print("\nAvailable Movies:")
        for movie_id, details in self.movies.items():
            print(f"ID: {movie_id}, Name: {details['name']}, Showtimes: {', '.join(details['showtimes'])}")

    def book_ticket(self):
        self.view_movies()
        try:
            movie_id = int(input("Enter Movie ID to book: ").strip())
            if movie_id not in self.movies:
                print("Invalid Movie ID.")
                return
            showtime = input(f"Enter Showtime (Available: {', '.join(self.movies[movie_id]['showtimes'])}): ").strip()
            if showtime not in self.movies[movie_id]['showtimes']:
                print("Invalid Showtime.")
                return
            customer_name = input("Enter Your Name: ").strip()
            ticket_id = self.ticket_id_counter
            self.booked_tickets[ticket_id] = {
                'movie_id': movie_id,
                'movie_name': self.movies[movie_id]['name'],
                'showtime': showtime,
                'customer_name': customer_name
            }
            self.ticket_id_counter += 1
            print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_ticket(self):
        if not self.booked_tickets:
            print("No tickets booked yet.")
            return

        try:
            choice = input("Enter Ticket ID to view (or 'all' to view all tickets): ").strip()
            if choice.lower() == 'all':
                for ticket_id, ticket in self.booked_tickets.items():
                    print(f"Ticket ID: {ticket_id}, Movie: {ticket['movie_name']}, Showtime: {ticket['showtime']}, Customer: {ticket['customer_name']}")
            else:
                ticket_id = int(choice)
                if ticket_id in self.booked_tickets:
                    ticket = self.booked_tickets[ticket_id]
                    print(f"Ticket ID: {ticket_id}, Movie: {ticket['movie_name']}, Showtime: {ticket['showtime']}, Customer: {ticket['customer_name']}")
                else:
                    print("Ticket not found.")
        except ValueError:
            print("Invalid input. Please enter a valid ticket ID.")

    def update_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID to update: ").strip())
            if ticket_id not in self.booked_tickets:
                print("Ticket not found.")
                return
            print("Options to update: 1) Showtime 2) Customer Name")
            choice = input("Enter your choice (1/2): ").strip()

            if choice == "1":
                new_showtime = input("Enter new Showtime: ").strip()
                movie_id = self.booked_tickets[ticket_id]['movie_id']
                if new_showtime not in self.movies[movie_id]['showtimes']:
                    print("Invalid new Showtime.")
                    return
                self.booked_tickets[ticket_id]['showtime'] = new_showtime
            elif choice == "2":
                new_customer_name = input("Enter new Customer Name: ").strip()
                self.booked_tickets[ticket_id]['customer_name'] = new_customer_name
            else:
                print("Invalid choice.")
                return
            print(f"Ticket {ticket_id} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid ticket ID.")

    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID to cancel: ").strip())
            if ticket_id in self.booked_tickets:
                del self.booked_tickets[ticket_id]
                print(f"Ticket {ticket_id} canceled successfully.")
            else:
                print("Ticket not found.")
        except ValueError:
            print("Invalid input. Please enter a valid ticket ID.")

    def menu(self):
        while True:
            print("\n--- Movie Ticket Booking System ---")
            print("1. Add Movie")
            print("2. View Movies")
            print("3. Book Ticket")
            print("4. View Ticket(s)")
            print("5. Update Ticket")
            print("6. Cancel Ticket")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.view_movies()
            elif choice == "3":
                self.book_ticket()
            elif choice == "4":
                self.view_ticket()
            elif choice == "5":
                self.update_ticket()
            elif choice == "6":
                self.cancel_ticket()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = MovieTicketBookingSystem()
    system.menu()
