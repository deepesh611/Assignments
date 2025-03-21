const express = require("express");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

const SECRET = "your-secret-key";

// Simulated user database
const users = [
    { email: "112215055@cse.iiitp.ac.in", passwordHash: "$2b$10$A8T/2OQAb22Jdmmqai8rieOYpsSE4PRwQgLnwHO8R1JNVcz0.SGRu" } // Password: "1234"
];

// Login Route
app.post("/login", async (req, res) => {
    const { email, password } = req.body;
    const user = users.find(u => u.email === email);
    if (!user) return res.status(401).json({ error: "Invalid email" });

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) return res.status(403).json({ error: "Invalid password" });

    const token = jwt.sign({ email }, SECRET, { expiresIn: "1h" });
    res.json({ token });
});

// Protected Route
app.get("/protected", (req, res) => {
    const token = req.headers.authorization?.split(" ")[1];
    if (!token) return res.status(401).json({ error: "No token" });

    try {
        const decoded = jwt.verify(token, SECRET);
        res.json({ message: "Access granted", user: decoded });
    } catch {
        res.status(403).json({ error: "Invalid token" });
    }
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
