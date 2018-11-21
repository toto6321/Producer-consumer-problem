## Performance analyses
With the statistics files, we can calculate the average accumulative elapsed time and 
the standard derivation for each mechanism. Observing the following charts and recalling the implementation details, 
we can conclude that the busy-waiting mechanism is able to work on the issue about shared data synchronization. 
However, it wastes a lot of time grasping the CPU. In addition, for some reason, the behavior of it is pretty unstable 
and even much weird in our experiments. Non-busy-waiting mechanism(semaphore mechanism) is a profound breakthrough 
becuase it does improve the performance a lot.  

1. N_LOOP = 10

![Performance_of_two_kinds_of_inplementation_10](charts/Performance_of_two_kinds_of_inplementation_10.png)

* Non-busy-waiting/semaphore    

|Item|1|2|3|4|5|6|7|8|9|10|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|AEVERAGE|932120.40|1370503.30|1829575.80|2285561.60|2734148.30|3186853.40|3627303.40|4106710.20|4555282.00|5076032.30|
|STDEV|90296.00|126882.57|172793.00|177417.17|188683.79|195322.46|209303.02|270088.13|279048.05|271880.42|

![Performance_analyses_semaphore_10](charts/Performance_analyses_semaphore_10.png)

* Busy-waiting

|Item|1|2|3|4|5|6|7|8|9|10|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|AEVERAGE|51372140.00|40077296.00|99761192.70|102897144.10|64054388.50|122244159.40|97201609.70|66905499.00|95434656.20|83018492.20|
|STDEV|70754196.43|73052704.85|106945463.12|126149250.17|114227753.82|121650495.98|121620927.78|113231037.71|90613342.55|119944286.88|

![Performance_analyses_busy-waiting_10](charts/Performance_analyses_busy-waiting_10.png)




2. N_LOOP = 50

![Performance_of_two_kinds_of_inplementation_50](charts/Performance_of_two_kinds_of_inplementation_50.png)

* Non-busy-waiting/semaphore    

|Item|1|2|3|4|5|6|7|8|9|10|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|AEVERAGE|952062.06|1404340.32|1858258.92|2318424.76|2777071.88|3240547.76|3684200.82|4175949.00|4675875.82|5166361.92|
|STDEV|202261.71|208502.52|221823.45|225574.13|233953.98|243500.53|252043.84|309197.04|434971.52|440096.43|

![Performance_analyses_semaphore_50](charts/Performance_analyses_semaphore_50.png)

* Busy-waiting

|Item|1|2|3|4|5|6|7|8|9|10|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|AEVERAGE|81401899.12|78595747.00|96720242.47|73802317.47|86406862.33|113321935.51|75721500.23|71811626.84|102355011.30|92631277.79|
|STDEV|80598657.30|83940348.92|106958346.35|88379818.08|106084843.00|114382633.24|102823248.70|88015500.51|100263936.56|87994272.34|

![Performance_analyses_busy-waiting_50](charts/Performance_analyses_busy-waiting_50.png)

