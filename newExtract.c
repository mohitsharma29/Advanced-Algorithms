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