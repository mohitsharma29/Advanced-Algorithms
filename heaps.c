#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct node
{
	int data;
	struct node *leftChild;
	struct node *rightChild;
};

struct node *root = NULL;
int num_of_nodes = 0;
int bits[32];

struct node *new_node(int data)
{
	struct node *node = (struct node *)malloc(sizeof(struct node));
	node -> data = data;
	node -> leftChild = NULL;
	node -> rightChild = NULL;
	return node;
};

void recompute()
{
	int temp = num_of_nodes + 1;
	int i = (int)log2(num_of_nodes + 1);
	while(temp != 0)
	{
		bits[i] = temp%2;
		temp /= 2;
		i--;
	}
}

int isEmpty()
{
	if(root == NULL && num_of_nodes == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void insert(struct node *some_node, int data, int bits[], int index)
{
	if(isEmpty())
	{
		root = new_node(data);
		num_of_nodes++;
	}
	else
	{
		if(bits[index] == 0 && some_node -> leftChild == NULL)
		{
			some_node -> leftChild = new_node(data);
			if(some_node -> leftChild -> data < some_node -> data)
			{
				int temp = some_node -> leftChild -> data;
				some_node -> leftChild -> data = some_node -> data;
				some_node -> data = temp;
			}
			num_of_nodes++;
		}
		else if(bits[index] == 1 && some_node -> rightChild == NULL)
		{
			some_node -> rightChild = new_node(data);
			if(some_node -> rightChild -> data < some_node -> data)
			{
				int temp = some_node -> rightChild -> data;
				some_node -> rightChild -> data = some_node -> data;
				some_node -> data = temp;
			}
			num_of_nodes++;
		}
		else if(bits[index] == 0 && some_node -> leftChild != NULL)
		{
			insert(some_node -> leftChild, data, bits, index + 1);
			if(some_node -> leftChild -> data < some_node -> data)
			{
				int temp = some_node -> leftChild -> data;
				some_node -> leftChild -> data = some_node -> data;
				some_node -> data = temp;
			}
		}
		else if(bits[index] == 1 && some_node -> rightChild != NULL)
		{
			insert(some_node -> rightChild, data, bits, index + 1);
			if(some_node -> rightChild -> data < some_node -> data)
			{
				int temp = some_node -> rightChild -> data;
				some_node -> rightChild -> data = some_node -> data;
				some_node -> data = temp;
			}
		}
	}
}

void heapify(struct node *root)
{
	if(root != NULL)
	{
		if(root -> leftChild != NULL && root -> rightChild != NULL)
		{
			if((root -> data > root -> leftChild -> data) || (root -> data > root -> rightChild -> data))
			{
				if(root -> leftChild -> data < root -> rightChild -> data)
				{
					int temp = root -> leftChild -> data;
					root -> leftChild -> data = root -> data;
					root -> data = temp;
					heapify(root -> leftChild);
				}
				else
				{
					int temp = root -> rightChild -> data;
					root -> rightChild -> data = root -> data;
					root -> data = temp;
					heapify(root -> rightChild);
				}
			}
			else
			{
				return;
			}
		}
		else if(root -> leftChild == NULL || root -> rightChild == NULL)
		{
			if(root -> leftChild == NULL && root -> rightChild == NULL)
			{
				return;
			}
			else if(root -> leftChild == NULL)
			{
				if(root -> data > root -> rightChild -> data)
				{
					int temp = root -> rightChild -> data;
					root -> rightChild -> data = root -> data;
					root -> data = temp;
					heapify(root -> rightChild);
				}
				else
				{
					return;
				}
			}
			else if(root -> rightChild == NULL)
			{
				if(root -> data > root -> leftChild -> data)
				{
					int temp = root -> leftChild -> data;
					root -> leftChild -> data = root -> data;
					root -> data = temp;
					heapify(root -> leftChild);
				}
				else
				{
					return;
				}
			}
		}

	}
	else
	{
		return;
	}
}

int extract_min()
{
	if(isEmpty())
	{
		return -1;
	}
	else
	{
		int return_value,flag;
		int temp = num_of_nodes;
		int i = (int)log2(num_of_nodes);
		while(temp != 0)
		{
			bits[i] = temp%2;
			temp /= 2;
			i--;
		}
		i = 1;
		struct node *temp_node;
		struct node *prev_node;
		temp_node = root;
		prev_node = root;
		return_value = root -> data;
		while(!(temp_node -> leftChild == NULL && temp_node -> rightChild == NULL))
		{
			if(bits[i] == 0)
			{
				prev_node = temp_node;
				temp_node = temp_node -> leftChild;
				i++;
				flag = 1;
			}
			else
			{
				prev_node = temp_node;
				temp_node = temp_node -> rightChild;
				i++;
				flag = -1;
			}
		}
		root -> data = temp_node -> data;
		if(flag == 1)
		{
			prev_node -> leftChild = NULL;
		}
		else if(flag == -1)
		{
			prev_node -> rightChild = NULL;
		}
		free(temp_node);
		num_of_nodes--;
		if(num_of_nodes == 0)
		{
			root = NULL;
		}
		heapify(root);
		return return_value;
	}
}

void traverse(struct node *root)
{
	if(root != NULL)
	{
		printf("%d\n" , root -> data);
		traverse(root ->  leftChild);
		traverse(root -> rightChild);
	}
	else
	{
		return;
	}
}

int main(int argc, char *argv[])
{
	int i = 0;
	for(i = 0; i < 32; i++)
	{
		bits[i] = 0;
	}

	insert(root, 10, bits, 1);

	recompute();
	insert(root, 2, bits, 1);

	recompute();
	insert(root, 1, bits, 1);

	recompute();
	insert(root, 0, bits, 1);

	printf("The minimum is %d.\n" , extract_min());
	traverse(root);
	return 0;
}