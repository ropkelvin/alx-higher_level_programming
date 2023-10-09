#include "lists.h"

/**
 * check_palindrome - check for palindrome
 * @first: pointer
 * @last: pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int check_palindrome(listint_t **first, listint_t *last)
{
	int i;

	if (last == NULL)
		return (1);
	i = check_palindrome(first, last->next);
	if (i == 0)
		return (0);
	if ((*first)->i == last->i)
		i = 1;
	else
		i = 0;
	*first = (*first)->next;
	return (i);
}

/**
 * is_palindrome - check if list is palindrome
 * @head: pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t **tmp, *curr;

	tmp = head;
	curr = *head;

	if (*head == NULL)
		return (1);
	return (check_palindrome(tmp, curr));
}