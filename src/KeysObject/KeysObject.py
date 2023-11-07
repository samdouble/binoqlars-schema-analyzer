class KeysObject:
    all_keys = dict()

    def add_value(self, key, value, id = None):
        if (key not in self.all_keys):
            self.all_keys[key] = {
                null_in: 0,
                null: [],
                exists_in: 0,
                values: set(),
                types: set(),
            }
        if (value == None):
            self.all_keys[key].null_in += 1
            self.all_keys[key].null.append(id)
        else:
            self.all_keys[key].exists_in += 1
            self.all_keys[key].values.add(value)
            self.all_keys[key].types.add(type(value))

    def toHuman(self):
        all_keys_human = dict()
        for key in self.all_keys:
            value = self.all_keys[key]
            has_only_one_type = len(value.types.size) == 1
            all_keys_human[key] = {
                #...value,
                #null: value.null.length >= 10
                #    ? util.inspect(value.null.slice(0, 10).concat('Other ids'), { showHidden: false, depth: null })
                #    : util.inspect(value.null, { showHidden: false, depth: null }),
                #values: value.values.size >= 10
                #    ? `${value.values.size} different values`
                #    : Array.from(value.values).sort(),
                #types: has_only_one_type
                #    ? Array.from(value.types)[0]
                #    : Array.from(value.types).sort(),
            }
        return all_keys_human
