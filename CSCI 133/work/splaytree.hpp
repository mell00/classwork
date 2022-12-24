#pragma once
#include <cassert>
#include <stdexcept>
#include<iostream>
#include<string>
using namespace std;

class splay_tree {
  public:
    struct node
    {
        node(int key, node* left, node* right, node* parent) :
            key(key), left(left), right(right), parent(parent)
        { }

        int key;
        node* left;
        node* right;
        node* parent;
    };

    ~splay_tree()
    {
        clear();
    }

    /* root()
       Returns the root of the tree.

       Runs in O(1) time.
    */
    node* root() const
    {
        return rt;
    }

    /* size()
       Wrapper function for size(n).

       Runs in O(n) time.
    */

    int size() const
    {
        // Remove the next line and add your code here.
        return size(rt);
    }

    /* size(n)
       Returns the size (total number of nodes) in the tree.
       Runs in O(n) time.
    */

    int size(node *n) const
    {
      if ((rt == nullptr) && (rt->right == nullptr) && (rt->left == nullptr)){
        return 0;
      }
      return 1 + size(n->right) + size(n->left);
    }

    /* empty()
       Returns true if the tree is empty.

       Runs in O(1) time.
    */
    bool empty() const
    {
        // Remove the next line and add your code here.
        if (rt == nullptr) return true;
        return false;
    }

    /* rotate(c,p)
       Rotate child node c with parent node p. c must be a child of p
       (either c == p->left or c == p->right) and neither c nor p can be
       nullptr.

       Runs in O(1) time.
    */
    static void rotate(node* c, node* p)
    {
        assert(c != nullptr and p != nullptr);
        assert(c == p->left or  c == p->right);
        assert(c->parent == p);

        // Remove the next line and add your code here.
        throw std::logic_error("Not implemented");
    }

    static void left_rotation(node* c,node* p)
    {
      c = p->right;
      p->right = c->left;
      c->left = 

    }

    /* splay(n)
       Splays n to the root of the tree, returning the new root. n must not
       be nullptr.

       As with `rotate`, splay is a static member function, so it is not allowed
       to access any member variables (it can call `rotate`, however).

       Runs in O(d) time where d is the depth of node n (amortized, this
       will be O(log n)).
    */
    static node* splay(node* n)
    {
        assert(n != nullptr);

        // Remove the next line and add your code here.
        throw std::logic_error("Not implemented");
    }

    /* find(k)
       Finds and returns the node containing key k, splaying it to the root.
       If no such node exists, then `find` splay's the parent of the location
       where k *should* be to the root, and then returns the new root. If the
       tree is empty, returns nullptr. To determine whether a key k exists in
       the (nonempty) tree, you would check

            k == find(k)->key

       Runs in O(log n) amortized time.
    */
    node* find(int k)
    {
        // Remove the next line and add your code here.
        node *n = root();
        if(n == nullptr) return nullptr;
        else if(k == n->value) return n; //Found!
        else if(k < n->value) return find(n->left,k);
        else if(k > n->value) return find(n->right,k);
    }

    /* insert(k)
       Inserts k into the tree, splaying the new node to the root. If k
       already exists in the tree, it should be splayed to the root. Returns
       the new root of the tree.

       Runs in O(log n) amortized time.
    */
    node* insert(int k)
    {
        node *root = root();
        // Remove the next line and add your code here.
        if(root == nullptr)
          node *n = new node{k,nullptr,nullptr}; //{value, left, right}
          splay(n);
          return root;
        else {
          node* p = parent(root,k);
          if(k < p->value and p->left != nullptr)
            splay(k);
            return root; //k already exists on the left
          if(k > p->value and p->right != nullptr)
            splay(k);
            return root; //k already exists on the right
          if (k < p->value){
            p->left = new node{k,nullptr,nullptr};
            splay(p->left);
            return root;
          } else {
            p->right = new node{k,nullptr,nullptr};
            splay(p->right);
            return root;
          }
    }

    /* remove(k)
       EXTRA CREDIT: Removes the node containing k, and splays its parent to
       the root. If k does not exist in the tree, then nothing is removed,
       but the parent (of where k *should* exist) is still splayed. Returns
       the new root of the tree.

       Runs in O(log n) amortized time.
    */
    node* remove(int k)
    {
        // If you want to do the extra credit problem, remove the next line.
        if (find(k) == nullptr){
          splay(k->parent);
          return root;
        } else {
          node *p = k->parent;
          if ((k->left == nullptr) && (k->right == nullptr)){
          delete k;
          splay(p);
          } else if ((k->left == nullptr) && (k->right != nullptr)){

          } else if ((k->left != nullptr) && (k->right == nullptr)){

          }
        }

    }

    /* set_root(n)
       Replaces the root node with n; this is only used for testing.
    */
    void set_root(node* n)
    {
        rt = n;
    }

    /* clear()
       Delete all nodes in the tree. You should implement the recursive
       `clear(node*)` version below, and not modify this one.
    */
    void clear()
    {
        clear(rt);
    }

  private:

    /* clear(n)
       Delete n and all its descendants.
    */
    void clear(node* n)
    {
        throw std::logic_error("Not implemented");
    }

    node* rt = nullptr;
};
