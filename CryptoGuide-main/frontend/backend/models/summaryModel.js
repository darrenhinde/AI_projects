const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const cryptoSchema = new Schema({
    title: {type: String, required: true},
    id: {type: String, required: true},
    summary: {type: String, required: true},
}, {
    timestamps: false,
})

const Crypto = mongoose.model('Sumamry', cryptoSchema, 'summary');


module.exports = Crypto;