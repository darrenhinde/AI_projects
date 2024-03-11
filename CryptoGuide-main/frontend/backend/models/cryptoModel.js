const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const cryptoSchema = new Schema({
    crypto: {type: String, required: true},
    views: {type: Number, required: true},
    score: {type: Number, required: true},
}, {
    timestamps: false,
})

const Crypto = mongoose.model('Crypto', cryptoSchema, 'crypto_stats');


module.exports = Crypto;