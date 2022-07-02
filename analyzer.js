require('dotenv').config({ path: './.env' });
const { Command } = require('commander');
const flat = require('flat');
const mongoConnect = require('./db');
const GenericSchema = require('./GenericSchema');
const KeysObject = require('./KeysObject');

const program = new Command();
program.version('0.0.1');
program
  .option('-d, --debug', 'output extra debugging')
  .option('-s, --small', 'small pizza size')
  .option('-p, --pizza-type <type>', 'flavour of pizza');

program.parse(process.argv);

const options = program.opts();
if (options.debug) console.log(options);
if (options.small) console.log('- small pizza size');
if (options.pizzaType) console.log(`- ${options.pizzaType}`);

(async () => {
  await mongoConnect(process.env.MONGO_URL);

  const allKeys = new KeysObject();

  const fights = await GenericSchema.find({ date: { $gt: '2000-01-01', $lt: '2022-07-01' }}).lean().exec();

  const nbDocuments = fights.length;
  for (const fight of fights) {
    const flatFight = flat(fight);
    Object.entries(flatFight)
      .forEach(([key, value]) => {
        allKeys.addValue(key, value, fight.id);
      });
  }

  console.log(nbDocuments, Object.entries(allKeys.toString()).filter(([key, value]) => {
    return value.nullIn !== 0;
  }));
})();
