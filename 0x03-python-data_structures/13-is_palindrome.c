#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 * Return: returns 1 if it is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i, j, len = 0;
	listint_t *use = *head;
	listint_t *use2 = *head;

	if (head == NULL)
		return (0);
	while (use != NULL)
	{
		len++;
		use = use->next;
	}
	int arr[len];

	for (i = 0; i < len; i++)
	{
		arr[i] = use2->n;
		use2 = use2->next;
	}
	for (i = 0, j = len - 1; i < len && j >= 0; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
