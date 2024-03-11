const router = require('express').Router();
let Crypto = require('../models/cryptoModel');

router.route('/').get((req, res) => {
    Crypto.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Error: ' + err));
  });

  module.exports = router;