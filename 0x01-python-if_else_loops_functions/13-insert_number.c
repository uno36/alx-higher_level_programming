#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a number to sorted linked list
 * @head: pointer point to the head of list
 * @number: number need to insert
 * Return: return a pointer of the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = NULL, *prev = *head;

	if (*head == NULL || number <= current->n) 
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (number <= current->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			prev->next = new;
			new->next = current;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	new = add_nodeint_end(&prev, number);
	return (new);
}
