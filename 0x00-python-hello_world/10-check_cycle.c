#include "lists.h"
/**
 * check_cycle - checks for cycle in singly linked lists
 * @list: linked list to check
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *slow;
listint_t *fast;

if (!list)
return (0);

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
