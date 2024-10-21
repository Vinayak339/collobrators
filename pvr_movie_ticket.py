class Movie:
    def __init__(self, title, showtimes):
        self.title = title
        self.showtimes = showtimes

class BookingSystem:
    def __init__(self):
        self.movies = []
        self.populate_movies()

    def populate_movies(self):
        self.movies.append(Movie("Movie A", ["10:00 AM", "1:00 PM", "4:00 PM"]))
        self.movies.append(Movie("Movie B", ["11:00 AM", "2:00 PM", "5:00 PM"]))
        self.movies.append(Movie("Movie C", ["12:00 PM", "3:00 PM", "6:00 PM"]))

    def display_movies(self):
        print("Available Movies:")
        for index, movie in enumerate(self.movies):
            print(f"{index + 1}. {movie.title}")

    def select_movie(self):
        self.display_movies()
        choice = int(input("Select a movie (1-3): ")) - 1
        if 0 <= choice < len(self.movies):
            return self.movies[choice]
        else:
            print("Invalid selection, please try again.")
            return self.select_movie()

    def select_showtime(self, movie):
        print(f"\nShowtimes for {movie.title}:")
        for index, time in enumerate(movie.showtimes):
            print(f"{index + 1}. {time}")
        choice = int(input("Select a showtime: ")) - 1
        if 0 <= choice < len(movie.showtimes):
            return movie.showtimes[choice]
        else:
            print("Invalid selection, please try again.")
            return self.select_showtime(movie)

    def book_ticket(self):
        movie = self.select_movie()
        showtime = self.select_showtime(movie)
        tickets = int(input("Enter number of tickets to book: "))
        print(f"\nYou have successfully booked {tickets} tickets for '{movie.title}' at {showtime}.")

if __name__ == "__main__":
    system = BookingSystem()
    system.book_ticket()
