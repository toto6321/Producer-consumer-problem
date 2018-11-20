## Problem description
Assume there are three types of threads in the system, A, B, and C.
There is buffer with size of 1 between A and B, where A writes data into the buffer and B reads data from the buffer;
and another buffer of size 1 between B and C,
where B writes the data read from the first buffer into this one, and C reads the data from it.

You are asked to implement such a system with 1) busy waiting synchronization mechanism; 2) semaphore. 
Compare the above two implementations in terms of the performance (execution time), and discussion on the test cases.


## How to build
```
g++ main.c -lpthread -o run-me
g++ main_busy_waiting.c -lpthread -o run-me-2
```

## How to run
After you build it, navigate to where the file main.c/run is located and run
```
./run-me
./run-me-2 # run the other one after you stop this one by interrupting it with Ctrl + C
```

## Program overview
Here are two kind of implementation of the chained producer&consumer problem, 
busy-waiting and non-busy-waiting (semaphore) implementations.    

N_LOOP is defined to decide when to stop the infinite loop, in other words, it keeps producing and consuming until C has
consumed N_LOOP times.    

Elapsed times(in nanosecond) when process C has consumed for i times is stored in the csv files, 
statistics_non-busy-waiting.csv and statistics_busy-waiting.csv respectively, where i is from 1 to N_LOOP. We are able
to run the executable file for as many times as we want to compare the performance between these two implementation. 
Every time you run the program, the statistics will be appended to the files unless you delete it manually. 

## Algorithm explanation
Overall, it is a producer and consumer problem with two buffers. 
Therefore, the algorithm could be briefly explained below. 
(The explanation is based on the non-busy-waiting implementation with the semaphores mechanism, however, 
the design is the same as the busy-waiting.)

We have two pair of empty and full semaphores: sem_t empty[2], full[2], two mutexes sem_t mutex[2] 
and two buffer in size of 1: char buffer[2].

* Process A
```
while(1){
    // codes to write buffer 1
    P(&empty[0]);
    P(&mutex[0]);
    /* write buffer[0] */
    V(&mutex[0]);
    V(&full[0]);

}
```


* Process B
```
while(1){
    // codes to read buffer 1
    P(&full[0]);
    P(&mutex[0]);
    /* read buffer[0] */
    V(&mutex[0]);
    V(&empty[0]);


    // codes to write buffer 2
    P(&empty[1]);
    P(&mutex[1]);
    /* read buffer[0] */
    V(&mutex[1]);
    V(&full[1]);

}
```

* Process C
```
while(1){
    // codes to read buffer 2
    P(&full[1]);
    P(&mutex[1]);
    /* read buffer[1] */
    V(&mutex[1]);
    V(&empty[1]);

}
```

## Sample standard output
Use "Ctrl + C" to stop(interrupt) the program.
```
Process A is writing A into buffer1
Process B is reading A from buffer1
Process A is writing A into buffer1
Process B is writing A into buffer2
Process B is reading A from buffer1
Process C is reading A from buffer2
Process A is writing A into buffer1
Process B is writing A into buffer2
Process B is reading A from buffer1
Process C is reading A from buffer2
...
```

## Sample statistics of elapsed time
* non-busy-waiting implementation (semaphore)
```csv
756945,965165,1107142,1306778,1524885,1734640,1952864,2164769,2400079,2723903
```

* busy-waiting implementation
```csv
1134146,1810506,2543384,3164156,3657149,3935484,4626362,5458323,6151492,6901059
```
