#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to be checked
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *current2;

	if (list == NULL)
		return (0);
	current = list;
	current2 = current->next;
	while (current2 != NULL && current != NULL)
	{
		current = current->next;
		current2 = current2->next;
		if (current2 == current)
			return (1);
		if (current2 != NULL)
			current2 = current2->next;
		if (current2 == current)
			return (1);
	}
	return (0);
}
