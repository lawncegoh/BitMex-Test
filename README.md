# BitMex-Test

**To Run** <br/> 
`python main.py`

- Uncomment the 3 lines in init to see order_book, position and balance respectively



## Extra Question:
**Explain what and where we can improve if we need a C++ version for high frequency trading**


### How can we use C++ to improve high speed trading?

In High Frequency Trading, speed of execution is very important as it can determine the amount of profits raked in.  In HFT programs that are latency sensitive, C++ can be used to improve the algorithm because it is the most efficient at processing high volumes of data. 

**Function executions**
C++ can be fast and powerful. At compile time, if we know which function is to be excecuted, we can use lambda functions instead. 
Memory allocation can be slow. So as compared to python, there are 3 changes we can make:
Pick from a pool of pre-allocated objects because allocation is costly
Reuse objects instead of deallocating: 
Even though delete involves no system calls, glibc free has 400 lines of code. Some lines may still be accessed 
this can help to avoid memory fragmentation
If we are deleting a huge object, maybe we can do it from another thread

We can add in exceptions in C++, they are claimed to be zero cost if they don’t throw. Add in exceptions for code that are not part of control flow. 

We can use templated approach rather than the branching approach. 
This code will run faster than the usual branching with if-else or conditonal operators. This is because branching is expensive. This can be done in the hot spots of the code. 

For example, for example pesudo code as follows:
At compile time, the compiler only takes 1 of these statements, but not both in the same function.

```
template<Side T> void strategy<T>::runStrategy();

template<> float Strategy<Side::Buy>::CalcPrice {
return value - $;
}

template<> float Strategy<Side::Sell>::CalcPrice {
return value + $;
}
``` 

As compared to

```
void strategy::runStrategy(input) {
if (input == buy) return value - $;
else return value + $;

}
```


**Across all functions:**
Inplace functions can be used instead of std::functions
It allocates inplace, if we declare function on stack, the buffer for the closure will be on the stack


**Multithreading**
If multiple threads are used, shared data should be kept to a minimum, copies of data can be passed around. To minimise sharing, a single writer, single reader lock free queue can be used. They only share an atomic lock.
In cases that allow for out-of-order information, can consider not to use synchronisation
