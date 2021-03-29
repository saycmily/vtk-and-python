/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head -> next == nullptr) return head;
        int cur = 0, size = 0;
        ListNode* p = head;
        while (p) {
            size ++;
            p = p -> next;
        }
        k = k % size;
        if (k == 0) return head;
        k = size - k;
        int j = k;
        p = head;
        while (k--)
            head = head -> next;
        ListNode* q = head;
        while (q -> next)
            q = q -> next;
        q -> next = p;
        while(j --)
            q = q -> next;
        q -> next = nullptr;
        return head;
    }
};