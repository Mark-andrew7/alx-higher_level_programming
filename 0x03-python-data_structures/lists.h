#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);
listint_t *reverse_list(listint_t *head);
listint_t *find_middle(listint_t *head);
int compare_lists(listint_t *head1, listint_t *head2);

#endif
