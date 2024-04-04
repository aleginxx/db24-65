const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const { exec } = require('child_process');
const app = express();
const http = require('http');
const jwt = require("jsonwebtoken");

const router = express.Router();
router.use(bodyParser.json()); 

const port = 3000;

router.get('/signup', (req, res) => {
    const filePath = path.join(__dirname, '..', 'frontend', 'signup.html');
    res.sendFile(filePath);
});

router.post('/signup', (req,res)=> {
    const first_name           = req.body.first_name;
    const last_name            = req.body.last_name;
    const phone_number         = req.body.phone_number;
    const birth_date           = req.body.year + '-' + req.body.month + '-' + req.body.date;
    const years_of_experience  = req.body.years_of_experience;
    const position             = req.body.position;
    const username             = req.body.username;
    const password             = req.body.password + '\r';

    const query = 'INSERT INTO cook (first_name,last_name,phone_number,birth_date, years_of_experience, position, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ';
    DB.connection.query(query, [first_name,last_name,phone_number,birth_date, years_of_experience, position, username, password], (err, results) => {
        console.log(req.body);
        if (err) {
            console.error('Error querying the database:', err);
            if (err.code === 'ER_DBACCESS_DENIED_ERROR' || DB.connection.config.user !== 'root' || DB.connection.config.password !== '') {
                return res.status(401).send("Not Authorized");
            } else {
                return res.status(500).send('Internal Service Error');
            }
        }

        else {
            res.status(200).redirect('/dacontest/login');
        }
    });
});

module.exports = router;