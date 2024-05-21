const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const DB = require('./database.js');
const http = require('http');
const phpExpress = require('php-express')();
const { exec } = require('child_process');
const cookieParser = require("cookie-parser");
const { cookieJwtAuth } = require("./middelware/cookieJwtAuth.js");


const port = 9876;
const app = express();

const base_url = '/dacontest';

app.use(cookieParser());

const healthcheck = require('./healthcheck.js');
app.use(base_url, healthcheck);

const backup = require('./admin functionalities/backup.js');
app.use(base_url, backup);

const restore = require('./admin functionalities/restore.js');
app.use(base_url, restore)

const login = require('./login.js');
app.use(base_url, login);

const signup = require('./signup.js');
app.use(base_url, signup);

const logout = require('./logout.js');
app.use(base_url, logout);

app.set('view engine', 'ejs');

const user = require('./user.js');
app.use(base_url, user);

const admin = require('./admin functionalities/admin.js');
app.use(base_url, admin);

const delition = require('./admin functionalities/delete.js');
app.use(base_url, delition);

const home = require('./home.js');
app.use(base_url, home);

const make_admin = require('./admin functionalities/make_admin.js');
app.use(base_url, make_admin);

const modify = require('./admin functionalities/modify.js');
app.use(base_url, modify);

// Queries
const score = require('./queries/score.js');
app.use(base_url, score);

const cooks_details = require('./queries/cooks_details.js');
app.use(base_url, cooks_details);

const most_recipes = require('./queries/most_recipes.js');
app.use(base_url, most_recipes);

const round_cooks = require('./queries/round_cooks.js');
app.use(base_url, round_cooks);

const round_recipes = require('./queries/round_recipes.js');
app.use(base_url, round_recipes);

const round_equipment = require('./queries/round_equipment.js');
app.use(base_url, round_equipment);

const round_cuisines = require('./queries/round_cuisines.js');
app.use(base_url, round_cuisines);

const round_ratings = require('./queries/round_ratings.js');
app.use(base_url, round_ratings);

// View Data 
const profile = require('./view_data/profile.js');
app.use(base_url, profile);

const view_recipes = require('./view_data/view_recipes.js');
app.use(base_url, view_recipes);

http.createServer(app).listen(port, () => {
    console.log(`HTTP server running on port ${port}`);
});