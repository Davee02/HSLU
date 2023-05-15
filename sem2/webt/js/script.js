const app = new Vue({
  el: "#app",
  data: {
    book: {
      title: "",
      author: "",
      genre: "",
      publicationYear: getCurrentYear(),
    },
    errors: {
      title: "",
      author: "",
      genre: "",
      publicationYear: "",
    },
    allGenres: [],
    topBooks: [],
    location_info: {
      zip: "",
      place_name: "",
      state: "",
      longitude: "",
      latitude: "",
    }
  },
  methods: {
    validateForm() {
      let isValid = true;

      if (
        !this.book.title ||
        this.book.title.length < 5 ||
        this.book.title.length > 30
      ) {
        this.errors.title =
          "Der Titel muss zwischen 5 und 30 Zeichen lang sein.";
        isValid = false;
      } else {
        this.errors.title = "";
      }

      if (!this.book.author) {
        this.errors.author = "Bitte geben Sie einen Autor ein.";
        isValid = false;
      } else {
        this.errors.author = "";
      }

      if (!this.book.genre) {
        this.errors.genre = "Bitte geben Sie ein Genre ein.";
        isValid = false;
      } else {
        this.errors.genre = "";
      }

      if (
        !this.book.publicationYear ||
        this.book.publicationYear < 1450 ||
        this.book.publicationYear > getCurrentYear()
      ) {
        this.errors.publicationYear =
          "Bitte geben Sie ein gültiges Erscheinungsjahr ein.";
        isValid = false;
      } else {
        this.errors.publicationYear = "";
      }

      return isValid;
    },
    submitForm() {
      if (this.validateForm()) {
        const formData = new FormData();
        formData.append("title", this.book.title);
        formData.append("author", this.book.author);
        formData.append("genre", this.book.genre);
        formData.append("publicationYear", this.book.publicationYear);

        fetch("process.php", {
          method: "POST",
          body: formData,
        })
          .then((response) => response.text())
          .then((data) => {
            document.body.innerHTML = data;
          });
      }
    },
  },
});

function getCurrentYear() {
  return new Date().getFullYear();
}

function loadBookData() {
  fetch("var/book_data.json")
    .then((response) => response.json())
    .then((data) => {
      app.topBooks = data.topBooks;
      app.allGenres = data.genres;
    });
}

function loadLocationData() {
  fetch("https://api.zippopotam.us/ch/6343")
    .then((response) => response.json())
    .then((data) => {
      app.location_info.zip = data["post code"];
      app.location_info.place_name = data.places[2]["place name"];
      app.location_info.state = data.places[2]["state abbreviation"];
      app.location_info.longitude = data.places[2].longitude;
      app.location_info.latitude = data.places[2].latitude;
    });
}

function drawCanvas() {
  const canvas = document.getElementById("countdown");
  const ctx = canvas.getContext("2d");

  function drawBlock(x, y, text) {
    const width = 40;
    const height = 45;

    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + width, y);
    ctx.lineTo(x + width + height * 0.2, y + height * 0.2);
    ctx.lineTo(x + height * 0.2, y + height * 0.2);
    ctx.closePath();
    ctx.fillStyle = "darkred";
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(x + height * 0.2, y + height * 0.2);
    ctx.lineTo(x + width + height * 0.2, y + height * 0.2);
    ctx.lineTo(x + width + height * 0.2, y + height + height * 0.2);
    ctx.lineTo(x + height * 0.2, y + height + height * 0.2);
    ctx.closePath();
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(x + height * 0.2, y + height * 0.2);
    ctx.lineTo(x, y + height);
    ctx.lineTo(x + width, y + height);
    ctx.lineTo(x + width + height * 0.2, y + height * 0.2);
    ctx.closePath();
    ctx.fillStyle = "white";
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "black";
    ctx.font = "20px Arial";
    ctx.fillText(text, x + width * 0.3, y + height * 0.7);
  }

  function getTimeUntil(date) {
    const now = new Date();
    const diff = date - now;

    const days = Math.floor(diff / 1000 / 60 / 60 / 24);
    const hours = Math.floor((diff / 1000 / 60 / 60) % 24);
    const minutes = Math.floor((diff / 1000 / 60) % 60);
    const seconds = Math.floor((diff / 1000) % 60);

    return { days, hours, minutes, seconds };
  }

  // first day of next month
  const nextDate = new Date();
  nextDate.setDate(1);
  nextDate.setHours(17, 0, 0, 0);
  nextDate.setMonth(nextDate.getMonth() + 1);

  setInterval(() => {
    const countdown = getTimeUntil(nextDate);
    drawBlock(50, 0, countdown.days);
    drawBlock(110, 0, countdown.hours);
    drawBlock(170, 0, countdown.minutes);
    drawBlock(230, 0, countdown.seconds);
  }, 1000);
}

// execute when dom is loaded
document.addEventListener("DOMContentLoaded", () => {
  loadLocationData();
  loadBookData();
  drawCanvas();
});
