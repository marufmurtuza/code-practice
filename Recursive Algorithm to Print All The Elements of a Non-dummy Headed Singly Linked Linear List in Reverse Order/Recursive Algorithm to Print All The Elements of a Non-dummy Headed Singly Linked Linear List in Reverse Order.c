#include <iostream>

using namespace std;

struct Node {

    int k;

    struct Node * next;

    Node(int k){

        this -> k = k;

        next = NULL;
    }
};

struct ourlist {

    Node * head;

    ourlist(){

        head = NULL;

    }


    Node * listreversefunction(Node * node){
        if (node == NULL){

          return NULL;

        }

        if (node -> next == NULL){

            head = node;

            return node;
        }

        Node * node_x = listreversefunction(node -> next);

        node_x -> next = node;

        node -> next = NULL;

        return node;
    }


    void listprint(){

        struct Node * temp = head;

        while (temp != NULL){

            cout << temp->k << " ";

            temp = temp -> next;
        }
    }

    void push(int data){

        Node * temp = new Node(data);

        temp -> next = head;

        head = temp;
    }
};


int main()
{
    ourlist l;

    int i , elementk , element;

    printf("\nEnter the k of element you want to insert: ");

    scanf("%d",&elementk);

    printf("\n");

    for(i=0;i<elementk;i++){

        printf("Push element %d: ",i);

        scanf("%d",&element);

        l.push(element);
    }


    printf("\nGiven List: \n");

    l.listprint();

    l.listreversefunction(l.head);

    printf("\n\nReversed List: \n");

    l.listprint();

    printf("\n");

    return 0;
}