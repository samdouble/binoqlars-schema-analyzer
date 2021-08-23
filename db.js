const mongoose = require('mongoose');

module.exports = async mongoConnectionString => {
  mongoose.connect(mongoConnectionString, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
  }, error => {
    if (error) {
      throw new Error('Could not connect to the database', error);
    }
  });
};
