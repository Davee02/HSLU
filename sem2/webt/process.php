<?php
// Establish connection to MySQL database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "books";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Save request contents into variables
$title = $_POST["title"] ?? "";
$author = $_POST["author"] ?? "";
$genre = $_POST["genre"] ?? "";
$publicationYear = $_POST["publicationYear"] ?? "";

// Ensure that title is between 5 and 30 characters, author is not empty, genre is not empty, and publicationYear is not empty
if (strlen($title) < 5 || strlen($title) > 30) {
  die("Error: Title must be between 5 and 30 characters");
}
if (empty($author)) {
  die("Error: Author cannot be empty");
}
if (empty($genre)) {
  die("Error: Genre cannot be empty");
}
// Ensure that publicationYear is between 1450 and current year
$currentYear = date("Y");
if (empty($publicationYear) || intval($publicationYear) < 1450 || intval($publicationYear) > $currentYear) {
  die("Error: Publication year must be between 1450 and " . $currentYear);
}

// Escape special characters in variables to prevent SQL injection attacks
$title = mysqli_real_escape_string($conn, $title);
$author = mysqli_real_escape_string($conn, $author);
$genre = mysqli_real_escape_string($conn, $genre);
$publicationYear = mysqli_real_escape_string($conn, $publicationYear);

// Save variables to MySQL database table
$sql = "INSERT INTO recommendations (title, author, genre, publicationYear) VALUES ('$title', '$author', '$genre', '$publicationYear')";

if ($conn->query($sql) !== TRUE) {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// Save recommendation count in cookie
if(isset($_COOKIE["recommendation_count"])){
    $count = $_COOKIE["recommendation_count"] + 1;
} else {
    $count = 1;
}
setcookie("recommendation_count", $count, time() + (10 * 365 * 24 * 60 * 60), "/");

// Display thank you message with request contents
echo "<!DOCTYPE html>
<html lang=\"de\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Deine Buchempfehlung</title>
    <link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">
</head>
<body>
    <header class=\"w3-container w3-teal\">
        <h1>Buchempfehlung</h1>
    </header>
    <section class=\"w3-container\">
        <h2>Danke für deine $count. Empfehlung!</h2>
        <p>Wir haben sie in unserer Datenbank gespeichert. Komme an unsere nächste Buchbesprechung, vielleicht wurde dein Buch als Buch des Monats auserkohren.</p>
        <p><strong>Titel:</strong> $title</p>
        <p><strong>Autor:</strong> $author</p>
        <p><strong>Genre:</strong> $genre</p>
        <p><strong>Erscheinungsjahr:</strong> $publicationYear</p>
        <a href=\"index.html\" class=\"w3-button w3-teal\">Zurück</a>
    </section>
</body>
</html>";

// Close connection to MySQL database server
$conn->close();
?>