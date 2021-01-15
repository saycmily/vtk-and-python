class TrieNode {
    boolean end = false;
    TrieNode[] nexts = new TrieNode[26];
}
class Trie {
    // define
    TrieNode root = new TrieNode();

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode cur = root;
        int len = word.length();
        int ch = 0;
        for (int i = 0; i < len; ++i) {
            ch = word.charAt(i) - 'a';
            if (cur.nexts[ch] == null)
                cur.nexts[ch] = new TrieNode();
            cur = cur.nexts[ch];
        }
        cur.end = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode cur = root;
        int len = word.length();
        int ch = 0;
        for (int i = 0; i < len; ++i) {
            ch = word.charAt(i) - 'a';
            if (cur.nexts[ch] == null)
                return false;
            cur = cur.nexts[ch];
        }
        return cur.end;
    }
    
    /** delete a word from the trie */
    public boolean delete(String word) {
        // this word in the trie
        if (search(word) == false)
            return false;
        TrieNode cur = root;
        int len = word.length();
        int ch = 0;
        for (int i = 0; i < len; ++i) {
            ch = word.charAt(i) - 'a';
            if (cur.nexts[ch] == null)
                return false;
            cur = cur.nexts[ch];
        }
        cur.end = false;
        return true;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        int len = prefix.length();
        int ch = 0;
        for (int i = 0; i < len; ++i) {
            ch = prefix.charAt(i) - 'a';
            if (cur.nexts[ch] == null)
                return false;
            cur = cur.nexts[ch];
        }
        return true;
    }
    public static void main(String[] args) {
        Trie a = new Trie();
        a.insert("apple");
        boolean b = a.search("apple");
        boolean c = a.startsWith("app");
        boolean d1 = a.delete("app");
        boolean d = a.delete("apple");
        boolean e = a.startsWith("app");
        System.out.println(b);
        System.out.println(c);
        System.out.println(d1);
        System.out.println(d);
        System.out.println(e);
    }
}
