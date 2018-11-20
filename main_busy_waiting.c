#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

#define  N_BUFFER 2
#define  N_THREAD 3

// each pair of empty and full semaphores controls one buffer
int empty[N_BUFFER];
int full[N_BUFFER];

int mutex[2];

// two buffers with default values
char buffer[N_BUFFER] = {'a', 'a'};
char labels[N_THREAD] = {'A', 'B', 'C'};

void wait(int *i) {
    while (*i <= 0) {
        /* busy waiting */
    }
    --(*i);
}

void signal(int *i) {
    ++(*i);
}

void *processA(void *v) {
    char *l = (char *) v;

    while (1) {
        wait(&empty[0]);
        wait(&mutex[0]);
        printf("Process A is writing A into buffer1\n");
        buffer[0] = 'A';
        sleep(2);
        signal(&mutex[0]);
        signal(&full[0]);
    }
}

void *processB(void *v) {
    char *l = (char *) v;

    while (1) {
        wait(&full[0]);
        wait(&mutex[0]);
        char buffer1 = buffer[0];
        printf("Process B is reading %c from buffer1\n", buffer1);
        sleep(2);
        signal(&mutex[0]);
        signal(&empty[0]);

        sleep(1);

        wait(&empty[1]);
        wait(&mutex[1]);
        printf("Process B is writing %c into buffer2\n", buffer1);
        buffer[1] = buffer1;
        sleep(2);
        signal(&mutex[1]);
        signal(&full[1]);
    }
}

void *processC(void *v) {
    char *l = (char *) v;

    while (1) {
        wait(&full[1]);
        wait(&mutex[1]);
        char buffer2 = buffer[1];
        printf("Process C is reading %c from buffer2\n", buffer2);
        sleep(2);
        signal(&mutex[1]);
        signal(&empty[1]);
    }
}


/*
 *
 */
int main(int argc, char **argv) {

    for (int i = 0; i < N_BUFFER; i++) {
        mutex[i] = 1;
    }

    for (int i = 0; i < N_BUFFER; i++) {
        empty[i] = 1; // At the beginning, all buffers are "empty", so that process A can write/produce,
        full[i] = 0; // while the others have to wait because they are not full.
    }

    pthread_t threads[N_THREAD];
    int thread_ids[N_THREAD + 1];
    thread_ids[0] = pthread_create(&threads[0], NULL, processA, &labels[0]);
    thread_ids[1] = pthread_create(&threads[1], NULL, processB, &labels[1]);
    thread_ids[2] = pthread_create(&threads[2], NULL, processC, &labels[2]);

    for (int i = 0; i < N_THREAD; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}