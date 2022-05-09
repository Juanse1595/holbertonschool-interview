#include "binary_trees.h"

/**
 * tree_lenght - calculates the lenght of a binary tree
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
 * heap_insert - inserts a value into a Max Binary Heap
 * @root: double pointer to root
 * @value: value of the new node
 * 
 * Return: pointer to the inserted node
 */

heap_t *heap_insert(heap_t **root, int value)
{
  if (*root == NULL)
    return binary_tree_node(*root, value);
}