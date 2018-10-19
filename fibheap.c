#include <stdio.h>
#include <malloc.h>
#include <math.h>

int total_nodes = 0;
int max_rank = 0;
int num_trees = 0;
int marked_nodes = 0;

struct node
{
	int data;
	int rank;
	struct node *prev;
	struct node *next;
	struct node *parent;
	struct node *child;
	int mark;
};

struct node *min = NULL;

struct node *new_node(int data)
{
	struct node *node = (struct node *)malloc(sizeof(struct node));
	node -> data = data;
	node -> rank = 0;
	node -> prev = NULL;
	node -> next = NULL;
	node -> parent = NULL;
	node -> child = NULL;
	node -> mark = -1;
	return node;
}

struct node *insert(int data)
{
	if(min == NULL)
	{
		min = new_node(data);
		min -> prev = min;
		min -> next = min;
		total_nodes++;
		num_trees++;
		max_rank = 1;
		return min;
	}
	else
	{
		struct node *some_node = new_node(data);
		(min -> prev) -> next = some_node;
		some_node -> prev = (min -> prev);
		some_node -> next = min;
		min -> prev = some_node;

		if(some_node -> data < min -> data)
		{
			min = some_node;
		}
		total_nodes++;
		num_trees++;
		return min;
	}
}

/*void consolidate()
{
	int numNodes = ceil(log2(total_nodes));
	struct node *aux[numNodes];
	int i = 0;
	for(i = 0; i < numNodes; numNodes++)
	{
		aux[i] = NULL;
	}

	struct node *temp = min;
	do
	{
		if(aux[temp -> rank] == NULL)
		{
			aux[temp -> rank] = temp;
		}
		else
		{
			if(temp -> data < aux[temp -> rank] -> data)
			{
				struct node *temp2 = temp;
				temp = aux[temp -> rank];
				aux[temp -> rank] = temp2;
			}
			if(aux[temp -> rank] -> child == NULL)
			{
				aux[temp -> rank] -> child = temp;
				aux[temp -> rank] -> rank++;
				if(aux[temp -> rank] == NULL)
				{
					aux[temp -> rank] = aux[temp -> rank - 1];
					aux[temp -> rank - 1] = NULL;
				}
				else
				{
					do
					{
						struct node *temp3 = aux[temp -> rank] -> child;
						struct node *temp4 = aux[temp -> rank - 1];
						aux[temp -> rank - 1] = NULL;
						(temp3 -> prev) -> next = temp4;
						temp4 -> prev = temp3 -> prev;
						temp4 -> next = temp3 -> next;
						(temp3 -> next) -> prev = temp4;
						aux[temp -> rank] -> rank++;
					}
					while(aux[temp -> rank] != NULL);
				}
			}
			else
			{
				do
				{
					struct node *temp3 = aux[temp -> rank] -> child;
					(temp3 -> prev) -> next = temp;
					temp -> prev = temp3 -> prev;
					temp -> next = temp3 -> next;
					(temp3 -> next) -> prev = temp;
					aux[temp -> rank] -> rank++;
					aux[temp -> rank - 1] = NULL;
				}
				while(aux[temp -> rank] != NULL);
			}
		}
	}
	while(temp -> next != min);
}*/

void consolidate()
{
	int numNodes = ceil(log2(total_nodes));
	struct node *aux[numNodes];
	int i = 0;
	for(i = 0; i < numNodes; numNodes++)
	{
		aux[i] = NULL;
	}

	struct node *temp = min;
	if(min == NULL)
	{
		printf("No heap exists");
		return;
	}
	do
	{
		if(aux[temp -> rank] == NULL)
		{
			aux[temp -> rank] = temp;
		}
		else
		{
			struct node *already = aux[temp -> rank];
			if(temp -> data < already -> data)
			{
				struct node *cutnode = already;
				(already -> prev) -> next = already -> next;
				(already -> next) -> prev = already -> prev;
				cutnode -> prev = NULL;
				cutnode -> next = NULL;
				if(temp -> child != NULL)
				{
					struct node *temp2 = temp -> child;
					(temp2 -> prev) -> next = cutnode;
					cutnode -> prev = temp2 -> prev;
					(temp2 -> next) -> prev = cutnode;
					cutnode -> next = temp2 -> next;
					temp -> rank = temp -> rank + 1;
					cutnode -> parent = temp;
				}
				else
				{
					temp -> child = cutnode;
					cutnode -> parent = temp;
					temp -> rank = temp -> rank + 1;
				}
			}
			else
			{
				if(already -> child != NULL)
				{
					struct node *temp2 = already -> child;
					(temp2 -> prev) -> next = temp;
					temp -> prev = temp2 -> prev;
					(temp2 -> next) -> prev = temp;
					temp -> next = temp2 -> next;
					already -> rank = already -> rank + 1;
					temp -> parent = already;
				}
				else
				{
					already -> child = temp;
					temp -> parent = already;
					already -> rank  = already -> rank + 1;
				}
			}
		}
	}
	while(temp != min);
	temp = temp -> next;
}

int extractMin()
{
	if(min == NULL)
	{
		return -1;
	}
	else if(min -> child == NULL)
	{
		int retData = min -> data;
		struct node *temp = min;
		if(temp -> prev == temp && temp -> next == temp)
		{
			temp -> prev = temp -> next = NULL;
			min = NULL;
			free(temp);
			total_nodes--;
			num_trees--;
			return retData;
		}
		(temp -> prev) -> next = temp -> next;
		(temp -> next) -> prev = temp -> prev;
		min = temp -> prev;
		free(temp);
		temp = min;
		struct node *temp2 = min;
		do
		{
			if(temp -> data < min -> data)
			{
				temp2 = temp;
			}
			temp = temp -> next;
		}
		while(temp -> next != min);
		min = temp2;
		total_nodes--;
		num_trees--;
		consolidate();
		return retData;
	}
	else if(min -> child != NULL)
	{
		if(min -> prev == min && min -> next == min)
		{
			int retData = min -> data;
			struct node *todel = min;
			struct node *inside = min -> child;
			struct node *temp = inside;
			struct node *mintemp = inside;
			int counter = 0;
			do
			{
				temp -> parent = NULL;
				if(temp -> data < mintemp -> data)
				{
					mintemp = temp;
				}
				counter++;
				temp = temp -> next;
			}
			while(temp -> next != inside);
			min = mintemp;
			free(todel);
			total_nodes--;
			num_trees += counter - 1;
			consolidate();
			return retData;
		}
		else
		{
			int counter = 0;
			int retData = min -> data;
			struct node *todel = min;
			struct node *inside = min -> child;
			inside -> prev = todel -> prev;
			(todel -> prev) -> next = inside;
			todel -> prev = NULL;
			struct node *temp = inside;
			struct node *mintemp = inside;
			do
			{
				temp -> parent = NULL;
				if(temp -> data < mintemp -> data)
				{
					mintemp = temp;
				}
				counter++;
				temp = temp -> next;
			}
			while(temp -> next != inside);
			(todel -> next) -> prev = temp;
			temp -> next = todel -> next;
			todel -> next = NULL;
			min = mintemp;
			free(todel);
			total_nodes--;
			num_trees += counter - 1;
			consolidate();
			return retData;
		}
	}
}

int flag = 0;
struct node *decreaseKey(int key, int updatedVal, struct node *root)
{
	if(root -> data == key)
	{
		if(root -> parent == NULL)
		{
			root -> data = updatedVal;
			if(root -> data < min -> data)
			{
				min = root;
			}
			flag = 1;
			return min;
		}
		else
		{
			root -> data = updatedVal;
			if(root -> data < root -> parent -> data)
			{
				(min -> prev) -> next = root;
				root -> prev = min -> prev;
				root -> next = min;
				min -> prev = root;

				if(root -> parent -> mark == 0)
				{
					root -> parent -> mark = 1;
					root -> parent -> rank--;
					root -> parent = NULL;
					(root -> prev) -> next = root -> next;
					(root -> next) -> prev = root -> prev;
				}
				else
				{
					// WHILE LOGIC
					while(root -> parent -> mark != 0 || root -> parent == NULL)
					{
						if(root -> parent == NULL)
						{
							root -> mark = 1;
							break;
						}
						(min -> prev) -> next = root;
						root -> prev = min -> prev;
						root -> next = min -> next;
						(min -> next) -> prev = root;
						struct node *temp = root -> parent;
						temp -> mark = 0;
						temp -> rank --;
						root -> parent = NULL;
						root = temp;
					}
				}
			}
			flag = 1;
		}
	}
	else
	{
		// AGAIN SOME BACKTRACKING CODE
		if(root -> next != root)
		{
			decreaseKey(key, updatedVal, root -> next);
			if(flag == 0)
			{
				if(root -> next -> child != NULL)
				{
					decreaseKey(key, updatedVal, root -> next -> child);
				}
			}
		}
		else
		{
			decreaseKey(key, updatedVal, root -> child);
			if(flag == 0)
			{
				if(root -> child -> next != root -> child)
				{
					decreaseKey(key, updatedVal, root -> child -> next);
				}
			}
		}
	}
}

int delete(int key)
{
	min = decreaseKey(key, -256, min);
	return extractMin();
}

void print_nodes()
{
	if(min == NULL)
	{
		printf("No nodes in the heap.\n");
		return;
	}
	struct node *temp = min;
	printf("Minimum is %d\n" , min ->  data);
	do
	{
		printf("Node is %d\n", temp -> data);
		temp = temp -> next;
	}
	while(temp != min);
	return;
}

int main(void)
{
	min = insert(21);
	min = insert(2);
	print_nodes();
	int retData = extractMin();
	printf("Extracted value is %d\n", retData);
}
