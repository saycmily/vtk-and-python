class MyHashMap {
private:
    vector<int> keys;
    vector<int> values;
public:
    /** Initialize your data structure here. */
    MyHashMap() {
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int i = find(keys.begin(), keys.end(), key) - keys.begin();
        if (i == keys.size()) {
            keys.emplace_back(key);
            values.emplace_back(value);
        } else {
            values[i] = value;
        }
    }
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int i = find(keys.begin(), keys.end(), key) - keys.begin();
        if (i == keys.size())
            return -1;
        else
            return values[i];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int i = find(keys.begin(), keys.end(), key) - keys.begin();
        if (i != keys.size()) {
            keys[i] = -1;
            values[i] = -1;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */