from flask import Flask, render_template, request, redirect, url_for, flash
from your_code_file import BookingSystem  # Replace with the actual filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages
booking_system = BookingSystem()

@app.route('/')
def index():
    movies = booking_system.movies
    return render_template('index.html', movies=movies)

@app.route('/select_movie', methods=['POST'])
def select_movie():
    movie_index = int(request.form['movie_index'])
    movie = booking_system.movies[movie_index]
    return render_template('showtimes.html', movie=movie)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    movie_title = request.form['movie_title']
    showtime = request.form['showtime']
    tickets = int(request.form['tickets'])

    flash(f"You have successfully booked {tickets} tickets for '{movie_title}' at {showtime}.")
    return redirect(url_for('index'))

@app.route('/select_showtime', methods=['POST'])
def select_showtime():
    movie_index = int(request.form['movie_index'])
    showtime_index = int(request.form['showtime_index'])
    movie = booking_system.movies[movie_index]
    showtime = movie.showtimes[showtime_index]

    return render_template('booking.html', movie=movie, showtime=showtime)

if __name__ == "__main__":
    app.run(debug=True)
