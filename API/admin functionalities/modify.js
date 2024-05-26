const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

const router = express.Router();
router.use(bodyParser.json());

router.get('/modify', (req, res) => {
    const token = req.cookies.token;
    const decodedToken = jwt.decode(token);
    const username_check = decodedToken.username;

    const check_admin = `SELECT * FROM administrator WHERE admin_username = ?`;

    DB.connection.query(check_admin, [username_check], (err, results) => { 
      if (err) {
          console.error('Error fetching admin data:', err);
          return res.status(500).send('Internal Server Error');
      }
      if (results.length === 0) {
          return res.status(404).send('You do not have permission to access this page');
      }
      else {
        const filePath = path.join(__dirname, '..', '..', 'frontend', 'modify.html');
    res.sendFile(filePath);
      }
    });
});

router.post('/modify', (req, res) => {
    const tableName = req.body.table; 
    const query = `SELECT * FROM ${tableName}`;
    
    DB.connection.query(query, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).send('Error retrieving table data.');
        } else {
            const columns = Object.keys(result[0]);
            const primaryKey = columns[0]; 
            
            res.json({ columns: columns, primaryKey: primaryKey, data: result });
        }
    });
});

router.post('/update', (req, res) => {
    const tableName = req.body.tableName;
    const rowID = req.body.rowID; 
    const data = req.body.data;
    const primaryKey = req.body.primaryKey; 

    let query = `UPDATE ${tableName} SET `;
    let values = [];
    for (let key in data) {
        query += `${key} = ?, `;
        values.push(data[key]);
    }
    query = query.slice(0, -2); 
    query += ` WHERE ${primaryKey} = ?`; 
    values.push(rowID); 

    DB.connection.query(query, values, (err, result) => {
        if (err) {
            console.error('Error updating row:', err);
            res.status(500).send('Error updating row in the database.');
        } else {
            console.log('Row updated successfully.');
            res.status(200).send('Row updated successfully.');
        }
    });
});

module.exports = router;

