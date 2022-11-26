#pragma once
/*
  dlist.h
  Doubly-linked lists of ints
 */
class dlist {
  public:

	// You don't need to modify the constructor, node struct, or head/tail methods.

    dlist()
    { }

    struct node {
		node(int value, node* next, node* prev) :
			value(value), next(next), prev(prev)
		{ }

        int value;
        node* next;
        node* prev;
    };

    node* head() const { return _head; };
    node* tail() const { return _tail; };

    // **** Implement ALL the following methods ****

    // Returns the node at a particular index (0 is the head). If n >= size()
    // return nullptr; if n < 0, return the head of the list.
    // Must run in O(n) time.
    node* at(int n) const{
      if(n >= size())
        return nullptr;
      else if(n < 0)
        return _head;
      else
      {
        node* current = _head;
        for(int i = 0; i < n; i++)
        current = current->next;
        return current;
      }
    };

    // Insert a new value, after an existing one. If previous == nullptr, then
    // the element is added *before* the head.
    // Must run in O(1) time.
    void insert(node *previous, int value)
    {
      node* n = new node();
      n->value = value;
      n->next = nullptr;
      n->prev = nullptr;

      if(previous == nullptr) //list is empty or insertion before head
      {
        n->next = _head;
      }
      if(n->next != nullptr)
        {n->next->prev = n;
        }
      if(_tail == nullptr){
        _tail = n;
        _head = n;
      }
      else
      {
        //set the 4 links when a node is inserted after previous- i.e. 2 links from n to previous and next node
        //1 link from previous to n and next node to n
        n->next = previous->next;
        n->prev = previous;
        if(n->next != nullptr) {
          n->next->prev = n;
          previous->next = n;
        }

        if(previous == _tail){
          _tail = n;
        }
      }
};

    // Delete the given node. Should do nothing if which == nullptr.
    // Must run in O(1) time.
    void remove(node* which);

    // Add a new element to the *end* of the list
    // Must run in O(1) time.
    void push_back(int value);

    // Add a new element to the *beginning* of the list
    // Must run in O(1) time.
    void push_front(int value);

    // Remove the first element
    // Must run in O(1) time
    void pop_front() {remove(_head);};

    // Remove the last element
    // Must run in O(1) time
    void pop_back() {remove(_tail);};

    // Get the size of the list
    // Should run in O(n) time at the worst
    int size() const
    {
      node* n = _head;
      int count = 0;
      while(n != nullptr)
      {
        n = n->next;
        count++;
      }
      return count;
    };

    // Returns true if the list is empty
    // Must run in O(1) time
    bool empty() const {return _head == nullptr;};

  private:
    node* _head = nullptr;
    node* _tail = nullptr;
};

// **** Implement ALL the following functions ****

/* a == b
   Compares two lists for equality, returning true if they have the same
   elements in the same positions. (Hint: it is *not* enough to just compare
   pointers! You have to compare the values stored in the nodes.)

   Must run in O(m) time, where m is the length of the shorter of the two lists.
*/
bool operator== (const dlist& a, const dlist& b);

/* a + b
   Returns a new list consisting of all the elements of a, followed by all the
   elements of b (i.e., the list concatenation).

   Must run in O(n) time in the length of the result.
*/
dlist operator+ (const dlist& a, const dlist& b);

/* reverse(l)
   Returns a new list that is the *reversal* of l; that is, a new list
   containing the same elements as l but in the reverse order.

   Must run in O(n) time.
*/
dlist reverse(const dlist& l);
