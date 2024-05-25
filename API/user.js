const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const router = express.Router();
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/user/', cookieJwtAuth, (req, res) => {
    const { username } = req.user;

    const query = 'SELECT * FROM cook WHERE username = ?'; 
    DB.connection.query(query, [username], (err, results) => { 
        if (err) {
            console.error('Error fetching user data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            return res.status(404).send('User not found');
        }
        const user = results[0]; 
        console.log("user");
        console.log(user);

        res.render(path.join(__dirname, '..', 'frontend', 'user'), { user });
    });
});

router.get('/user/edit', cookieJwtAuth, (req, res) => {
    const { username } = req.user;

    const query = 'SELECT * FROM cook WHERE username = ?'; 
    DB.connection.query(query, [username], (err, results) => { 
        if (err) {
            console.error('Error fetching user data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            return res.status(404).send('User not found');
        }
        const user = results[0]; 
        console.log("user");
        console.log(user);

        res.render(path.join(__dirname, '..', 'frontend', 'user-edit'), { user });
    });
});


router.post('/user/edit', cookieJwtAuth, (req, res) => {
    const { first_name, last_name, phone_number, birth_date, years_of_experience, position, cook_img, username, password } = req.body;

    console.log(req.body);

    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const query_id =   `SELECT cook_id FROM cook WHERE username = ?`

    const query_username = `
        UPDATE cook 
        SET first_name = ?, last_name = ?, phone_number = ?, birth_date = ?, years_of_experience = ?, position = ?, cook_img = ?, username = ?, password = ?
        WHERE cook_id = ?
    `;

    DB.connection.query(query_id, [username_check], (err, results) => { 
        if (err) {
            console.error('Error fetching user data:', err);
            return res.status(500).send('Internal Server Error');
        }
        if (results.length === 0) {
            return res.status(404).send('User not found');
        }

        const id = results[0]; 
        
        DB.connection.query(query_username, [first_name, last_name, phone_number, birth_date, years_of_experience, position, cook_img, username, password, id.cook_id], (err, results) => {
            if (err) {
                console.error('Error updating user data:', err);
                return res.status(500).send('Internal Server Error');
            }
    
            req.user.username = username;
            const token = jwt.sign(req.user, process.env.MY_SECRET);
            res.cookie('token', token, { httpOnly: true });
    
            res.redirect('/dacontest/user/');
        });
    });
});


module.exports = router;
