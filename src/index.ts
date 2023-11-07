import flat from 'flat';
import mongoConnect from './db';
import GenericSchema from './GenericSchema';
import KeysObject from './KeysObject';

(async () => {
  await mongoConnect(process.env.MONGO_URL);

  const allKeys = new KeysObject();

  const fights = await GenericSchema
    .find({ date: { $gt: '2000-01-01', $lt: '2022-07-01' } })
    .lean()
    .exec();

  const nbDocuments = fights.length;
  for (const fight of fights) {
    const flatFight = flat(fight);
    Object.entries(flatFight)
      .forEach(([key, value]) => {
        allKeys.addValue(key, value, fight.id);
      });
  }

  console.log(
    nbDocuments,
    allKeys.toHuman(),
    // Object.entries(allKeys.toHuman())
    //   .filter(([, value]: any[]) => value.nullIn !== 0),
  );

  process.exit(0);
})();
