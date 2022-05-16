package sample;

import java.util.Iterator;
import java.util.NoSuchElementException;

//Johnny Rivera
//This code allows the file TestMyCircularLinkedList.Java to run test on managing items in a list using Iterators and Nodes. The code allows the user to add,remove elements to the list even allowing further modifications such as removing and adding first element of the list
//as well as the last. The test file returns the values of the test that were successful.
public class MyCircularLinkedList<E> implements MyList<E>
{
    private class Node<T>
    {
        T element;
        Node<T> next;

        public Node(T element)
        {
            this.element = element;
            next = null;
        }

    }

    private Node<E> tail;
    private int size;
    
    public MyCircularLinkedList()
    {
        tail = null;
        size = 0;
    }


    public boolean add(E element) {
        addLast(element);
        return false;
    }


    public void add(int index, E e)
    {
       
        if(index >= 0 && index <=size)
        {
            if(index == 0)
                addFirst(e);
            else if(index == size)
                addLast(e);
            else
            {
                int n = 0;
                Node<E> current = tail.next;
                Node<E> end = tail;

                while(n < index)
                {
                    end = current;
                    current = current.next;
                    n++;
                }

                Node<E> node = new Node<E>(e);
                end.next = node;
                node.next = current;
                size++;
            }
        }else
            throw new IndexOutOfBoundsException("Illegal index of "+index+" passed to CircularLinkedList remove method.");

    }
    
    public E get(int index)
    {
  
        if(index >= 0 && index < size)
        {
            if(index == 0)
                return getFirst();
            else if(index == size-1)
                return getLast();
            else
            {
                Node<E> current = tail.next;

                int currentIndex = 0;
   
                while(currentIndex < index)
                {
                    current = current.next;
                    currentIndex++;
                }
        
                return current.element;

            }
        }else
            throw new IndexOutOfBoundsException("Illegal index of "+index+" passed to MyCircularLinkedList get method.");
    }


    public int indexOf(Object e)
    {
        if(size > 0)
        {
            int index = 0;
            Node<E> current = tail.next;

            while(true)
            {
                if(current.element.equals(e))
                    return index;
                else if(current == tail)
                    break;
                current = current.next;
                index++;
            }

        }

        return -1;
    }

    
    public int lastIndexOf(E e)
    {
        int n = -1;

        if(size > 0)
        {
            int index = 0;
            Node<E> current = tail.next;

            while(true)
            {
                if(current.element.equals(e))
                    n = index;
                else if(current == tail)
                    break;
                current = current.next;
                index++;
            }

        }

        return n;
    }
    public E remove(int index)
    {
        if(index >=0 && index < size)
        {
            if(index == 0)
                return removeFirst();
            else if(index == size-1)
                return removeLast();
            else
            {
                Node<E> current = tail.next;
                Node<E> endv = tail;

                int currentIndex = 0;
                while(currentIndex < index)
                {
                    endv = current;
                    current = current.next;
                    currentIndex++;
                }

                endv.next = current.next;
                size--;
                return current.element;
            }
        }else
            throw new IndexOutOfBoundsException("Illegal index of "+index+" passed to CircularLinkedList remove method.");
    }

    public E set(int index, E e)
    {
        if(index >= 0 && index < size)
        {
            if(index == 0)
            {
                E element = tail.next.element;
                tail.next.element = e;
                return element;
            }
            else if(index == size-1)
            {
                E element = tail.element;
                tail.element = e;
                return element;
            }else
            {
                Node<E> current = tail.next;

                int currentIndex = 0;
                while(currentIndex < index)
                {
                    current = current.next;
                    currentIndex++;
                }


                E element = current.element;
                current.element = e;
                return element;
            }
        }else
            throw new IndexOutOfBoundsException("Illegal index of "+index+" passed to CircularLinkedList set method.");
    }

    public boolean contains(Object e)
    {
        return(indexOf(e) != -1);
    }

    public int size()
    {
        return size;
    }

    public String toString()
    {
        String string = "[";
        if(size > 0)
        {
            Node<E> current = tail.next;

            while(current != tail)
            {
                string += current.element.toString()+", ";
                current = current.next;
            }

            string += tail.element.toString();
        }

        string += "]";

        return string;
    }

    public void clear()
    {
        tail = null;
        size = 0;
    }

    public void addFirst(E e)
    {
        Node<E> node = new Node<E>(e);
        if(tail == null)
        {
            tail = node;
            tail.next = tail;
        }else
        {
            node.next = tail.next;
            tail.next = node;
        }
        size++;
    }

    public void addLast(E e)
    {
        Node<E> node = new Node<E>(e);
        if(tail == null)
        {
            tail = node;
            tail.next = tail;
        }else
        {
            node.next = tail.next;
            tail.next = node;
            tail = node;
        }
        size++;
    }

    public E getFirst()
    {
        if(tail == null)
            throw new NoSuchElementException();
        return tail.next.element;
    }

    public E getLast()
    {
        if(tail == null)
            throw new NoSuchElementException();
        return tail.element;
    }

    public E removeFirst()
    {
        if(tail != null)
        {
            E element = tail.next.element;
            if(tail.next == tail)
            {
                tail = null;
            }else
                tail.next = tail.next.next;
            size--;
            return element;
        }

        throw new NoSuchElementException();
    }

    public E removeLast()
    {
        if(tail != null)
        {
            E element = tail.element;
            if(tail.next == tail)
            {
                tail = null;
            }else
            {
                Node<E> current = tail.next;

                while(current.next != tail)
                    current = current.next;

                current.next = tail.next;
                tail = current;

            }
            size--;
            return element;
        }

        throw new NoSuchElementException();
    }

    public Iterator<E> iterator()
    {
        return new MyCircularLinkedListIterator();
    }

    private class MyCircularLinkedListIterator implements Iterator<E>
    {

        private Node current;
        int n ;
        public MyCircularLinkedListIterator()
        {
            n = 0;
            current = tail.next;
        }

        @Override
        public boolean hasNext() {
            return (n < size);
        }

        @Override
        public E next() {
            n++;
            E element = (E) current.element;
            current = current.next;
            return element;
        }

        @Override
        public void remove()
        {
            throw new UnsupportedOperationException();
        }

    }

}
