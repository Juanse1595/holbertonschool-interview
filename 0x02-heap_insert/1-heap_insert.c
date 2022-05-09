#include "binary_trees.h"

/**
 * tree_length - calculates the lenght of a binary tree
 * @root: pointer to the head of the tree
 *
 * Return: length of the tree
 */

int tree_length(heap_t **root)
{
	if (root == NULL || *root == NULL)
		return (0);

	return (tree_length(&((*root)->left)) + tree_length(&((*root)->right)) + 1);
}

/**
 * get_parent_node - get the parent node to insert new node below
 * @root: root of the tree
 * @index: number of nodes
 *
 * Return: none
 */

void get_parent_node(heap_t **root, int index)
{
	int parent_index = (index - 1) / 2;

	/* base case */
	if (root == NULL || index == 0)
	{
		return;
	}

	get_parent_node(root, parent_index);
	if (parent_index > 0 && parent_index % 2 == 0)
	{
		(*root) = (*root)->right;
	}
	if (parent_index > 0 && parent_index % 2 != 0)
	{
		(*root) = (*root)->left;
	}
}

void swap_values(heap_t *current)
{
	int tmp;
	if (current->parent == NULL)
		return;

	if (current->n > (current->parent)->n)
	{
		tmp = current->n;
		current->n = (current->parent)->n;
		(current->parent)->n = tmp;
	}

	swap_values(current->parent);
}

/**
 * heap_insert - inserts a value into a Max Binary Heap
 * @root: double pointer to root
 * @value: value of the new node
 *
 * Return: pointer to the inserted node
 */

heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *parent_node = *root;
	heap_t *new_node = NULL;
	int index = tree_length(root);

	if (root == NULL)
		return (NULL);

	new_node = malloc(sizeof(heap_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = value;
	new_node->left = new_node->parent = new_node->right = NULL;

	if (*root == NULL)
	{
		*root = new_node;
		return (new_node);
	}

	get_parent_node(&parent_node, index);
	new_node->parent = parent_node;
	if (parent_node->left == NULL)
	{
		parent_node->left = new_node;
	}
	else
	{
		parent_node->right = new_node;
	}

	swap_values(new_node);

	return (new_node);

}
