#include "lists.h"
/**
 * check_cycle - check if the linked list has a cycle or not
 * @list: head of linked list
 * Return: return 1 if the list has a cycle, otherwise, return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	if (list == NULL)
		return (0);
	while (list)
	{
		if (list->next == NULL)
			return (0);
		list = list->next;
		if (tmp->next == NULL || tmp->next->next == NULL)
			return (0);
		tmp = tmp->next;
		tmp = tmp->next;
		if (list == tmp)
			return (1);
	}
	return (0);
}
