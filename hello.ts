
console.log("Hello, World!");

const userInput = req.query.user;
const query = "SELECT * FROM users WHERE name = '" + userInput + "'"; // SQL Injection vulnerability
db.execute(query);

