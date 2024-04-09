const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

const router = express.Router();
router.use(bodyParser.json());

const port = 3000;

router.get('/modify',(req,res)=>{
    const filePath = path.join(__dirname, '..', '..' ,'frontend', 'modify.html');
    res.sendFile(filePath);
});

router.post('/modify', (req, res) => {
    const tableName = req.body.table; // Extracting the table name from the request body
    const query = `SELECT * FROM ${tableName}`; // Constructing the SQL query
    
    // Execute the query and handle the response
    DB.connection.query(query, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).send('Error retrieving table data.');
        } else {
            const columns = Object.keys(result[0]);
            const primaryKey = columns[0]; // Assuming the first column is the primary key
            
            // Send both column names, including primary key, to the client
            res.json({ columns: columns, primaryKey: primaryKey, data: result });
        }
    });
});

router.post('/update', (req, res) => {
    const tableName = req.body.tableName;
    const rowID = req.body.rowID; // Extract the row ID from the request body
    const data = req.body.data;
    const primaryKey = req.body.primaryKey; // Extract the primary key from the request body

    // Construct SQL query to update the specified row in the table
    let query = `UPDATE ${tableName} SET `;
    let values = [];
    for (let key in data) {
        query += `${key} = ?, `;
        values.push(data[key]);
    }
    query = query.slice(0, -2); // Remove the trailing comma and space
    query += ` WHERE ${primaryKey} = ?`; // Use the primary key column dynamically
    values.push(rowID); // Use the rowID parameter as the value for the WHERE clause

    // Execute the update query
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

