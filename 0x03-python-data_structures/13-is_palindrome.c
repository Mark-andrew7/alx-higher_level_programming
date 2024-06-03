#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *next = NULL;

while (head != NULL)
{
next = head->next;
head->next = prev;
prev = head;
head = next;
}
return (prev);
}

/**
 * find_middle - Finds the middle of a linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the middle node.
 */
listint_t *find_middle(listint_t *head)
{
listint_t *slow = head;
listint_t *fast = head;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}
return (slow);
}

/**
 * compare_lists - Compares two linked lists.
 * @head1: Pointer to the head of the first list.
 * @head2: Pointer to the head of the second list.
 *
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 != NULL && head2 != NULL)
{
if (head1->n != head2->n)
return (0);
head1 = head1->next;
head2 = head2->next;
}
return (head1 == NULL && head2 == NULL);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
listint_t *middle, *second_half, *reversed_second_half;
int result;

if (head == NULL || *head == NULL)
return (1);

middle = find_middle(*head);
reversed_second_half = reverse_list(middle);
result = compare_lists(*head, reversed_second_half);    
return (result);
}
