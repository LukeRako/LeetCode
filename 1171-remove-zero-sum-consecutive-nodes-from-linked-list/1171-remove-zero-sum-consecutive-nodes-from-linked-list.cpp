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
    ListNode* removeZeroSumSublists(ListNode* head) {

        if (head == NULL) {
            return 0;
        }

        int prefixS = 0;
        unordered_map<int, ListNode*> freq;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        freq[0] = dummy;

        while (head != NULL) {
            prefixS += head->val;

            if (freq.find(prefixS) != freq.end()) {
                ListNode* start = freq[prefixS];
                int pSum = prefixS;

                while (start != NULL && start != head) {
                    start = start->next;
                    pSum += start->val;

                    if (start != head) {
                        freq.erase(pSum);
                    }

                freq[prefixS]->next = head->next;
                }
            } else {
                freq[prefixS] = head;
            }
            head = head->next;
        }
        return dummy->next;
    }
};