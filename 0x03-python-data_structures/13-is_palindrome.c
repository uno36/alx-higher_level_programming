#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *reverse_listint(listint_t **head);
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer that points to the address of the head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *cur = *head, *rev = NULL, *tmp1 = *head;
	int count = 0, tmp_count = 0, match = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp)
	{
		tmp = tmp->next;
		count++;
	}
	for (tmp_count = count / 2; tmp_count > 0; tmp_count--)
	{
		cur = cur->next;
	}
	rev = reverse_listint(&cur);
	i = count / 2;
	while (i > 0)
	{
		if (rev->n == tmp1->n)
			match = 1;
		else
		{
			match = 0;
			break;
		}
		rev = rev->next;
		tmp1 = tmp1->next;
		i--;
	}
	if (match == 1)
		return (1);
	else
		return (0);
}
/**
 * reverse_listint -  reverses a listint_t linked list.
 * @head: pointer that points to the address of head node of list
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev_node, *next_node;

	prev_node = NULL;
	next_node = NULL;
	while (*head != NULL)
	{
		next_node = (*head)->next;/* move next node forward*/
		(*head)->next = prev_node;/* change direction/point backward*/
		prev_node = *head;/* after change dir,move prev_node forward */
		*head = next_node; /* move head forward */
	}
	*head = prev_node;/* change head points to prev_node instead of NULL */
	return (*head);
}
