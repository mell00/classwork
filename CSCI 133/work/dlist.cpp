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
    dlist::node* dlist::at(int n) const
    {
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
    void dlist::insert(node *previous, int value)
    {
      node* n = new node();
      n->value = value;
      n->next = nullptr;
      n->prev = nullptr;

      if(previous == nullptr)
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
    void dlist::remove(node* which)
    {
    if(which == nullptr){
      return;
    }
    else
    {
      node* prev = which->prev;
      node* next = which->next;

      if(prev != nullptr){
        prev->next = which->next;
      }
      if(next != nullptr){
        next->prev = prev;
      }
      if(which == _head){
        _head = next;
      }
      if(which == _tail){
        _tail = prev;
      }
      delete which;
      }
    };


    // Add a new element to the *end* of the list
    // Must run in O(1) time.
    void dlist::push_back(int value)
    {
      insert(_tail, value);
    };
    // Add a new element to the *beginning* of the list
    // Must run in O(1) time.
    void dlist::push_front(int value)
    {
      insert(nullptr, value);
    };
    // Remove the first element
    // Must run in O(1) time
    void dlist::pop_front()
    {
      remove(_head);
    };

    // Remove the last element
    // Must run in O(1) time
    void dlist::pop_back()
    {
      remove(_tail);
    };

    // Get the size of the list
    // Should run in O(n) time at the worst
    int dlist::size() const
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
    bool dlist::empty() const
    {return _head == nullptr;}

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
bool operator== (const dlist& a, const dlist& b)
{
  int size1 = a.size();
  int size2 = b.size();
  if(size1 != size2){
      return false;
  }
  else
  {
    for(int i = 0; i < size1; i++)
    {
      dlist::node* n1 = a.at(i);
      dlist::node* n2 = b.at(i);
      if(n1->value != n2->value){
        return false;
      }
    }
  }

  return true;
};

/* a + b
   Returns a new list consisting of all the elements of a, followed by all the
   elements of b (i.e., the list concatenation).

   Must run in O(n) time in the length of the result.
*/
dlist operator+ (const dlist& a, const dlist& b)
{
  dlist res;
  int sz = a.size();
  for(int i = 0;i < sz; i++)
  {
    res.push_back(a.at(i)->value);
  }

  sz = b.size();
  for(int i = 0;i < sz; i++)
  {
    res.push_back(b.at(i)->value);
  }
  return res;
};

/* reverse(l)
   Returns a new list that is the *reversal* of l; that is, a new list
   containing the same elements as l but in the reverse order.

   Must run in O(n) time.
*/
dlist reverse(const dlist& l)
{
  dlist list;
  int sz = l.size();
  for(int i = 0; i < sz; i++){
    list.push_front(l.at(i)->value);
  }
  return list;
};
