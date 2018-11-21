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

## Sample statistics of elapsed time (in nanosecond)
For example, I have run these two program fors 10 times respectively with the shell script run.sh, and got the data below.
It indicates the non-busy-waiting mechanism does significantly improve the performance.
* non-busy-waiting implementation (semaphore)
```csv
853072,1257084,1628118,2035620,2470156,2842895,3330136,3805943,4171814,4618277
825323,1195582,1564022,1927760,2231209,2581631,2953044,3294209,3679914,4099645
735332,1124935,1526464,1945091,2381611,2797043,3163302,3499073,3840561,4230793
694158,1093177,1493298,1859484,2229426,2639898,3029238,3470812,3856552,4344973
841312,1369721,1839416,2218672,2616791,3031801,3480380,3880915,4251430,4658613
828113,1368971,1722303,2100538,2552888,2959027,3355206,3714491,4083187,4465712
728764,1098651,1522168,2035523,2459255,2841725,3223864,3727389,4082527,4498037
791708,1126358,1582602,2035101,2407263,2749212,3120022,3500097,3863263,4322478
844881,1224855,1640394,2021437,2417618,2808877,3270092,3632904,3953764,4371616
796945,1158992,1510758,1859034,2268690,2667507,3054617,3435104,3921494,4404844

```

* busy-waiting implementation
```csv
24448739,20890084,21103381,24473514,21524173,27679360,28504099,22159868,28453774,22579511
12701310,16499266,16511120,16534789,17275356,14258888,20473341,14679081,20529757,15098302
19921394,12354519,12560618,15928541,12985496,13214860,13427165,13652663,19918621,14077775
12755327,12964358,13193773,16493607,13627367,16542700,14075035,20515569,14500672,16570549
12556495,16335783,12973735,16384649,20348105,13622679,20350794,14057677,14277012,14493720
12773904,12979308,13192784,20523258,20587644,19521488,20549408,14277114,14502688,14730995
20285331,16790286,20341029,17218498,24337339,22371420,24343893,18068897,24343511,24461325
20557308,20631902,20545041,20560743,17564059,24564761,22136814,18209173,18415315,18629962
20830973,21039070,24608933,21466477,28607897,28605610,28417273,28608896,22522448,22738330
24597798,20982478,24607768,24146621,28595448,28606135,28579491,22270162,22482728,22706622

```
