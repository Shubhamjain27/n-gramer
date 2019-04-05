const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  var PythonShell = require('python-shell');
  var pyshell = new PythonShell('/compute.py', {
    scriptPath: __dirname,
    pythonPath: 'python2'
  });
  pyshell.send(JSON.stringify(req.query));

  result = "";

  pyshell.on('message', function (message) {
    result += message;
  });

  pyshell.end(function (err) {
    if (err) {
      throw err;
    } else {
      console.log(result);
      name = result.split('/');
      res.json({
        'fileName': name[name.length - 1]
      });
    }

  });
});

module.exports = router;
