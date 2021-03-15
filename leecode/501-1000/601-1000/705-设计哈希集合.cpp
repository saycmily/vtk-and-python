class MyHashSet {
public:
    /** Initialize your data structure here. */
    vector<int> hashmap;
    MyHashSet() {
    }
    
    void add(int key) {
        for (int k : hashmap)
            if (k == key)
                return;
        hashmap.emplace_back(key);
    }
    
    void remove(int key) {
        for (int i = 0; i < hashmap.size(); ++i)
            if (hashmap[i] == key) {
                hashmap.erase(hashmap.begin() + i);
                return;
            }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        for (int k : hashmap)
            if (k == key)
                return true;
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */