#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 * Return: returns 1 if it is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *Single = *head;
	listint_t *Static = *head;
	listint_t *Double = *head;

	if (head == NULL || *head == NULL)
		return (1);
	while (Double->next != NULL && Double->next->next != NULL)
	{
		Single = Single->next;
		Double = Double->next->next;
	}
	Single = Single->next;
	Single = rev_list(Single);
	while (Single != NULL)
	{
		if (Static->n != Single->n)
		{
			return (0);
		}
		Static = Static->next;
		Single = Single->next;
	}
	return (1);
}

/**
 * rev_list - reverses a list
 * @temp: head of the list
 * Return: the head of the reversed list
 */
listint_t *rev_list(listint_t *temp)
{
	listint_t *temp1 = temp, *temp2 = NULL, *temp3 = NULL;

	while (temp1 != NULL)
	{
		temp3 = temp1->next;
		temp1->next = temp2;
		temp2 = temp1;
		temp1 = temp3;
	}
	return (temp2);
}
