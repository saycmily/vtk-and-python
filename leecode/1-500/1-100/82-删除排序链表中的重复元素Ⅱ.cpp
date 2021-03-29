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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* q = new ListNode(-101);
        q -> next = head;
        ListNode* p = q;
        while (q) {
            bool flag = false;
            ListNode* clone = q ->next;
            while(clone && clone->next && clone->val == clone->next->val) {
                clone = clone->next;
                flag = true;
            }
            if (flag)
                q->next = clone->next;
            else
                q = q -> next;
        }
        return p -> next;
    }
};