const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const DB = require('../database.js');
const router = express.Router();
const { cookieJwtAuth } = require("../middelware/cookieJwtAuth.js");
const jwt = require("jsonwebtoken");

router.use(bodyParser.json());
const filePath = path.join(__dirname, '..', '..', 'frontend', 'admin_functions.html');

router.get('/admin_functions', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    res.sendFile(filePath);
});

router.get('/edit-data', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    res.sendFile(filePath);
});

router.post('/edit-data', cookieJwtAuth, (req, res) => {
    const token = req.cookies.token;
    const table = req.body.table;
    const attributes = req.body;
    const service = req.body.service;
    delete attributes.service;
    delete attributes.table;

    if (!table || !service || !attributes) {
        return res.status(400).json({ error: "Missing required parameters" });
    }

    if (service === 'add') {
        let query = `INSERT INTO ${addTable} (${Object.keys(attributes).join(', ')}) VALUES (${Object.values(attributes).map((value, index, array) => {
            return index === array.length - 1 ? `'${value}\\r'` : `'${value}'`;
        }).join(', ')})`;

        DB.connection.query(query, (err, result) => {
            if (err) {
                console.error("Error executing SQL query:", err);
                return res.status(500).json({ error: "Error inserting data into the database" });
            }
            
            console.log("Data inserted successfully into", addTable);
            return res.status(200).redirect('/dacontest/edit-data');
        });
    } else if (service === 'modify') {
        DB.connection.query(`SHOW INDEX FROM ${table} WHERE Non_unique = 0`, (err, result) => {
            if (err) {
                console.error("Error retrieving unique columns:", err);
                return res.status(500).json({ error: "Error retrieving unique columns" });
            }
            if (result.length === 0) {
                return res.status(500).json({ error: "Unique columns not found" });
            }
            const uniqueColumns = result.map(row => row.Column_name);

            // Check which attributes already exist in the table
            let existingAttributesQuery = `SELECT * FROM ${table} WHERE `;
            let whereConditions = [];
            for (let column of uniqueColumns) {
                if (attributes[column]) {
                    whereConditions.push(`${column} = '${attributes[column]}'`);
                }
            }
            existingAttributesQuery += whereConditions.join(' AND ');
            
            DB.connection.query(existingAttributesQuery, (err, result) => {
                if (err) {
                    console.error("Error executing SQL query:", err);
                    return res.status(500).json({ error: "Error retrieving existing data from the database" });
                }

                if (result.length === 0) {
                    return res.status(404).json({ error: "Record not found" });
                }

                const existingAttributes = result[0];

                // Construct the SQL UPDATE query dynamically
                let updateQuery = `UPDATE \`${table}\` SET `;
                let updates = [];
                for (let attribute in attributes) {
                    if (attributes.hasOwnProperty(attribute) && attributes[attribute] !== '' && attributes[attribute] !== existingAttributes[attribute]) {
                        updates.push(`${attribute} = '${attributes[attribute]}'`);
                    }
                }
                if (updates.length === 0) {
                    return res.status(200).json({ message: "No changes detected" });
                }
                updateQuery += updates.join(', ');
                updateQuery += ` WHERE `;
                let whereConditionsUpdate = [];
                for (let column of uniqueColumns) {
                    whereConditionsUpdate.push(`${column} = '${existingAttributes[column]}'`);
                }
                updateQuery += whereConditionsUpdate.join(' AND ');

                // Execute the SQL UPDATE query
                DB.connection.query(updateQuery, (err, result) => {
                    if (err) {
                        console.error("Error executing SQL query:", err);
                        return res.status(500).json({ error: "Error updating data in the database" });
                    }
                    console.log("Data updated successfully in", table);
                    return res.status(200).redirect('/dacontest/edit-data');
                });
            });
        });
    } else if (service === 'delete') {
        const nonEmptyAttributes = {};
        for (const [key, value] of Object.entries(attributes)) {
            if (value !== '') {
                nonEmptyAttributes[key] = value;
            }
        }

        const condition = Object.entries(nonEmptyAttributes)
            .map(([key, value]) => `${key} = '${value}'`)
            .join(' AND ');

        deleteQuery = `DELETE FROM ${table} WHERE ${condition}`;

        console.log(deleteQuery);

        DB.connection.query(deleteQuery, (err, result) => {
            if (err) {
                console.error("Error executing SQL query:", err);
                return res.status(500).json({ error: "Error updating data in the database" });
            }
            console.log("Data deleted successfully from", table);
            return res.status(200).redirect('/dacontest/edit-data');
        });

    } else {
        return res.status(400).json({ error: "Invalid service type" });
    }
});

module.exports = router;
