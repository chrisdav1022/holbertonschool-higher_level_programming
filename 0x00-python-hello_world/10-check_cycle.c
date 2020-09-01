#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: pointer to struct.
 * Return: 1 if exist and 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *check = list, *i = list;

	while (check != NULL && i != NULL && check->next != NULL)
	{
		check = check->next->next;
		i = i->next;
		if (check == i)
			return (1);
	}
	return (0);
}
