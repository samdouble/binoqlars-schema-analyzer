import util from 'util';

function KeysObject(this: any) {
  const allKeys = {};

  this.addValue = (key, value, id = null) => {
    if (!Object.prototype.hasOwnProperty.call(allKeys, key)) {
      allKeys[key] = {
        nullIn: 0,
        null: [],
        existsIn: 0,
        values: new Set(),
        types: new Set(),
      };
    }
    if (value === null) {
      allKeys[key].nullIn += 1;
      allKeys[key].null.push(id);
    } else {
      allKeys[key].existsIn += 1;
      allKeys[key].values.add(value);
      allKeys[key].types.add(typeof value);
    }
  };

  this.toHuman = () => Object.entries(allKeys)
    .reduce((acc, [key, value]: [string, any]) => {
      const hasOnlyOneType = value.types.size === 1;
      return {
        ...acc,
        [key]: {
          ...value,
          null: value.null.length >= 10
            ? util.inspect(value.null.slice(0, 10).concat('Other ids'), { showHidden: false, depth: null })
            : util.inspect(value.null, { showHidden: false, depth: null }),
          values: value.values.size >= 10
            ? `${value.values.size} different values`
            : Array.from(value.values).sort(),
          types: hasOnlyOneType
            ? Array.from(value.types)[0]
            : Array.from(value.types).sort(),
        },
      };
    }, {});
}

export default KeysObject;
