#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head node
 * Return: 0 if no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *Single = list, *Double = list;

	while (Double && Double->next)
	{
		Single = Single->next;
		Double = Double->next->next;
		if (Single == Double)
			return (1);
	}
	return (0);
}
