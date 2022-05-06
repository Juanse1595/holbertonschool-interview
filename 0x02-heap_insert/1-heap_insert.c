#include "binary_trees.h"

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