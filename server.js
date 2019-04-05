const express = require('express');
const http = require('http');
const app = express();
const path = require('path');

const Result = require('./server/Routes/result.js');

app.use(express.static(path.join(__dirname, 'dist')));
app.use('/output', express.static(path.join(__dirname, 'output')));

app.use(function (req, res, next) {

  // Website you wish to allow to connect
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4200');

  // Request methods you wish to allow
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

  // Request headers you wish to allow
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

  // Set to true if you need the website to include cookies in the requests sent
  // to the API (e.g. in case you use sessions)
  res.setHeader('Access-Control-Allow-Credentials', true);

  // Pass to next layer of middleware
  next();
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist/index.html'));
});

app.use('/result', Result);

const port = process.env.PORT || '3000';
app.set('port', port);
const server = http.createServer(app);
server.listen(port);
