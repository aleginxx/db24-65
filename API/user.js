const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('./database.js');
const router = express.Router();

router.use(bodyParser.urlencoded({ extended: true }));

router.get('/user/:username', (req, res) => {
    const username = req.params.username; 
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

        res.render(path.join(__dirname, '..', 'frontend', 'user'), { user });
    });
});

module.exports = router;
