import mongoose from 'mongoose';

const COLLECTION_NAME = 'UFCFights';

const GenericSchema = new mongoose.Schema(
  {},
  { strict: false },
);

const Generic = mongoose.model('Generic', GenericSchema, COLLECTION_NAME);

export default Generic;
