#include <stdio.h>
#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>

#define  N_BUFFER 2
#define  N_THREAD 3

// each pair of empty and full semaphores decides one buffer
sem_t empty[N_BUFFER];
sem_t full[N_BUFFER];

sem_t mutex[2];

// two buffers with default values
char buffer[N_BUFFER] = {'a', 'a'};
char labels[N_THREAD] = {'A', 'B', 'C'};

void *processA(void *v) {
    char *l = (char *) v;

    while (1) {
        sem_wait(&empty[0]);
        sem_wait(&mutex[0]);
        printf("Process A is writing A into buffer1\n");
        buffer[0] = 'A';
        sleep(2);
        sem_post(&mutex[0]);
        sem_post(&full[0]);
    }
}

void *processB(void *v) {
    char *l = (char *) v;

    while (1) {
        sem_wait(&full[0]);
        sem_wait(&mutex[0]);
        char buffer1 = buffer[0];
        printf("Process B is reading %c from buffer1\n", buffer1);
        sleep(2);
        sem_post(&mutex[0]);
        sem_post(&empty[0]);

        sleep(1);

        sem_wait(&empty[1]);
        sem_wait(&mutex[1]);
        printf("Process B is writing %c into buffer2\n", buffer1);
        buffer[1] = buffer1;
        sleep(2);
        sem_post(&mutex[1]);
        sem_post(&full[1]);
    }
}

void *processC(void *v) {
    char *l = (char *) v;

    while (1) {
        sem_wait(&full[1]);
        sem_wait(&mutex[1]);
        char buffer2 = buffer[1];
        printf("Process C is reading %c from buffer2\n", buffer2);
        sleep(2);
        sem_post(&mutex[1]);
        sem_post(&empty[1]);
    }
}


/*
 *
 */
int main(int argc, char **argv) {

    for (int i = 0; i < N_BUFFER; i++) {
        sem_init(&mutex[i], 0, 1);
    }

    for (int i = 0; i < N_BUFFER; i++) {
        sem_init(&empty[i], 0, 1); // At the beginning, all buffers are "empty", so that process A can write/produce,
        sem_init(&full[i], 0, 0); // while the others have to wait because they are not full.
    }

    pthread_t threads[N_THREAD];
    int thread_ids[N_THREAD];
    thread_ids[0] = pthread_create(&threads[0], NULL, processA, &labels[0]);
    thread_ids[1] = pthread_create(&threads[1], NULL, processB, &labels[1]);
    thread_ids[2] = pthread_create(&threads[2], NULL, processC, &labels[2]);

    for (int i = 0; i < N_THREAD; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}