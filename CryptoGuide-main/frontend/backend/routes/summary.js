const router = require('express').Router();
let Summary = require('../models/summaryModel');

router.route('/').get((req, res) => {
    Summary.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Error: ' + err));
  });

  module.exports = router;