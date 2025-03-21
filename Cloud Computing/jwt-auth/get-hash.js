const bcrypt = require('bcrypt');

const password = "1234";
bcrypt.hash(password, 10, (err, hash) => {
    console.log("New Hash:", hash);
});
