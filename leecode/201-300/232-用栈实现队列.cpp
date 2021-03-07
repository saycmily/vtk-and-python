class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> ru;
    stack<int> chu;
    MyQueue() {
    }
    /** Push element x to the back of queue. */
    void push(int x) {
        ru.push(x);
    }
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int x;
        if (chu.empty()) {
            while (!ru.empty()) {
                int x = ru.top(); ru.pop();
                chu.push(x);
            }
        }
        x = chu.top(); chu.pop();
        return x;
    }
    
    /** Get the front element. */
    int peek() {
        if (chu.empty()) {
            while (!ru.empty()) {
                int x = ru.top(); ru.pop();
                chu.push(x);
            }
        }
        return chu.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if (ru.empty() && chu.empty())    
            return true;
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */