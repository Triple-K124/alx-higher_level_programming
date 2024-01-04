/*
 * File: 10-check_cycle.c
 * Auth: Kalu Kelechi Kalu
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *turt, *har;

	if (list == NULL || list->next == NULL)
		return (0);

	turt = list->next;
	har = list->next->next;

	while (turt && har && har->next)
	{
		if (turt == har)
			return (1);

		turt = turt->next;
		har = har->next->next;
	}

	return (0);
}
