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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* ans = new ListNode();
        ans -> next = head;
        ListNode* pre = ans;
        for (int i = 1; i < left; ++i)
            pre = pre -> next;
        head = pre -> next;
        for (int i = left; i < right; ++i) {
            ListNode* nex = head -> next;
            head -> next = nex -> next;
            nex -> next = pre -> next;
            pre -> next = nex;
        }
        return ans -> next;
    }
};