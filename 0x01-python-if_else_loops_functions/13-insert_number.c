#include "lists.h"

/**
 * insert_node - insert node to a sorted linked list
 *
 * @head: the start of the linked list
 * @number: the integer in list
 * Return: address of node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pre, *current, *np;

	if (!head)
		return (NULL);

	np = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	np->n = number;
	np->next = NULL;

	if (*head == NULL)
	{
		*head = np;
		return (np);
	}

	pre = NULL, current = *head;
	if (current->n > number)
	{
		np->next = current;
		*head = np;
		return (np);
	}
	while (current != NULL)
	{
		if (current->n > number)
		{
			pre->next = np;
			np->next = current;
			return (np);
		}
		pre = current;
		current = current->next;
	}
	pre->next = np;
	return (np);
}
