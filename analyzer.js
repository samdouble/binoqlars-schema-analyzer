require('dotenv').config({ path: './.env' });
const { Command } = require('commander');
const flat = require('flat');
const mongoConnect = require('./db');
const GenericSchema = require('./GenericSchema');

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

  const allKeys = {};

  const fights = await GenericSchema.find().lean().exec();

  const nbDocuments = fights.length;
  for (const fight of fights) {
    const flatFight = flat(fight);
    Object.entries(flatFight)
      .forEach(([key, value]) => {
        if (!allKeys.hasOwnProperty(key)) {
          allKeys[key] = {
            usedIn: 0,
            values: new Set(),
          };
        }
        allKeys[key].usedIn++;
        allKeys[key].values.add(value);
      });
  }

  console.log(nbDocuments, allKeys);
})();
