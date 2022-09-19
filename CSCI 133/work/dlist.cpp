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

    node* head() const { return _head; }
    node* tail() const { return _tail; }

    // **** Implement ALL the following methods ****

    // Returns the node at a particular index (0 is the head). If n >= size()
    // return nullptr; if n < 0, return the head of the list.
    // Must run in O(n) time.
    node* at(int n) const;

    // Insert a new value, after an existing one. If previous == nullptr, then
    // the element is added *before* the head.
    // Must run in O(1) time.
    void insert(node *previous, int value);
    {
      if(a == nullptr) {
        // Insert new head
        hd = new node{x,hd}; // {value,next}

        if(tl == nullptr){
          tl = n;
        }
      }
      else {
        // Insert after a
        a->next = new node{x,a->next} //only working with node POINTERS

        if(a == t1)
          t1 = n;
      }
    }
    // Delete the given node. Should do nothing if which == nullptr.
    // Must run in O(1) time.
    void remove(node* which);

    // Add a new element to the *end* of the list
    // Must run in O(1) time.
    void push_back(int value);
    {
      insert(tl, x);
    }
    // Add a new element to the *beginning* of the list
    // Must run in O(1) time.
    void push_front(int value);
    {
      insert(nullptr, x);
    }
    // Remove the first element
    // Must run in O(1) time
    void pop_front();

    // Remove the last element
    // Must run in O(1) time
    void pop_back();

    // Get the size of the list
    // Should run in O(n) time at the worst
    int size() const;

    // Returns true if the list is empty
    // Must run in O(1) time
    bool empty() const;

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
